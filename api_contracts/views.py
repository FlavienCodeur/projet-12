from django.shortcuts import get_object_or_404
from rest_framework import status , generics
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from api_events.models import Events
from api_contracts.models import Contracts
from api_contracts.serializer import ContratSerialiser
from api_customers.models import Customers
from api_customers.permissions import VendeursPermissions


class ContratListes(generics.ListCreateAPIView):

    serializer_class = ContratSerialiser
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        if self.request.user.assignment.department == 'Sales':
            return Contracts.objects.filter(sales_contact=self.request.user)
        elif self.request.user.assignment.department == 'Support':
            client_contrat_assigne = [event.client.id for event in Events.objects.filter(support_contact=self.request.user)]
            return Contracts.objects.filter(client__in=client_contrat_assigne)

    def create(self, request, *args, **kwargs):
        serialiser = ContratSerialiser(data=request.data)
        if serialiser.is_valid():
            client = Customers.objects.filter(id=serialiser.validated_data['client'].id)
            self.check_object_permissions(self.request, client)
            serialiser.save(sales_contact=self.request.user)
            return Response(serialiser.data, status=status.HTTP_201_CREATED)
        return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)


class ContratCorrectif(APIView):
    permission_classes = [IsAuthenticated, VendeursPermissions]
    
    def patch(self, request, pk):
        contrat = get_object_or_404(Contracts, pk=pk)
        client = Customers.objects.get(id=contrat.client_id)
        self.check_object_permissions(self.request, client)
        serialiser = ContratSerialiser(contrat, data=request.data, partial=True)
        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data)
        return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)





