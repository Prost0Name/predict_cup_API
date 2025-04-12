import tensorflow as tf
import numpy as np
from PIL import Image
import os

class CupClassifier:
    def __init__(self, model_path='cup_classifier.keras'):
        try:
            model_path = os.path.join(os.path.dirname(__file__), model_path)
            print(f"TensorFlow version: {tf.__version__}")
            print(f"Loading model from: {model_path}")
            print(f"File exists: {os.path.exists(model_path)}")
            print(f"File size: {os.path.getsize(model_path)} bytes")
            
            # Try to load the model with custom objects
            self.model = tf.keras.models.load_model(
                model_path,
                custom_objects=None,
                compile=False  # Don't compile the model on load
            )
            print("Model loaded successfully")
            print(f"Model summary: {self.model.summary()}")
            self.img_size = (224, 224)
        except Exception as e:
            print(f"Detailed error loading model: {str(e)}")
            print(f"Error type: {type(e).__name__}")
            import traceback
            print(f"Stack trace: {traceback.format_exc()}")
            raise

    def preprocess_image(self, image_path):
        try:
            img = Image.open(image_path)
            img = img.convert('RGB')
            img = img.resize(self.img_size)
            img_array = np.array(img) / 255.0
            img_array = np.expand_dims(img_array, axis=0)
            return img_array
        except Exception as e:
            print(f"Error preprocessing image: {str(e)}")
            raise

    def predict(self, image_path, threshold=0.5):
        try:
            processed_img = self.preprocess_image(image_path)
            prediction = self.model.predict(processed_img)[0][0]
            return 'defective' if prediction < threshold else 'good'
        except Exception as e:
            print(f"Error during prediction: {str(e)}")
            raise

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('image_path', help='Path to the image for prediction')
    # args = parser.parse_args()

    classifier = CupClassifier()
    result = classifier.predict("/content/train/defective/buyxmztmmy.jpg")
    print(f'Prediction: {result}')