from django.contrib import admin
from .models import Post, Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):    #TO TWEAK OUR ADMIN INTERFACE BEFORE WE REGISTER OUR MODEL
    list_display = ('title', 'created_on')   
    search_fields = ['title', 'content']



#REGISTER OUR MODEL AND OUR CLASS
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)