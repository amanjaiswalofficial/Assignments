from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import re
import os

# Create your views here.
#this and above import we do to avoid some problems while POST
@csrf_exempt
def function_one(request,filename):

    if re.match('^[^\s@%$*#\^][\w\d]*',filename) is not None:
        try:
            if request.method=='GET':
                if os.path.isfile(filename):
                    with open(filename,mode='r') as json_file:
                        data=json.load(json_file)
                    return JsonResponse(data)
                else:
                    raise FileNotFoundError

            elif request.method=='POST':
                json_data = json.loads(request.body)
                with open(filename,mode='w') as json_file:
                    json.dump(json_data,json_file)
                return HttpResponse('File created successfully')

            elif request.method == 'PUT':
                if os.path.isfile(filename):
                    json_data = json.loads(request.body)
                    with open(filename,mode='w') as json_file:
                        json.dump(json_data,json_file)
                    return HttpResponse('File updated successfully')
                else:
                    raise FileNotFoundError
                    
            elif request.method == 'DELETE':
                if os.path.isfile(filename):
                    os.remove(filename)
                    return HttpResponse('File deleted successfully')
                else:
                    raise FileNotFoundError
            else:
                return HttpResponse('Invalid request, try again')
        except FileNotFoundError:
            return HttpResponse('No such file exists')
    else:
        return HttpResponse('Invalid file name')