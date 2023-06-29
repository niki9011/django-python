from django.shortcuts import render, redirect
from  .forms import PhotoAddForm, PhotoEditForm
from .models import Photo
from petstagram.photos.models import Photo


def photo_add(request):
    form = PhotoAddForm()

    if request.method == 'POST':
        form = PhotoAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'photos/photo-add-page.html', context=context)


def photo_details(request, pk):
    photo = Photo.objects.get(pk=pk)

    context = {
        "photo": photo,
        "likes": photo.like_set.count(),
        "comments": photo.comment_set.all(),
    }

    return render(request, 'photos/photo-details-page.html', context=context)


def photo_edit(request, pk):
    return render(request, 'photos/photo-edit-page.html')
