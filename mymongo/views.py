import json
from django.shortcuts import render
import os
from django.utils import timezone
from .models import photomodel
from django.http import StreamingHttpResponse, FileResponse
from django.shortcuts import HttpResponse
from django.conf import settings
# Create your views here.

def uploadimage(request):
    if request.method == 'POST':
        image_name = request.POST.get('imagename')+'.jpg'
        t1 = timezone.localtime()
        t2 =t1.strftime("%Y-%m-%d %H:%M:%S")
        files = request.FILES
        content = files.get('image', None)
        size = content.size/1000
        photomodel.objects.create(name=image_name, created_at=t2, size=str(size)+'kB')
        content = content.read()
        path = os.path.join(settings.MEDIA_ROOT,image_name,)
        with open(path,'wb') as f:
            f.write(content)
        return HttpResponse('upload success')
        pass
def downloadimage(request):
    if request.method == 'POST':
        global filename
        filename = request.POST.get('downloadname')+'.jpg'
        result = photomodel.objects.filter(name=filename)
        return  HttpResponse(None)
    if request.method == 'GET':
        filepath = os.path.join(settings.MEDIA_ROOT,filename)
        fp = open(filepath, 'rb')
        #response = StreamingHttpResponse(fp)
        response = FileResponse(fp)
        response['Content-Type'] = 'application/x-jpg'
        response['Content-Disposition'] = 'attachment;filename="%s"' % filename
        return response
        fp.close()
        pass
def gainalbum(request):
    if request.method == 'POST':
        photolist = []
        for i in photomodel.objects.all():
            photolist = photolist+[i.name]+[' ']
            print(photolist)
        response = HttpResponse(photolist)
        return response
