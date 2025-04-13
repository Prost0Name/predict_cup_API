from tortoise.models import Model
from tortoise import fields

class DefectiveImage(Model):
    id = fields.IntField(pk=True)
    image_data = fields.BinaryField()
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "defective_images"


class ProductionTime(Model):
    id = fields.IntField(pk=True)
    time = fields.DatetimeField(auto_now_add=True)
    is_defective = fields.BooleanField(default=False)

    class Meta:
        table = "production_time"