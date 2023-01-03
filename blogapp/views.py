from django.shortcuts import render, redirect
from . models import Post, Comment
from .forms import CommentForm,UserRegisterForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.utils.safestring import mark_safe
from django.views.generic import DeleteView


# Create your views here.
def index(request):
    trending = Post.objects.get(trending=True)  #GET THE POST THATS MARKED AS TRENDING ON DB
    posts = Post.objects.filter(trending=False)
    context = {
        "trending":trending,
        "posts":posts
    }
    return render(request, 'index.html', context)


def readmore(request, slug):
    post = Post.objects.get(slug = slug)    
    comments = post.comment_set.all()       #TO GET ALL COMMENTS FROM A SPECIFIC BLOG POST
    form = CommentForm()  #GET "COMMENTFORM" FROM THE FRONTEND THROUGH A POST HTTP METHOD
    new_comment =  None
    if request.method == 'POST':  
        form = CommentForm(request.POST)    #THE COMMENT GOTTEN FROM FRONTEND THROUGH A POST METHOD
        if form.is_valid():
            new_comment = form.save(commit = False)   #SET IT AS "NEWCOMMENT" FROM FRONTEND AND  BEFORE WE SAVE IT
            new_comment.post = post  #WE SET THE COMMENT TO THE APPROPRIATE BLOG POST
            new_comment.save()
            return HttpResponseRedirect(reverse('readmore', kwargs={'slug' : slug}))
    context = {
        "post":post,
        "comments":comments,
        "form":form,
    }
    return render(request, "article.html", context)    


def about(request):
    return render(request, 'about.html')    


def others(request):
    return render(request, "others.html")      

      

def register_view(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hey {username}, Your account was successfully created")
            new_user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1'])                     
            login(request, new_user)
            return redirect("home")                        
    else:
        form = UserRegisterForm()

    context = {
        'form':form
    }      
    return render(request, "registration/signup.html", context)



def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request, f"Hey you are already logged in as {request.user}.")
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "You are logged in")
                return redirect("home")  
            else:
                messages.warning(request, f"User does not exist, create an account.")
        except:
            messages.warning(request, "Could not authenticate, check credentials")             
    return render(request, "registration/login.html")    



def logout_view(request):
    logout(request)
    messages.success(request, "You logged out.")
    return redirect("home")

   

def get_mail(request):
    if request.method == "POST":
        email = request.POST.get("mail")
        email.save(commit=False)
        messages.success(request, "Email received successfully")
        return redirect("stories")
    return render(request, "others.html")      
    