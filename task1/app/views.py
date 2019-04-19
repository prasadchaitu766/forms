from django.shortcuts import render
from .forms import *

def home(request):
    res=feedback
    return render(request,"feedback.html",{"res":res})


def SaveDetails(request):
    if request.method== "POST":
        form = feedback(request.POST)
        if form.is_valid():
                # process form data
                obj = Feedback_Form()  # gets new object
                obj.f_name = form.cleaned_data['f_name']
                obj.l_name = form.cleaned_data['l_name']
                obj.email = form.cleaned_data['email']
                obj.comment = form.cleaned_data['comment']
                # finally save the object in db
                obj.save()
    res=feedback

    return render(request,"feedback.html",{"message":"Saved","res":res})