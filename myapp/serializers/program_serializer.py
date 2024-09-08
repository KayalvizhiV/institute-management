from rest_framework import serializers
from ..models.program_model import ProgramModel

class ProgramSerializer(serializers.ModelSerializer):
    """Program Serializer class"""
    class Meta:
        """ Meta class for Program Serializer"""
        model=ProgramModel
        fields = "__all__"