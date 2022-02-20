from operator import is_not
from django.shortcuts import render
from blog.forms import postForm
from blog.models import Post
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

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
                thumbnail = informacion['thumbnail'],
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

def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            user = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username = user, password = password)

            if user is not None:
                login (request, user)

                return render(request, 'blog/index.html')

            else: 

                return render(request, 'blog/index.html', {'mensaje': f'Datos incorrectos'})

        else:

            return render (request, 'blog/index.html', {'mensaje': f'Formulario erroneo'})

    form = AuthenticationForm()

    return render (request, 'blog/login.html', {'form':form})


def register(request):
    
    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']

            form.save()

            return render (request, 'blog/index.html', {'mensaje': 'Usuario creado!'})

    else:

        form = UserCreationForm()

    return render(request,'blog/signup.html', {'form':form})


        

