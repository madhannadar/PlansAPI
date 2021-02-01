from rest_framework import serializers
from .models import Plans,CustomUser
from rest_framework_jwt.settings import api_settings
from service.backend import ExampleAuthentication
class PlansSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        # read_only_fields = ['plan_id']
        # exclude = ['last_modified']
        model = Plans

    # def get_fields(self, *args, **kwargs):
    #     fields = super(PlansSerializer, self).get_fields(*args, **kwargs)
    #     request = self.context.get('request', None)
    #     if request and getattr(request, 'method', None) == "PUT" or getattr(request, 'method', None) == "POST" :
    #         fields['plan_id'].required = False
    #     return fields
    # def update(self, instance, validated_data):
        # validated_data.pop('plan_id', None)  # prevent myfield from being updated
        # return super().update(instance, validated_data)        

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER
from rest_framework_jwt.settings import api_settings
class CustomUserSerializer(serializers.ModelSerializer):
    print("-------serializer")
    class Meta:
        fields = "__all__"
        # read_only_fields = ['plan_id']
        # exclude = ['last_modified']
        model = CustomUser
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user
    def validate(self,data):
        username = data.get("email", None)
        password = data.get("password", None)
        print("yes validate")   
        user = ExampleAuthentication.authenticate(self,None,username=username, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )        
        print(user[0].username)

        payload = JWT_PAYLOAD_HANDLER(user)
        jwt_token = JWT_ENCODE_HANDLER(payload)
        print(jwt_token)