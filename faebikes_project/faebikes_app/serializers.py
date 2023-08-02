from rest_framework import serializers
from .models import *

class faebikesSerializers(serializers.ModelSerializer):
    class Meta:
        model = faebikes
        fields="__all__"
