from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager
# Create your models here.
class Plans(models.Model):
    plan_id = models.AutoField(primary_key=True,null=False)
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
        managed = True
        db_table = 'plans'

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    password_reset_status_choices = member_display_flag_choices = (
        ('0', '0'),
        ('1', '1')
    )

    user_aof_status_choices =  (
        ('single', 'single'),
        ('joint', 'joint'),
        ('anyone_survivor', 'anyone_survivor')
    )



    user_dependants_choices =(
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6')
    )
    questionnaire_flag_choices =(
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4')
    )
    fhc_flag_choices =(
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
        
    )
    bse_reg_choices =(
        ('Y','Y'),
        ('N','N'),
    )
    
    bse_aof_status_choices =(
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
    )
    
    # id = models.BigAutoField(primary_key=True)
    email = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    salutation = models.CharField(max_length=10)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    rm_id = models.IntegerField(default=0)
    mobile = models.CharField(max_length=255)
    designation_id = models.IntegerField(default=0)
    company_id = models.IntegerField(default=0)
    branch_id = models.IntegerField(default=0)
    landline = models.CharField(max_length=255)
    dob = models.CharField(max_length=255)
    pan = models.CharField(max_length=15)
    flat_no = models.CharField(max_length=50)
    building_name = models.CharField(max_length=50)
    road_street = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    pincode = models.IntegerField(default=0)
    user_location = models.IntegerField(default=0)
    user_tax_status = models.IntegerField(default=0)
    gender = models.CharField(max_length=255)
    tags = models.TextField()
    father_name = models.CharField(max_length=255)
    occupation = models.IntegerField(default=0)
    marital_status = models.CharField(max_length=50)
    spouse_name = models.CharField(max_length=255)
    guardian_name = models.CharField(max_length=255)
    guardian_relation = models.CharField(max_length=50)
    relation = models.CharField(max_length=50)
    residential_status = models.IntegerField(default=0)
    parent_user_id = models.IntegerField(default=0)
    member_display_flag = models.CharField(max_length=1,choices=member_display_flag_choices,default='1')
    user_comments = models.TextField()
    bse_status_id = models.IntegerField(default=0)
    fhc_password = models.CharField(max_length=255)
    fp_password = models.CharField(max_length=255)
    mf_password = models.CharField(max_length=255)
    fg_regdate = models.DateTimeField(auto_now_add=True, blank=True)
    regdate = models.DateTimeField(auto_now_add=True, blank=True)
    password_reset_status = models.CharField(max_length=1,choices=password_reset_status_choices,default='0')
    IncomeSlabID = models.IntegerField(default=0)  # Field name made lowercase.
    tax_slab = models.CharField(max_length=20)
    huf = models.IntegerField(default=0)
    will = models.IntegerField(default=0)
    contact_fh = models.IntegerField(default=0)
    contact_w_fh = models.IntegerField(default=0)
    call_back_mobile = models.TextField()
    user_investor_id = models.IntegerField(default=0)
    profile_picture = models.TextField()
    requested_member = models.TextField(blank=True, null=True)
    user_holding_nature = models.CharField(max_length=20    ,choices=user_aof_status_choices,default='0')
    joint_survivor_user_id = models.IntegerField(default=0)
    user_dependants = models.CharField(max_length=1,choices=user_dependants_choices,default='0')
    questionnaire_flag = models.CharField(max_length=1,choices=questionnaire_flag_choices,default='1')
    questionnaire_date = models.DateTimeField(blank=True, null=True)
    fhc_flag = models.CharField(max_length=1,choices=fhc_flag_choices,default='1')
    fhc_date = models.DateTimeField(blank=True, null=True)
    bse_reg = models.CharField(max_length=1,choices=bse_reg_choices,default='N')
    bse_aof_status = models.CharField(max_length=1, choices=bse_aof_status_choices,default='0')
    bse_aof_remark = models.CharField(max_length=1000, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password','name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email