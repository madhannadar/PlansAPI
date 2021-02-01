from django.shortcuts import render
from rest_framework import viewsets
from service.serializer import PlansSerializer,CustomUserSerializer
from .models import Plans,CustomUser
from django.contrib.auth.models import User, Group
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.http import HttpResponse,JsonResponse   
from django.core import serializers
import json
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from service.backend import ExampleAuthentication
from service.permission import IsAuthenticatedExample
from rest_framework_simplejwt.authentication  import JWTAuthentication
from rest_framework.decorators import api_view
from .models import Testusers
from django.db.models import Q        
# Create your views here.

class PlansViewSet(viewsets.ModelViewSet):
    queryset = Plans.objects.all()
    serializer_class = PlansSerializer
    authentication_classes = [ExampleAuthentication]
    permission_classes = [IsAuthenticated]
    def destroy(self, request, *args, **kwargs):
        print(kwargs['pk'])
        # print(Plans.objects.get(plan_id=kwargs['pk']))
        try:
            p = Plans.objects.get(plan_id=kwargs['pk'])
        except Plans.DoesNotExist:
            p = None
        
        if p:
            p.delete()
            print("destroy")
            return Response({"status":"Successfulyy Deleted"},status=202)
        else:
            return Response({"error":"No Plans Found"},status=status.HTTP_404_NOT_FOUND)

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    authentication_classes = [ExampleAuthentication]
    permission_classes = (IsAuthenticatedExample,)

# class Plans1:
# 	@classmethod
# 	@csrf_exempt
# 	def addprofile(self,request):
# 		if request.method == 'POST':
# 			try:
# 				data = json.loads(request.body.decode('utf-8'),strict=False)
# 				try:
# 					# data= request.POST
# 					data = json.loads(request.body.decode('utf-8'),strict=False)
# 				except Exception as e:
# 					# return HttpResponse(traceback.format_exc())
# 					return JsonResponse({'error_code': '102','message':'Invalid json , please provide proper json input','data' : '' },safe=0)    
#         else:
#                 response = {'error_code': '104','message':'Invalid Request Method(Only POST method is allowed)','data' : ''}
#                 return JsonResponse(response)

def validateinput(input):
    print("inside validate",input)
    if(len(str(input)) < 1):
        return 1
    return 0

@csrf_exempt    
@api_view(['GET','POST'])
@authentication_classes([ExampleAuthentication])    
@permission_classes([IsAuthenticated])
def userlogin(request):
    print("inside view ######")
    if request.method == 'POST':
        # print(request.session_key)
        print(request.data['email'],request.data['password'])
        try:
            Testusers.objects.get(Q(email=request.data['email'])|Q(mobile=request.data['email']))
        except Testusers.DoesNotExist:
            return Response({"error": "No User Found","status":402})

        try:            
            Testusers.objects.get(Q(email=request.data['email'],password=request.data['password'])|Q(mobile=request.data['email'],password=request.data['password']))
            print("loggedin ins ")
            return Response({"message": "User logged in successfully","status":200},status=status.HTTP_200_OK)
        except Testusers.DoesNotExist:
            return Response({"error": "Invalid email address or password","status":401})
    return Response({"message": "Login View"})

@csrf_exempt    
@api_view(['GET','POST'])
@authentication_classes([ExampleAuthentication])    
@permission_classes([IsAuthenticated])
def userlogout(request):
    if request.method == 'POST':
        print(request.data['email'],request.data['password'])
        try:
            Testusers.objects.get(Q(email=request.data['email'])|Q(mobile=request.data['email']))
        except Testusers.DoesNotExist:
            return Response({"error": "No User Found","status":402})

        try:            
            Testusers.objects.get(Q(email=request.data['email'],password=request.data['password'])|Q(mobile=request.data['email'],password=request.data['password']))
            print("loggedin ins ")
            return Response({"message": "User logged out successfully","status":200},status=status.HTTP_200_OK)
        except Testusers.DoesNotExist:
            return Response({"error": "Invalid email address or password","status":401})
    return Response({"message": "logged out successfully"})

class PlansView:    
    @classmethod
    @csrf_exempt    
    # @api_view(['GET'])
    # @authentication_classes([ExampleAuthentication])    
    # @permission_classes([IsAuthenticated])
    def getplans(self,request):
        user = ExampleAuthentication().authenticate(request)
        print(user.status_code)
        if(user.status_code==200):
            print(user)
            error_arr = []        
            if(request.method == 'GET'):            
                # print(request.user)
                # plans = Plans.objects.all()
                plans = serializers.serialize('json', Plans.objects.all())
                # print("get",plans)
                # re
                return HttpResponse(plans, content_type="application/json")
            elif(request.method == 'POST'):
                try:
                    # data= request.POST
                    data = json.loads(request.body.decode('utf-8'),strict=False)

                    if(validateinput(data['plan_name'])):
                        error_arr.append({"error":"plan_name is missing"})

                    if(validateinput(data['plan_description'])):
                        error_arr.append({"error":"plan_description is missing"})

                    if(validateinput(data['plan_amount'])):
                        error_arr.append({"error":"plan_amount is missing"})

                    if(validateinput(data['plan_icon'])):
                        error_arr.append({"error":"plan_icon is missing"})  

                    if(validateinput(data['plan_type'])):
                        error_arr.append({"error":"plan_type is missing"}) 

                    if(validateinput(data['plan_service_id'])):
                        error_arr.append({"error":"plan_service_id is missing"}) 

                    if(validateinput(data['plan_gst_amount'])):
                        error_arr.append({"error":"plan_gst_amount is missing"})                                                             

                    if(validateinput(data['plan_video'])):
                        error_arr.append({"error":"plan_video is missing"})                                                                                 

                    if(validateinput(data['plan_sample_report'])):
                        error_arr.append({"error":"plan_sample_report is missing"})                                                             

                    if(validateinput(data['plan_original_price'])):
                        error_arr.append({"error":"plan_original_price is missing"})                                                             

                    if(validateinput(data['plan_isactive'])):
                        error_arr.append({"error":"plan_isactive is missing"})                                                             

                    if(validateinput(data['plan_created_by'])):
                        error_arr.append({"error":"plan_created_by is missing"})                                                                                                                                                             

                    print(error_arr)                
                    if(error_arr):
                        return JsonResponse({"error":error_arr},safe=False)
                    p = Plans(**data)
                    p.save()          
                    print(Plans.objects.get(plan_id=p.plan_id))      
                    plan = serializers.serialize('json', Plans.objects.filter(plan_id=p.plan_id))
                    # print(error_arr)                
                except Exception as e:
                    print(e)
                    # return HttpResponse(traceback.format_exc())
                    return JsonResponse({'error_code': '102','message':'Invalid json , please provide proper json input','data' : '' },safe=0)            
                return HttpResponse(plan, content_type="application/json")
            else:
                response = {'error_code': '104','message':'Invalid Request Method(Only POST method is allowed)','data' : ''}
                return JsonResponse(response)
            # print("get")          
        else:
            response = {'error_code': '104','message':'Invalid username or password','data' : ''}            
            return JsonResponse(response)
    # authentication_classes = [ExampleAuthentication]
# response = {'error_code': '104','message':'Invalid Request Method(Only POST method is allowed)','data' : ''}
# return JsonResponse(response)            