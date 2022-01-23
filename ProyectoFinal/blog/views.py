from django.shortcuts import render
from blog.forms import postForm
from blog.models import Post
from django.views.generic import ListView, DetailView

# Create your views here.

class Inicio (ListView):
    model = Post
    template_name = 'blog/index.html'

class postDetails(DetailView):
    model = Post
    template_name = 'blog/post_details.html'

def about(request):
    return render(request, 'blog/about.html')

def creaPost(request):
    
    if request.method == 'POST':
        
        formularioPost = postForm(request.POST)

        print(formularioPost)

        if formularioPost.is_valid:
            
            informacion = formularioPost.cleaned_data

            post = Post (
                title = informacion['title'],
                content = informacion['content'],
                # thumbnail = informacion['thumbnail'],
                # created_date = datetime.now

            )
            
            post.save()

            return render(request, 'blog/index.html')

    else:

        formularioPost = postForm()

    return render(request, 'blog/creapost.html', {'formularioPost':formularioPost})

def buscarPost(request):

    return render(request, 'blog/buscarPost.html')

def buscar(request):

    if request.method == 'POST':

        searched = request.POST['searched']
        posts = Post.objects.filter(title__contains=searched)

        return render(request, 'blog/resultadoBuscar.html', {'searched':searched, 'posts':posts})

    else:

        return render(request, 'blog/resultadoBuscar.html', {})

