from django.db import models
from django.contrib.auth.models import User         #CLASS FOR USERS WITHIN DJANGO AUTH SYSTEM
from django.db.models.deletion import SET_NULL

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(default="slug")     
    author = models.ForeignKey(User, on_delete=SET_NULL, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)        #On modification date will be updated
    content = models.TextField()
    image = models.ImageField(upload_to="img", default="")
    trending = models.BooleanField(default = False)


class Meta:     #METADATA TO TELL DJANGO WHERE TO SORT DATA
    arrangememt = ['-created_on']   #TO MAKE POST IN A DESCENDING ORDER BY POST DATE


def __str__(self):      #Dunder method(to identify posts by title)
    return self.title
    

#FOR COMMENT FUNCTIONALITY
class Comment(models.Model): 
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  #POST HAS COMMENTS, HENCE WHEN WE DELETE A CERTAIN POST. ITS COMMENTS ALSO DELETES
    body = models.TextField()
    #author_name = models.CharField(max_length = 100)

    def __str__(self):
        return self.body
