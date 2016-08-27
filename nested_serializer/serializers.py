from rest_framework import serializers
from .models import Person , Profile


class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
        model = Profile
        fields = ('person','fave_movie','fave_place','phonenumber',)
        read_only_fields=('id')



class PersonSerializer(serializers.ModelSerializer):
	profile = ProfileSerializer(many=True)
	class Meta:
		model = Person
		fields = ('username','firstname','lastname','profile')

		def create(self, validated_data):
		# This line will remove person values form serializers and stored in a 'Person_info '
		# This will gives us onley Profile data we will save profile and pass the Profile object
		# into Person modle.
        person_info = validated_data.pop('Person')
        # we have clean profile data we will save to the database and stored in profile_obj
        profile_obj = Profile.objects.create(**validated_data)
        # we are running loop the get the all values in Person
        for person_data in person_info:
            person = Person.objects.create(profile=profile_obj, **person_data)
        return person

