from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    titulo = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    autor = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    actualizado = models.DateTimeField(auto_now= True)
    contenido = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-creado']

    def __str__(self):
        return self.titulo