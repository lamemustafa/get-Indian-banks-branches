from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import logging
from .models import IndianBanksBranches
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions
from .serializers import bank_details_Serializer,branches_Serializer

logging = logging.getLogger('__name__')

def index(request):
    if request.method == 'GET':
        if 'ifsc' in request.GET:
            get_ifsc_code = request.GET['ifsc']
            flag=0
            try:
                limit = int(request.GET['limit'])
            except Exception as e:
                limit = None
            try:
                offset = int(request.GET['offset'])
            except Exception as e:
                offset = None
            if limit is None and offset is None:
                flag=1
            elif limit == 1 and offset is None:
                flag=1
            elif offset==0 and limit is None:
                flag=1
            elif limit == 1 and offset==0:
                flag=1
            try:
                branch_details = IndianBanksBranches.objects.get(ifsc=get_ifsc_code)
                if flag == 1:
                    bank_details = {
                        "Bank Name: ":branch_details.bank_name,
                        "Branch Name: ":branch_details.branch,
                        "Branch Address: ":branch_details.address,
                        "District: ":branch_details.district,
                        "City: ":branch_details.city,
                        "State: ":branch_details.state,
                        "IFSC CODE: ":branch_details.ifsc,
                    }
                else:
                    bank_details = {
                        "Code":2,
                        "Error":"Wrong_Limit_OR_Offset_Value"
                    }
                return JsonResponse(bank_details,json_dumps_params={'indent': 2})
            except Exception as e:
                logging.error("Exception Occured during IFSC = {}".format(get_ifsc_code),exc_info=True)
                data = {
                    'code':0,
                    'Error':'IFSC_Code_Not_Found',
                }
                return JsonResponse(data)
        elif 'bank_name' in request.GET and 'city' in request.GET:
            get_bank_name = request.GET['bank_name']
            get_city = request.GET['city']      
            try:
                limit = int(request.GET['limit'])
            except Exception as e:
                limit = None
            try:
                offset = int(request.GET['offset'])
            except Exception as e:
                offset = None

            try:
                branches = IndianBanksBranches.objects.filter(bank_name__icontains=get_bank_name,city__icontains=get_city)[offset:limit]
                branch_details = []
                for items in branches:
                    data = {
                        'IFSC Code: ': items.ifsc,
                        'Branch Name: ': items.branch,
                        'Branch Address: ':items.address,
                        "District: ":items.district,
                        "State: ":items.state,
                    }
                    branch_details.append(data)
                return JsonResponse({"Branches":branch_details},json_dumps_params={'indent': 2})
            except Exception as e:
                logging.error("Exception Occured during IFSC = {}".format(get_bank_name),exc_info=True)
                return HttpResponse("hi")
        else:
            return HttpResponse("hello")

class BranchList(APIView):
    def get(self,request):
        if 'ifsc' in request.GET:
            get_ifsc_code = request.GET['ifsc']
            flag=0
            try:
                limit = int(request.GET['limit'])
            except Exception as e:
                limit = None
            try:
                offset = int(request.GET['offset'])
            except Exception as e:
                offset = None
            if limit is None and offset is None:
                flag=1
            elif limit == 1 and offset is None:
                flag=1
            elif offset==0 and limit is None:
                flag=1
            elif limit == 1 and offset==0:
                flag=1
            
            try:
                branch_details = IndianBanksBranches.objects.get(ifsc=get_ifsc_code)
                serializer = bank_details_Serializer(branch_details)
                if flag==1:
                    return Response(serializer.data)
                else:
                    bank_details = {
                        "Code":2,
                        "Error":"Wrong_Limit_OR_Offset_Value"
                    }
                    return Response(bank_details)
            except Exception as e:
                logging.error("Exception Occured during IFSC = {}".format(get_ifsc_code),exc_info=True)
                data = {
                    'code':0,
                    'Error':'IFSC_Code_Not_Found',
                }
                return Response(data)
        
        elif 'bank_name' in request.GET and 'city' in request.GET:
            get_bank_name = request.GET['bank_name']
            get_city = request.GET['city']      
            try:
                limit = int(request.GET['limit'])
            except Exception as e:
                limit = None
            try:
                offset = int(request.GET['offset'])
            except Exception as e:
                offset = None

            try:
                branches = IndianBanksBranches.objects.filter(bank_name__icontains=get_bank_name,city__icontains=get_city)[offset:limit]
                serializer = branches_Serializer(branches,many=True)
                
                return Response(serializer.data)
            except Exception as e:
                logging.error("Exception Occured during BankName = {0} & city={1}".format(get_bank_name,get_city),exc_info=True)
                data = {
                    'code':0,
                    'Error':'Branches_Not_Found',
                }
                return Response(data)
        
        else:
            data = {
                    'code':0,
                    'Error':'Wrong_Query_Parameters',
                }
            return Response(data)

