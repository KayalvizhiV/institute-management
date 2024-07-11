from django.db import models

class OrganizationModel(models.Model):
    org_id = models.BigIntegerField(primary_key=True)
    org_name = models.CharField(max_length=100, blank=True, null=True)
    org_short_name = models.CharField(max_length=100, blank=True, null=True)
    org_desc = models.CharField(max_length=200, blank=True, null=True)
    org_address01 = models.CharField(max_length=100, blank=True, null=True)
    org_address02 = models.CharField(max_length=100, blank=True, null=True)
    org_postal_code = models.IntegerField(blank=True, null=True)
    org_city = models.CharField(max_length=100, blank=True, null=True)
    org_phone_num = models.IntegerField(blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '"kayal"."ORGANIZATION"'