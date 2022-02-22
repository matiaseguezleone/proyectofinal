from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

# class User(AbstractUser):
#     pass

#     def __str__(self):
#         return self.username

class Post(models.Model):
    title = models.CharField(max_length=100)
    # content = models.TextField()
    content = RichTextField(blank = True, null = True)
    slug = models.SlugField(max_length=200, null = True, unique=True)
    thumbnail = models.ImageField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post-details', kwargs={'slug': self.slug})

class Comment(models.Model):
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    # def __str__(self):
    #     return self.user.username
class Likes(models.Model):
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.user.username
    