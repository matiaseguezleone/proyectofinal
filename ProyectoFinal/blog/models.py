from django.db import models
from django.contrib.auth.models import User

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
    content = models.TextField()
    thumbnail = models.ImageField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    # def __str__(self):
    #     return self.user.username

# class PostView (models.Model):
#     # user = models.ForeignKey(User, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     time = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.user.username
class Likes(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.user.username
    