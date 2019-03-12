from django.shortcuts import render
from django.http import HttpResponse
from collections import defaultdict
import sys

# Create your views here.
def wish_user(request,input_num):
    if 5<=input_num<12:
        wish='Good Morning'
    elif 12<=input_num<18:
        wish='Good Evening'
    elif 18<=input_num<24:
        wish='Good Night'
    else:
        wish='Go To Bed'
    return HttpResponse(wish)