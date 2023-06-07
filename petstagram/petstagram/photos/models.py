from django.db import models
from django.core.validators import MinLengthValidator
from .validators import image_size_validator_5mb
from petstagram.pets.models import Pet


class Photo(models.Model):
    # TODO: add validator
    pet_image = models.ImageField(
        blank=False,
        null=False,
        validators=(image_size_validator_5mb, ),
        upload_to="mediafiles/photos",
    )
    # optional
    description = models.TextField(
        max_length=300,
        validators=(MinLengthValidator(10),),
        blank=True,
        null=True,
    )
    location = models.CharField(max_length=30, blank=True, null=False)
    tagged_pets = models.ManyToManyField(Pet, blank=True)
    date_of_publication = models.DateField(auto_now=True)
