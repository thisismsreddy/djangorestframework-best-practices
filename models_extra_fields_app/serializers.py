from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
	# this can be a model method or serializer method we need specifi the soure 
	# exp if have model method i would say(source = 'getmephonenumber')

	#phonenumber = serializers.CharField(source='getmephoneno',write_only=True)

	# or we can write a SerializerMethodField http://www.django-rest-framework.org/api-guide/fields/#modelfield

	#phonenumber = serializers.SerializerMethodField(method_name=None)
	#Hint you have to user get_method_name exp(get_is_user_has_account)

    phonenumber = serializers.CharField(max_length=100,write_only=True)
    
    class Meta:
        model = Person
        '''
       	def is_user_has_accout(self,phonenumber):
       		# perfoming some api call or database lookup
       		# like phonenumbber == "something"
       		return 
       	'''	
        fields = ('id','username','firstname','lastname','phonenumber',)
        read_only_fields=('id')

        #This pice of code givews you to coustem error handling,Beset pratices is tell like 
        #Username is require radhar then {Username:[this filed is required]} I found this is 
        #use full while working with forntend javascript
        def __init__(self, *args, **kwargs):
        super(UserRegistrationSerializer, self).__init__(*args, **kwargs)
        
        for field in self.Meta.fields:
            self.fields[field].error_messages['required'] = "%s is required" % field




