from django.db import models
from django.core.validators import MinLengthValidator
from petstagram.pets.models import Pet


class Photo(models.Model):
    # TODO: add validator
    pet_image = models.ImageField(blank=False, null=False)
    # optional
    description = models.TextField(
        max_length=300,
        validators=(MinLengthValidator(10),),
        blank=True, null=True
    )
    location = models.CharField(max_length=30)
    tagged_pets = models.ManyToManyField(Pet, blank=True, null=True)
    date_of_publications = models.DateField(auto_now=True)
