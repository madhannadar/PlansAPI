from rest_framework import serializers
from .models import Plans

class PlansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plans
        exclude = ('plan_id','plan_updated_date','last_modified' )
