import datetime
from rest_framework.response import Response
from rest_framework import serializers
from .models import Events
from api_contracts.models import Contracts 


class EvenementSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['id','date_created','date_updated','attendees','event_date','status','notes','client','contract','support_contact']
