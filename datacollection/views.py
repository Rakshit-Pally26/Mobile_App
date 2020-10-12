from django.db import models
from django.template.loader import get_template 
from dataapp.utils import render_to_pdf 
import requests
import io, os
from django.core.files.storage import FileSystemStorage
import sys
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Data

from django.shortcuts import render
def home(request):
    return render(request, 'index.html')

def data(request):
    return render(request, 'data.html')

def userdata(request):
    print("form is submitted")
    first_name= request.POST['first_name']
    last_name= request.POST['last_name']
    email= request.POST['email']
    location= request.POST['location']
    flood_depth= request.POST['flood_depth']
    latitude= request.POST['latitude']
    longitude = request.POST['longitude']
    time_stamp = request.POST['time_stamp']
    date = request.POST['date']
    additional_info= request.POST['additional_info']
    data = Data(first_name=first_name, last_name=last_name, email=email, additional_info=additional_info, location=location, flood_depth=flood_depth, date=date, time_stamp=time_stamp)
    data.save()
    template = get_template('pdf_template.html')
    context = {
        'FirstName' : first_name,
        'LastName' : last_name,
        'Email' : email,
        'Location' : location,
        'FloodDepth' : flood_depth,
        'Latitude' : latitude,
        'Longitude' : longitude,
        'TimeStamp' : time_stamp,
        'Date' : date,
        'AdditionalInfo' : additional_info,
    }
    html = template.render(context)
    pdf = render_to_pdf('pdf_template.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "User_%s.pdf" %("Details")
        content = "inline; filename='%s'" %(filename)
        download = request.GET.get("download")
        if download:
            content = "attachment; filename='%s'" %(filename)
        response['Content-Disposition'] = content
        return response
    return render(request, 'data.html')

def upload(request):
    context={}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs= FileSystemStorage()
        name= fs.save(uploaded_file.name, uploaded_file)
        context['url']= fs.url(name)
    return render(request, "data.html", context)

# Create your views here.
