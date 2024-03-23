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
    overview = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title}"

class VehicleBrand(models.Model):
    """
    Brand of Vehicle objects
    """
    brand = models.CharField(max_length=35, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Brands'

    def __str__(self):
        return f"Brand: {self.brand}"

class VehicleModel(models.Model):
    """
    Model of vehicle objects
    """
    model = models.CharField(max_length=35, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    brand = models.ForeignKey(VehicleBrand, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Models'

    def __str__(self):
       return f"Model: {self.model}"

class Vehicle(models.Model):
    """
    Model for Vehicle objects
    """
    brand = models.ForeignKey(VehicleBrand, on_delete=models.CASCADE)
    model = models.ForeignKey(VehicleModel, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                     related_name='category_vehicle')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='vehicle_user')
    title = models.CharField(max_length=200, unique=True, blank=False)
    cc = models.CharField(max_length=5, unique=False, blank=False, default='10')
    motor_type = models.CharField(max_length=20, unique=False, blank=False, default='Boxer')
    hp = models.CharField(max_length=5, unique=False, blank=False, default='10')
    slug = models.SlugField(max_length=200, unique=True, blank=False)
    summary = models.TextField(blank=True)
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
        return f"Brand: {self.brand.brand} model: {self.model.model}"
    
    def like_count(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('vehicle_detail', kwargs={
            'id': self.id
        })

class Comment(models.Model):
    """
    Model for Vehicle objects
    """
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="vehicle_comments")
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Comments'
        ordering = ["-created_on"]

    def __str__(self):
        return f"Comment: {self.comment[:50]} by: {self.name}"

class Author(models.Model):
   """
   Model for Author object
   """
   user = models.OneToOneField(User,on_delete=models.CASCADE,
                               related_name='user_author')
   created_on = models.DateTimeField(auto_now_add=True)
   author_picture = CloudinaryField('image', default='placeholder')#

   class Meta:
       verbose_name_plural = 'Authors'

   def __str__(self):
       return f"{self.user.username} created on {self.created_on}"