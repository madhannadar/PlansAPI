from django.db import models

# Create your models here.
class Plans(models.Model):
    plan_id = models.IntegerField(primary_key=True)
    plan_name = models.CharField(max_length=765, blank=True, null=True)
    plan_description = models.TextField(blank=True, null=True)
    plan_amount = models.IntegerField(blank=True, null=True)
    plan_added = models.DateTimeField(blank=True, null=True)
    plan_icon = models.CharField(max_length=300, blank=True, null=True)
    plan_type = models.CharField(max_length=3, blank=True, null=True)
    plan_service_id = models.IntegerField(blank=True, null=True)
    plan_gst_amount = models.IntegerField(blank=True, null=True)
    plan_video = models.TextField(blank=True, null=True)
    plan_sample_report = models.TextField(blank=True, null=True)
    plan_original_price = models.IntegerField(blank=True, null=True)
    plan_isactive = models.CharField(db_column='plan_isActive', max_length=3, blank=True, null=True)  # Field name made lowercase.
    plan_created_by = models.IntegerField(blank=True, null=True)
    plan_updated_date = models.DateTimeField(blank=True, null=True)
    plan_updated_by = models.IntegerField(blank=True, null=True)
    last_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'plans'
