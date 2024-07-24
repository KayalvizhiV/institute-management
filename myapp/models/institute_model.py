from django.db import models
from ..models.organization_model import OrganizationModel

class InstituteModel(models.Model):
    inst_id = models.BigIntegerField(primary_key=True)
    inst_name = models.CharField(max_length=100, blank=True, null=True)
    institute_short_name = models.CharField(max_length=100, blank=True, null=True)
    inst_desc = models.CharField(max_length=200, blank=True, null=True)
    inst_address01 = models.CharField(max_length=100, blank=True, null=True)
    inst_address02 = models.CharField(max_length=100, blank=True, null=True)
    inst_postal_code = models.IntegerField(blank=True, null=True)
    org = models.ForeignKey(OrganizationModel, on_delete=models.CASCADE, to_field='org_id', db_column='ORG_ID')
    inst_city = models.CharField(max_length=100, blank=True, null=True)
    inst_phone_num = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"kayal"."INSTITUTE"'