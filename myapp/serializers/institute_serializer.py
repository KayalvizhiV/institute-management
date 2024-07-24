from rest_framework import serializers
from ..models.institute_model import InstituteModel

class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstituteModel
        fields = "__all__"