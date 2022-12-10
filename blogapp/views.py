from django.shortcuts import render
from .models import Post, Comment
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse

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



