from rest_framework import serializers
from .models import Faculty
from base_files.models import BaseModel


class BaseFieldsSerializeres(serializers.ModelSerializer):
    class Meta:
        model = BaseModel
        fields = ('id','created_at','updated_at')
        



class FacultySerializers(serializers.ModelSerializer):
    base = BaseFieldsSerializeres()
    class Meta:
        model = Faculty
        fields = ('base' ,'name')