from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
class Post(models.Model):
    image = CloudinaryField('image')
    image_name = models.CharField(max_length = 100)
    image_caption = models.TextField(max_length = 500)
    created = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    likes = models.IntegerField(null = True, default = 0)

    def __str__(self):
        return self.image_name

    def delete(self):
        self.delete()
        
