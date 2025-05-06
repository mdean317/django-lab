from rest_framework import serializers 
from .models import Locations 

class LocationsSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Locations # tell django which model to use
        fields = ('street', 'city', 'state',) # tell django which fields to include