from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.

def insert_topic(request):

    TOT=TopicForm()
    d={'TOT':TOT}

    if request.method=='POST':
        TD=TopicForm(request.POST)
        if TD.is_valid():
            TD.save()
            return HttpResponse('topic data inserted')

    return render (request,'insert_topic.html',d)


def insert_webpage(request):

    WOT=WebpageForm()
    d={'WOT':WOT}
    if request.method=='POST':
        WD=WebpageForm(request.POST)
        if WD.is_valid():
            WD.save()
            return HttpResponse('webpage data inserted')

    

    return render (request,'insert_webpage.html',d)



def insert_AccessRecord(request):

    AOT=AccessRecordForm()
    d={'AOT':AOT}
    if request.method=='POST':
        AD=AccessRecordForm(request.POST)
        if AD.is_valid():
            AD.save()
            return HttpResponse('AccessRecord data inserted')

    

    return render (request,'insert_AccessRecord.html',d)