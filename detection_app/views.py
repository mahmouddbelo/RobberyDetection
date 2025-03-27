from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .utils import predict_shoplifting
import os

def index(request):
    if request.method == 'POST' and request.FILES['video']:
        video_file = request.FILES['video']
        fs = FileSystemStorage()
        filename = fs.save(video_file.name, video_file)
        video_path = os.path.join(settings.MEDIA_ROOT, filename)
        
        # Make prediction
        result = predict_shoplifting(video_path)
        
        # Save the result in session to display on result page
        request.session['result'] = result
        request.session['video_filename'] = filename
        
        return redirect('result')
    
    return render(request, 'detection_app/index.html')

def result(request):
    result = request.session.get('result', {})
    video_filename = request.session.get('video_filename', '')
    
    context = {
        'result': result,
        'video_url': f'/media/{video_filename}'
    }
    return render(request, 'detection_app/result.html', context)