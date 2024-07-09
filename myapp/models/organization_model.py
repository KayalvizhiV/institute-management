from django.db import models

class OrganizationModel(models.Model):
    """Organization"""

    org_id = models.IntegerField(db_column='ORG_ID', max_length=20)
    org_name = models.CharField(db_column='ORG_NAME',max_length=100)
    org_short_name = models.CharField(db_column='ORG_SHORT_NAME', max_length=100)
    org_desc = models.CharField(db_column='ORG_DESC', max_length=200)
    org_addr1 = models.CharField(db_column='ORG_ADDRESS01', max_length=100)
    org_addr2 = models.CharField(db_column='ORG_ADDRESS02', max_length=100)
    postal_code = models.IntegerField(db_column='ORG_POSTAL_CODE',max_length=8)
    city = models.CharField(db_column='ORG_CITY', max_length=100)
    phone_num = models.IntegerField(db_column='ORG_PHONE_NUM', max_length=10)
    active = models.CharField(db_column='ACTIVE', max_length=1)
    created_date = models.DateTimeField(db_column='CREATED_DATE')
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')
    created_by = models.CharField(db_column='CREATED_BY', max_length=100)
    updated_by = models.CharField(db_column='UPDATED_BY', max_length=100)

    class Meta:
        """ Specifing table name"""
        db_table = '[ORGANIZATION]'
        managed = False
