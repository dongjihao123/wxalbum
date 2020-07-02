from django.db import models

# Create your models here.
import mongoengine
class photomodel(mongoengine.Document):
    name = mongoengine.StringField(max_length=64)
    created_at = mongoengine.StringField(default=0)
    size = mongoengine.StringField(default=0)