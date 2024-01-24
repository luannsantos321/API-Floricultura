from rest_framework import serializers
from .models import Flor

class FlorSerializers(serializers.ModelSerializer):
    class  Meta:
        model = Flor
        fields = '__all__'