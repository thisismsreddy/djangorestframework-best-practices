from django.shortcuts import render
from rest_framework import status,views
from rest_framework.response import Response 
from .serializers import DistanceSerializer


class DistanceView(views.APIView):
    
    def post(self, request, format=None):
        serializer = DistanceSerializer(data=request.data)
        if serializer.is_valid():
            subject = serializer.validated_data.get('city1')
            message = serializer.validated_data.get('city2')
            #do something with data and return the data like dist(city1-city2)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
