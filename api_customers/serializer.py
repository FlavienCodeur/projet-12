from rest_framework.serializers import ModelSerializer

from api_customers.models import Customers


class ClientSerialiser(ModelSerializer):
    class Meta:
        model = Customers
        fields = ['id','first_name','last_name','email','phone','mobile','company_name','sales_contact']
        extra_kwargs = {'sales_contact': {'read_only': True}}
