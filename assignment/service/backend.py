from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

from service.models import Testusers

from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions
from rest_framework import HTTP_HEADER_ENCODING, exceptions
import base64
import binascii
from django.http import JsonResponse
from rest_framework import status

class ExampleAuthentication(authentication.BaseAuthentication):
    def get_authorization_header(self,request):
        """
        Return request's 'Authorization:' header, as a bytestring.
        Hide some test client ickyness where the header can be unicode.
        """
        auth = request.META.get('HTTP_AUTHORIZATION', b'')
        if isinstance(auth, str):
            # Work around django test client oddness
            auth = auth.encode(HTTP_HEADER_ENCODING)
        return auth

    def get_user(self, user_id):
        # get a user from the user_id
        try:
            return Testusers.objects.get(pk=user_id)
        except Testusers.DoesNotExist:
            return None
    def authenticate(self,request,username=None,password=None,**kwargs):
        # print(self)
        print("-----------authentication backen")
        print(username,password)
        auth = self.get_authorization_header(request).split()
        print("------",auth)
        if not auth or auth[0].lower() != b'basic':
            print("no auth")
            # return JsonResponse("data", status=status.HTTP_400_BAD_REQUEST,safe=False)
            return None

        if len(auth) == 1:
            msg = _('Invalid basic header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _('Invalid basic header. Credentials string should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)        
        try:
            try:
                auth_decoded = base64.b64decode(auth[1]).decode('utf-8')
            except UnicodeDecodeError:
                auth_decoded = base64.b64decode(auth[1]).decode('latin-1')
            auth_parts = auth_decoded.partition(':')
        except (TypeError, UnicodeDecodeError, binascii.Error):
            msg = _('Invalid basic header. Credentials not correctly base64 encoded.')
            raise exceptions.AuthenticationFailed(msg)        
        # print(request.body)
        # print(request.META)
        userid, password = auth_parts[0], auth_parts[2]
        # credential_list = request.META['HTTP_AUTHORIZATION'].split(' ') # get the username request header
        # username = None
        # username = credential_list[0]
        # print(credential_list[0]
        if not userid: # no username passed in request headers
            return None # authentication did not succeed
        try:
            user = Testusers.objects.get(email=userid) # get the user
        except Testusers.DoesNotExist:            
            # return JsonResponse("data", status=status.HTTP_400_BAD_REQUEST,safe=False)
            raise exceptions.AuthenticationFailed('No such user') # raise exception if user does not exist 
            # return return JsonResponse(response)
        try:
            user = Testusers.objects.get(email=userid,password=password)
        except Testusers.DoesNotExist:
            print("does not exist")
            raise exceptions.AuthenticationFailed('Invalid username or password') # raise exception if user does not exist             
            # response = {'error_code': '104','message':'Invalid username or password','data' : ''}            
            # return JsonResponse(response)
        print("done",user.email)   
        user.is_authenticated = True
        return (user, None) # authentication successful
        # return user
    # def customauthenticate(self,userid=None,password=None):
    #     try:
    #         user = Testusers.objects.get(username=userid) # get the user
    #     except Testusers.DoesNotExist:            
    #         # return JsonResponse("data", status=status.HTTP_400_BAD_REQUEST,safe=False)
    #         raise exceptions.AuthenticationFailed('No such user') # raise exception if user does not exist 
    #         # return return JsonResponse(response)
    #     try:
    #         user = Testusers.objects.get(username=userid,password=password)
    #     except Testusers.DoesNotExist:
    #         print("does not exist")
    #         raise exceptions.AuthenticationFailed('Invalid username or password') # raise exception if user does not exist             
    #         # response = {'error_code': '104','message':'Invalid username or password','data' : ''}            
    #         # return JsonResponse(response)
    #     print("done",user.username)   
    #     user.is_authenticated = True
    #     return user# authentication successful        