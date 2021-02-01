from django.contrib.sessions.models import Session
from service.backend import ExampleAuthentication
from datetime import datetime
from rest_framework import HTTP_HEADER_ENCODING, exceptions
import base64
import binascii
from .models import Testusers,LoggedInUser
from django.http import HttpResponse,JsonResponse   
import ast
import json 

class BaseMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

class OneSessionPerUserMiddleware(BaseMiddleware):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        # print("calllllllllllllll")
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        return response      

    def getheader(self,auth):
        auth = auth.split()
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
        userid, password = auth_parts[0], auth_parts[2]    
        return userid,password 

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('----- Middleware view %s' % view_func.__name__)
        print("view args",request.META)
        print(request.META.get('PATH_INFO'))

        if request.META.get('PATH_INFO') == "/api/login":
            if request.META.get('REQUEST_METHOD') == "GET": 
                return JsonResponse({"error":"Post method not allowed"})
            else:
                print("inside login middle",request.body)
                body = request.body
                dict_str = body.decode("UTF-8")
                # print(dict_str)
                mydata = json.loads(dict_str)
                print(mydata['email'])
                username,password = mydata['email'],mydata['password']
        else:
            header_token = request.META.get('HTTP_AUTHORIZATION', None)
            print(header_token)
            if header_token is not None:
                # try:
                auth = request.META.get('HTTP_AUTHORIZATION', b'')
                if isinstance(auth, str):
                    # Work around django test client oddness
                    auth = auth.encode(HTTP_HEADER_ENCODING)
                username,password = self.getheader(auth)
            else:
                    return JsonResponse({"error":"header is missing"})
        try:
            # token = sub('Token ', '', request.META.get('HTTP_AUTHORIZATION', None))
            testuser = Testusers.objects.get(email = username,password=password)
            
            print("test user",testuser)                
        except Testusers.DoesNotExist:
            return JsonResponse({"error":"Invalid username or password"})

        if request.META.get('PATH_INFO') == "/api/logout":
            print("logout")    
            try:                        
                LoggedInUser.objects.get(user=testuser).delete()
            except LoggedInUser.DoesNotExist:
                return JsonResponse({"error":"User already logged off"})
        else:
            try:
                userobj = LoggedInUser.objects.get(user=testuser)
                return JsonResponse({"error":"User already logged in from another device"})
            except LoggedInUser.DoesNotExist:
                userobj = LoggedInUser(user=testuser,session_key="123")
                userobj.save()
                # return JsonResponse({"data":"User  succesfully logged in"})

            print(request.user)        
            # request = request.META
            request.getdetail = "Madhan"
            # response = self.get_response(request)
            # return request
    def process_response(request, response):
        print("Response ")
        return None


