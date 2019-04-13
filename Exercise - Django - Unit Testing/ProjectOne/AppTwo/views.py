from django.shortcuts import render
from django.http import HttpResponse
from collections import defaultdict
import sys


def wish_user(request,input_num):
    if input_num in range(5,13):
        wish = 'Good Morning'
    elif 12 <= input_num<18:
        wish = 'Good Evening'
    elif 18 <= input_num<24:
        wish = 'Good Night'
    else:
        wish = 'Go To Bed'
    #return HttpResponse(wish)
    return wish


def multiply(a, b):
    return a * b
