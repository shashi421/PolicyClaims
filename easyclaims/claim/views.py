from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from claim.models import Claim
from insurances.models import Insurance
from claim.serializers import ClaimSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


class ClaimViewList(APIView):
    def get(self, request, format=None):
        snippets = Claims.objects.all()
        serializer =ClaimSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        #logger.debug('In post function call')
        serializer = ClaimSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClaimViewDetail(APIView):
     def get_object(self, pk):
        try:
            return Claim.objects.get(pk=pk)
        except Claim.DoesNotExist:
            raise Http404
     def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ClaimSerializer(snippet)
        return Response(serializer.data)
     def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer =ClaimSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ClaimStatusDetail(APIView):
    def get_object(self, pk):
        try:
            return Claim.objects.get(pk=pk)
        except List.DoesNotExist:
            raise Http404
    def post(self, request, pk, format=None):
        serializer = ClaimSerializer(data=request.data)
        snippet = self.get_object(pk)
        serializer = ClaimSerializer(snippet)
        claim_status = serializer.data['status']
        return JsonResponse(claim_status,safe=False)
         
@csrf_exempt
def createclaim(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            snippet = Insurance.objects.get(pk=data['policy_id'])
            print(snippet)
        except Insurance.DoesNotExist:
            return HttpResponse(status=404)
        serializer = ClaimSerializer(data=data)
        #print(serializer)
        if serializer.is_valid():
            serializer.save()
            success={"success":"Claim created successfully"}
            return JsonResponse(success, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def updateclaim(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        try:
            snippet = Claim.objects.get(pk=data['claim_id'])
            print(snippet)
        except Claim.DoesNotExist:
            return HttpResponse(status=404)
        serializer = ClaimSerializer(snippet,data=data)
        if serializer.is_valid():
            serializer.save()
            success={"success":"Claim updated successfully"}
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def getclaims(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            snippet = Claim.objects.filter(policy_id=data['policy_id'],user_id=data['user_id'])
        except Insurance.DoesNotExist:
            return HttpResponse(status=404)
        else:
            serializer = ClaimSerializer(snippet,many=True)
            return JsonResponse(serializer.data,safe=False)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def getclaimsforadmin(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets=Claim.objects.all()
        serializer = ClaimSerializer(snippets,many=True)
        return JsonResponse(serializer.data,safe=False)
        

