from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import image
from myapp.forms import imageForm

# Create your views here.
def upload(request):
    if request.method =='POST':
        form= imageForm (request.POST,request.FILES)
        if form.is_valid ():
            form.save ()
    form=imageForm()
    images=image.objects.all()
    return render (request,'index.html',{'form':form , 'images':images })        
                