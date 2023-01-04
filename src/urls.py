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

]
