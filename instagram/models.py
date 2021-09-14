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

class NewPost(models.Model):
    image = CloudinaryField('image')


class Comment(models.Model):
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    post = models.ForeignKey('Post', on_delete = models.CASCADE)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.post

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('image')
    bio = models.TextField(default='Bio', max_length=100)

    def __str__(self):
        return f'{self.user.username} Profile'