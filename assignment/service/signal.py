from django.contrib.auth import user_logged_in, user_logged_out
from django.dispatch import receiver
from rest_framework import HTTP_HEADER_ENCODING, exceptions
import base64
import binascii
# from service.models import LoggedInUser

print("signal")

@receiver(user_logged_in)
def on_user_logged_in(sender, request, **kwargs):
    print("user logged in")
    LoggedInUser.objects.get_or_create(user=kwargs.get('user')) 


@receiver(user_logged_out)
def on_user_logged_out(sender, **kwargs):
    LoggedInUser.objects.filter(user=kwargs.get('user')).delete()

def log_request(sender,**kwargs):
    from service.backend import ExampleAuthentication    
    from .models import LoggedInUser
    # print(kwargs)
    # print("new req",kwargs.get('environ').get('HTTP_AUTHORIZATION',b''))
    auth = kwargs.get('environ').get('HTTP_AUTHORIZATION',b'')
    # print("auth",auth)
    if isinstance(auth, str):
        # print("encodinf")
        # Work around django test client oddness
        auth = auth.encode(HTTP_HEADER_ENCODING)
    # print("credential",auth)

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
    # print(request.body)
    # print(request.META)
    userid, password = auth_parts[0], auth_parts[2]    
    print(userid,password)
    user = ExampleAuthentication().customauthenticate(userid,password)
    print("user object ",user.username)
    # LoggedInUser.objects.get_or_create(user) 
    # auth = auth.encode()
    # print("service auth",auth)
    # print("new request resuest fron client")