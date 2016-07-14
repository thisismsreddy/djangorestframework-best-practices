from rest_framework.response import Response 
from rest_framework import status,views,generics
from django.shortcuts import render
from .serializers import PersonSerializer
from .models import Person


class PersonView(generics.CreateAPIView):
    """
    This api endpoint take user phonenumber but
    it's not a database filed it's extra field
    """
    serializer_class = PersonSerializer
    def perform_create(self,serializer):
        serializer = PersonSerializer(data=self.request.data)
        if serializer.is_valid():
            phoneno = serializer.validated_data.get('phonenumber')
            print('phonenumber')
            # here I am calling third party api for some verifaction
            # we can put a try and except statement for verifaction
            # am not doing anything here in this exaple
            person = Person(
                username = serializer.validated_data.get('username'),
                # First name and last name or optnal if your dont 
                #chose any i am passing None object
                firstname = serializer.validated_data.get('firstname', None),
                lastname = serializer.validated_data.get('lastname', None),

                )
            person.save()