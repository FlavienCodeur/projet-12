from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from api_customers.models import Customers
from api_customers.permissions import VendeursPermissions
from api_customers.serializer import ClientSerialiser
from api_events.models import Events

class ClientQueryset(generics.ListCreateAPIView):
    serializer_class = ClientSerialiser
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.assignment.department == 'Sales':
            return Customers.objects.filter(sales_contact=self.request.user)
        elif self.request.user.assignment.department == 'Support':
                client_evenements = [event.client.id for event in Events.objects.filter(support_contact=self.request.user.pk)]
                return Customers.objects.filter(id__in=client_evenements)
        else: 
            return Customers.objects.all()
    

class ClientCreer(CreateAPIView):
    permission_classes = [IsAuthenticated, VendeursPermissions]

    def create(self, request, *args, **kwargs):
        serialiser = ClientSerialiser(data=request.data)
        if serialiser.is_valid():
            serialiser.save(sales_contact=self.request.user)
            return Response(serialiser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientCorrectif(APIView):
    permission_classes = [IsAuthenticated, VendeursPermissions]

    def patch(self, request, pk):
        client = get_object_or_404(Customers, pk=pk)
        self.check_object_permissions(self.request, client)
        serialiser = ClientSerialiser(client, data=request.data, partial=True)
        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data)
        return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientFiltre(generics.ListCreateAPIView):
    filter_fields = ('last_name', 'email',)
    serializer_class = ClientSerialiser
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        if self.request.user.assignment.department == 'Sales':
            return Customers.objects.filter(sales_contact=self.request.user)
        elif self.request.user.assignment.department == 'Support':
            client_evenements = [event.client.id for event in Events.objects.filter(support_contact=self.request.user.pk)]
            return Customers.objects.filter(id__in=client_evenements)
            
    def list(self, request, *args, **kwargs):
        listes = self.filter_queryset(self.get_queryset())
        if not listes:
            return Response({"erreur": "Le client que souhaitez avoir n'existe pas"},status=status.HTTP_404_NOT_FOUND)
        self.check_object_permissions(self.request, listes)
        serialiser = self.get_serializer(listes, many=True)
        return Response(serialiser.data)
