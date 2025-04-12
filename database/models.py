from tortoise.models import Model
from tortoise import fields

class DefectiveImage(Model):
    id = fields.IntField(pk=True)
    image_data = fields.BinaryField()
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "defective_images"
