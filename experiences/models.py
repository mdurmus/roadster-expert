from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.validators import MaxLengthValidator, MinLengthValidator
from cloudinary.models import CloudinaryField
User = get_user_model()


class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.CharField(
        max_length=20,
        validators=[MaxLengthValidator(20), MinLengthValidator(1)],
        blank=False
    )

    model = models.CharField(
        max_length=40,
        validators=[
            MaxLengthValidator(40),
            MinLengthValidator(1)
        ],
        blank=False
    )

    title = models.CharField(
        max_length=50,
        validators=[
            MaxLengthValidator(50),
            MinLengthValidator(5)
        ],
        blank=False
    )

    summary = models.CharField(
        blank=False,
        max_length=500,
        validators=[MaxLengthValidator(500)]
    )

    content = models.TextField(blank=False)

    max_speed = models.CharField(max_length=5, default='900')

    featured_image = CloudinaryField('image', default='placeholder')

    created_on = models.DateTimeField(auto_now_add=True)

    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]
        verbose_name_plural = 'My Experiences'

    def __str__(self):
        return f"Brand: {self.brand} model: {self.model}"

    def get_absolute_url(self):
        return reverse('my-experience', kwargs={
            'id': self.id
        })
