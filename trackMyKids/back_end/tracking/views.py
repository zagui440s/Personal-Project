from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Child, Location
from .serializers import ChildSerializer, LocationSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

class APIInfoAPIView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({
            'status': 'ok',
            'message': 'API is working!',
            'version': '1.0'
        })


# Child View (Handle GET/POST for Child)
class ChildListCreateAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # Get all children
        children = Child.objects.all()
        serializer = ChildSerializer(children, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        # Create a new child
        serializer = ChildSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Location View (Handle GET/POST for Location)
class LocationListCreateAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # Get all locations
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        # Create a new location
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
