from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api_contracts.views import ContratListes, ContratCreer, ContratFiltre, ContratCorrectif
from api_customers.views import ClientQueryset, ClientCreer, ClientFiltre, ClientCorrectif
from api_events.views import EvenementListes, EvenementCreer, EvenementFiltre, EvenementCorrectif

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/login/', TokenObtainPairView.as_view()),
    path('authentication/refresh-token/', TokenRefreshView.as_view()),
    path('api/clients/', ClientQueryset.as_view(), name='client-list'),
    path('api/creer-client/', ClientCreer.as_view(), name='client-creation'),
    path('api/clients', ClientFiltre.as_view(), name='client-filtre'),
    path('api/clients/<int:pk>/', ClientCorrectif.as_view(), name='client-maj'),
    path('api/contrats/', ContratListes.as_view(), name='contrats-liste'),
    path('api/creer-contrat/', ContratCreer.as_view(), name='contrat-creer'),
    path('api/contrats', ContratFiltre.as_view(), name='contrat-filtre'),
    path('api/contrats/<int:pk>/', ContratCorrectif.as_view(), name='contract-maj'),
    path('api/evenement/', EvenementListes.as_view(), name='evenement-liste'),
    path('api/creer-evenement/', EvenementCreer.as_view(), name='evenement-creation'),
    path('api/evenement', EvenementFiltre.as_view(), name='evenement-filtre'),
    path('api/evenement/<int:pk>/', EvenementCorrectif.as_view(), name='evenement-maj'),

]
