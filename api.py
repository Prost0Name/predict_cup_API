from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import uvicorn
from predict import CupClassifier
import io
from PIL import Image
from tortoise.contrib.fastapi import register_tortoise
from database.models import DefectiveImage, ProductionTime
import os

app = FastAPI()
classifier = CupClassifier()

@app.post("/predict")
async def predict_image(file: UploadFile = File(...)):
    try:
        # Read the uploaded file
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        
        # Save the image temporarily
        temp_path = "temp_image.jpg"
        image.save(temp_path)
        
        # Make prediction
        result = classifier.predict(temp_path)
        print(result)
        # If the prediction is defective, store the image in the database
        if result == "defective":
            await DefectiveImage.create(image_data=contents)
            await ProductionTime.create(is_defective=True)
        else:
            await ProductionTime.create(is_defective=False)
        # Clean up temporary file
        if os.path.exists(temp_path):
            os.remove(temp_path)
        
        return JSONResponse(content={"prediction": result})
    except Exception as e:
        try:
            await ProductionTime.create()
        except Exception as e:
            print("Error saving production time:", e)
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )

async def setup():
    config = uvicorn.Config(app, host="0.0.0.0", port=8000)
    server = uvicorn.Server(config)
    await server.serve() 
