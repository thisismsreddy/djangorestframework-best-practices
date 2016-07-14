from rest_framework.response import Response 
from .serializers import DistanceSerializer
from rest_framework import status,views,generics
from django.shortcuts import render





# class DistanceView(views.APIView):
#     """
#     This api endpoint take two inputs and return result
#     """
    
#     def post(self, request, format=None):
#         serializer = DistanceSerializer(data=request.data)
#         if serializer.is_valid():
#             subject = serializer.validated_data.get('city1')
#             # In this example we can take extra argumnet make it optnal
#             #useing the .get method in python dic
#             # exp we need to add some other city between this two citys 
#             # in that case we can likethis
#             # validate_data.get('city3', None)
            
#             message = serializer.validated_data.get('city2')
#             #do something with data and return the data like dist(city1-city2)
#             s = serializer.data
#             # here we can perform any third party api calls and get the result and inject into dict
#             s.update({'distacne': subject+message})
#             return Response(s,status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class DistanceView(generics.CreateAPIView):
    """
    This api endpoint take two inputs and return result
    """
    serializer_class = DistanceSerializer
    def post(self, request, format=None):
        serializer = DistanceSerializer(data=request.data)
        if serializer.is_valid():
            subject = serializer.validated_data.get('city1')
            # In this example we can take extra argumnet make it optnal
            #useing the .get method in python dic
            # exp we need to add some other city between this two citys 
            # in that case we can likethis
            # validate_data.get('city3', None)
            
            message = serializer.validated_data.get('city2')
            #do something with data and return the data like dist(city1-city2)
            s = serializer.data
            # here we can perform any third party api calls and get the result and inject into dict
            s.update({'distacne': subject+message})
            return Response(s,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
