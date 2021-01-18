from rest_framework import serializers
from .models import Plans

class PlansSerializer(serializers.ModelSerializer):
    class Meta:
        # fields = "__all__"
        # read_only_fields = ['plan_id']
        exclude = ['last_modified']
        model = Plans

    def get_fields(self, *args, **kwargs):
        fields = super(PlansSerializer, self).get_fields(*args, **kwargs)
        request = self.context.get('request', None)
        if request and getattr(request, 'method', None) == "PUT":
            fields['plan_id'].required = False
        return fields
    # def update(self, instance, validated_data):
        # validated_data.pop('plan_id', None)  # prevent myfield from being updated
        # return super().update(instance, validated_data)        
