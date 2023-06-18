from django.shortcuts import render, redirect
from petstagram.pets.models import Pet
from petstagram.pets.forms import PetAddForm, PetEditForm, PedDeleteForm


def pet_add(request):
    form = PetAddForm()

    if request.method == 'POST':
        form = PetAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile details', pk=1)

    context = {
        "form": form,
    }

    return render(request, 'pets/pet-add-page.html', context=context)


def pet_details(request, username, pet_name):
    pet = Pet.objects.filter(slug=pet_name).first()
    all_photos = pet.photo_set.all()

    context = {
        "pet": pet,
        "all_photos": all_photos,
    }
    return render(request, 'pets/pet-details-page.html', context=context)


def pet_edit(request, username, pet_name):
    pet = Pet.objects.filter(slug=pet_name).first()
    form = PetEditForm(instance=pet)

    if request.method == "POST":
        form = PetEditForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()

            return redirect('pet details', username=username, pet_name=pet_name)

    context = {
        "form": form,
        "username": username,
        "pet_name": pet_name
    }

    return render(request, 'pets/pet-edit-page.html', context=context)


def pet_delete(request, username, pet_name):
    pet = Pet.objects.filter(slug=pet_name).first()
    form = PedDeleteForm

    if request.method == "POST":
        if form.is_valid(request.POST, instance=pet):
            pet.delete()

        return redirect('profile details', pk=1)

    context = {
        "form": form,
        "username": username,
        "pet_name": pet_name,
    }

    return render(request, 'pets/pet-delete-page.html', context=context)
