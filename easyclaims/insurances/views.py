from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from insurances.models import Insurance
from insurances.serializers import InsuranceSerializer

@csrf_exempt
def createpolicy(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = InsuranceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            success={"success":"policy created successfully"}
            return JsonResponse(success, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def updatepolicy(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        try:
            snippet = Insurance.objects.get(pk=data['policy_id'])
        except Insurance.DoesNotExist:
            return HttpResponse(status=404)
        serializer = InsuranceSerializer(snippet,data=data)
        if serializer.is_valid():
            serializer.save()
            success={"success":"policy updated successfully"}
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def getpolicy(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            snippet = Insurance.objects.get(pk=data['policy_id'])
        except Insurance.DoesNotExist:
            return HttpResponse(status=404)
        else:
            serializer = InsuranceSerializer(snippet)
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)



@csrf_exempt
def getallpolicy(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            snippet = Insurance.objects.filter(user_id_id=data['user_id'])
        except Insurance.DoesNotExist:
            return HttpResponse(status=404)
        else:
            serializer = InsuranceSerializer(snippet,many=True)
            return JsonResponse(serializer.data,safe=False)
        return JsonResponse(serializer.errors, status=400)


