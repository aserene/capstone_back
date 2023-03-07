from .models import Entry
from rest_framework import serializers

class EntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        #Which model will get serialized by the class
        model= Entry
        #which fields should be included in the output
        fields = ['id','date','title', 'body', 'timestamp']