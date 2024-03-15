from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"),(1, "Published"))
CABIN_TYPE = ((0, "Coupe"),(1, "Cabrio"),(2, "Targa"))
User = get_user_model()

class Profile(models.Model):
    """
    Model file for User profile object
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name="user_profile")
    image = CloudinaryField('image')

    def __str__(self):
        return f"{self.user.username}'s profile"

class Category(models.Model):
    """
    Model for vehicle category object
    """
    title = models.CharField(max_length=50)
    category_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} created on {self.created_on}"

class Author(models.Model):
    """
    Model for Author object
    """
    user = models.OneToOneField(User,on_delete=models.CASCADE,
                                related_name='user_author')
    created_on = models.DateTimeField(auto_now_add=True)
    author_picture = CloudinaryField('image', default='placeholder')

    class Meta:
        verbose_name_plural = 'Authors'

    def __str__(self):
        return f"{self.user.username} created on {self.created_on}"

class Vehicle(models.Model):
    """
    Model for Vehicle objects
    """
    # Normally, according to normalization rules, the make
    # and model information should be stored in a separate
    # table. However, I am using it this way for now so 
    # that the project does not grow. 
    brand = models.CharField(max_length=20, blank=False)
    model = models.CharField(max_length=20, blank=False)
    cabin_type = models.IntegerField(choices = CABIN_TYPE, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                     related_name='category_vehicle')
    author = models.ForeignKey(Author, on_delete=models.CASCADE,
                               related_name='vehicle_author')
    title = models.CharField(max_length=200, unique=True, blank=False)
    slug = models.SlugField(max_length=200, unique=True, blank=False)
    summary = models.TextField()
    comment_count = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=False)
    featured_image = CloudinaryField('image',default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User,related_name='vehicle_like', blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]
        verbose_name_plural = 'Vehicles'

    def __str__(self):
        return f"Brand: {self.brand} model: {self.model} - created: {self.created_on}"
    
    def like_count(self):
        return self.likes.count()

class Comment(models.Model):
    """
    Model for Vehicle objects
    """
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE,
                                related_name="vehicle_comment")
    name = models.CharField(max_length = 100, blank=False)
    email = models.EmailField(blank=False)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Comments'
        ordering = ["-created_on"]

    def __str__(self):
        return f"Comment: {self.comment[:50]} by: {self.name}"

    class Meta:
        verbose_name_plural = 'Comments'
