from rest_framework import serializers


# in this example i am takeing two citys and returning distance.
class DistanceSerializer(serializers.Serializer):
    city1 = serializers.CharField(max_length=100)
    city2 = serializers.CharField(max_length=100)
    distance = serializers.CharField(required=False,max_length=100,allow_blank=True,read_only=True)
    
    def create(self,validated_data):
    	return Distance(**validated_data)