from rest_framework import serializers
from ..models.institute_model import InstituteModel

class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstituteModel
        fields = ["inst_id", "inst_name", "institute_short_name","inst_desc","inst_address01","inst_address02","inst_postal_code",
                  "org","inst_city","inst_phone_num","created_date","updated_date","created_by","updated_by"]
        # fields = "__all__"