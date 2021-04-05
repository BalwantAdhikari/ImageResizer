from django.shortcuts import render
from django.http import HttpResponse
from .models import Images, ResizedImages
from PIL import Image
from datetime import datetime
from os import path
import sys
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

def index_view(request):
    if request.method == 'POST':
        f = request.FILES['fileImage']
        pImage = Image.open(f)
        (width, height) = pImage.size
        salt = datetime.now().strftime("%d%b%y%H%M%S")
        fname, fext = path.splitext(f.name)
        img = Images(image_name=fname+salt+fext, image_width=width, image_height=height, image=f)
        img.save()

        origImg = Images.objects.get(image_name=fname+salt+fext)

        data = {
            'image_name': origImg.image_name,
            'image_width': width,
            'image_height': height,
            'image': origImg.image
            }
        return render(request, 'resizerApp/index.html', {'data': data})
    
    return render(request, 'resizerApp/index.html')

def resized_view(request):
    if request.method == 'POST':
        imageName = request.POST['imageName']
        width = request.POST['width']
        height = request.POST['height']
        image = request.POST['image']

        imageN, imageE = path.splitext(image)

        pImage = Image.open('images/{}'.format(image))

        output = BytesIO()

        pImageResized = pImage.resize((int(width),int(height)))
        pImageResized.save(output, format='PNG', quality=100)
        output.seek(0)
        resizedImage = InMemoryUploadedFile(output,'ImageField', imageN+imageE, 'image/{}'.format(imageE[1:]), sys.getsizeof(output), None)
		
        # check if the image already exist in the database
        imageCount = ResizedImages.objects.filter(image_name=imageName).count()
        if imageCount > 0:
            return render(request, 'resizerApp/resize.html')

        img = ResizedImages(image_name=imageName, image_width=width, image_height=height, image=resizedImage)
        img.save()

        finalImage = ResizedImages.objects.get(image_name=imageName)

        data = {
            'image_name': finalImage.image_name,
            'image_width': width,
            'image_height': height,
            'image': finalImage.image
            }

        return render(request, 'resizerApp/resize.html', {'data': data})

    return render(request, 'resizerApp/resize.html')