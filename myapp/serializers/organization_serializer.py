from rest_framework import serializers
from ..models.organization_model import OrganizationModel

class OrganizationSerializer(serializers.ModelSerializer):
    """  OrganizationSerializer class"""
    class Meta:
        """ Meta class for OrganizationSerializer"""
        model=OrganizationModel
        # fields = ['org_id','org_name','org_short_name','org_desc','org_addr1','org_addr2','postal_code','city',\
                #   'phone_num','active','created_date','updated_date','created_by','updated_by']
        fields = ['org_id','org_name','org_short_name','org_desc','org_addr1','org_addr2','postal_code','city',\
                  'phone_num','active']
        # fields = "_all__"
