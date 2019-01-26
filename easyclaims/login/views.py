from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from login.models import User
from login.serializers import LoginSerializer

@csrf_exempt
def create(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LoginSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def login(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            user_details = User.objects.get(user_id=data['user_id'])
        except User.DoesNotExist:
            error={"error message":"user details not found"}
            return JsonResponse(error, status=404)
        serializer = LoginSerializer(user_details)
        if serializer.data['password'] == data['password']:
            return JsonResponse(serializer.data, status=201)
        else:
            error={"error message":"password is invalid"}
            return JsonResponse(error, status=400)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def validateuser(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            user_details = User.objects.get(user_id=data['user_id'])
        except User.DoesNotExist:
            error={"error message":"user details not found"}
            return JsonResponse(error, status=404)
        serializer = LoginSerializer(user_details)
        if serializer.data['dob'] == data['dob'] and serializer.data['postcode'] == data['postcode']:
            success={"success":"user exists"}
            return JsonResponse(success, status=201)
        else:
            error={"error message":"please enter correct combination of date of birth and post code"}
            return JsonResponse(error, status=400)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def update(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        try:
            user_details = User.objects.get(user_id=data['user_id'])
        except User.DoesNotExist:
            error={"error message":"user details not found"}
            return JsonResponse(error, status=404)
        serializer = LoginSerializer(user_details,data=data)
        if serializer.is_valid():
            serializer.save()
            success={"success":"password is updated successfully"}
            return JsonResponse(success)
        return JsonResponse(serializer.errors, status=400)
