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

# in this exaple we are using user login state.
# writeing onley one view we have all four methods 
# get(pk),patch(pk),put(pk),delete(pk).
# we allowing onley asisiated user to perform any action

class PersonDetailView(generics.RetrieveUpdateDestroyAPIView):

    model = Person
    serializer_class = PersonSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )


    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user.id)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)            