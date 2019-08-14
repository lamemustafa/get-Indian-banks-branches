from rest_framework import  serializers
from .models import IndianBanksBranches

class bank_details_Serializer(serializers.ModelSerializer):
     class Meta:
         model=IndianBanksBranches
         fields=('bank_name','branch','address','district','city','state','ifsc')

class branches_Serializer(serializers.ModelSerializer):
    class Meta:
        model=IndianBanksBranches
        fields=('ifsc','branch','address','district','state')