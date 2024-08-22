from rest_framework import serializers

from .models import FaceEmbade



class FaceEmbadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaceEmbade
        fields = ['id','age','emotion','gender','timestamp']
