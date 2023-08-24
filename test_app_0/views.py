from django.shortcuts import render

from pymongo import MongoClient
from django.db import connection

client = MongoClient(connection.settings_dict['CLIENT']['host'])
db_name = connection.settings_dict['NAME']
connect_to_db = client[db_name]

def login_page(request):
    data_dict = {"title": "Login"}
    return render(request, 'base.html', data_dict)
