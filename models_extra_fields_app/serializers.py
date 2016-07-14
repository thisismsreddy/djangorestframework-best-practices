from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    phonenumber = serializers.CharField(max_length=100,write_only=True)
    
    class Meta:
        model = Person
        fields = ('id','username','firstname','lastname','phonenumber',)
        read_only_fields=('id')
