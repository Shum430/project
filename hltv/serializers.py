from rest_framework import serializers

from .models import *

class  TeamSerializer1(serializers.ModelSerializer):
    coach=serializers.StringRelatedField()
    class Meta:
        model = Team
        fields = ['name','points','country','logo','coach']