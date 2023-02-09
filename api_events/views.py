from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView
from django.core.exceptions import PermissionDenied
from api_contracts.models import Contracts
from api_customers.models import Customers
from api_customers.permissions import VendeursPermissions
from api_customers.serializer import ClientSerialiser
from api_events.models import Events
from api_events.permissions import SupportPermissions
from api_events.serializer import EvenementSerialiser


class EvenementListes(generics.ListCreateAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = EvenementSerialiser

    def get_queryset(self):
        if self.request.user.assignment.department == 'Sales':
            return Events.objects.filter(sales_contact=self.request.user)
        elif self.request.user.assignment.department == 'Support':
            return Events.objects.filter(support_contact=self.request.user)



class EvenementCreer(CreateAPIView):

    permission_classes = [IsAuthenticated, VendeursPermissions]

    def create(self, request, *args, **kwargs):
        serialiser = EvenementSerialiser(data=request.data)
        if serialiser.is_valid():
            contrat = Contracts.objects.get(id=serialiser.validated_data['contract'].id)
            client = Customers.objects.filter(id=contrat.client_id)
            self.check_object_permissions(self.request, client)
            contrat.status = True
            contrat.save()
            serialiser.save(sales_contact=self.request.user)
            return Response(serialiser.data, status=status.HTTP_201_CREATED)
        return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)


class EvenementCorrectif(APIView):
    permission_classes = [IsAuthenticated, SupportPermissions]

    def patch(self, request, pk):
        evenement = Events.objects.filter(pk=pk)
        if not evenement:
            return Response({"erreur": "L'evenements existe pas !"},status=status.HTTP_404_NOT_FOUND)
        self.check_object_permissions(self.request, evenement)
        serialiser = EvenementSerialiser(evenement[0], data=request.data, partial=True)
        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data)
        return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)


class EvenementFiltre(generics.ListCreateAPIView):
    filter_fields = ('client__last_name', 'client__email', 'event_date')
    permission_classes = [IsAuthenticated, ]
    serializer_class = EvenementSerialiser
    
    def get_queryset(self):
        if self.request.user.assignment.department == 'Sales':
            return Events.objects.filter(sales_contact=self.request.user)
        elif self.request.user.assignment.department == 'Support':
            return Events.objects.filter(support_contact=self.request.user)

    def list(self, request, *args, **kwargs):
        listes = self.filter_queryset(self.get_queryset())
        if not listes:
            return Response({"erreur": "Pas de evenements existants"},status=status.HTTP_404_NOT_FOUND)
        self.check_object_permissions(self.request, listes)
        serialiser = self.get_serializer(listes, many=True)
        return Response(serialiser.data)
