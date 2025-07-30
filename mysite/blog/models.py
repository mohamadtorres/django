from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True) # Unique identifier for the post url
    author = models.ForeignKey(User, on_delete=models.CASCADE) # Link to the user who created the post, if the user removes their account, the post will be deleted
    body = models.TextField() # Main content of the post, text field for longer content
    created_date = models.DateTimeField(auto_now_add=True) #auto_now_add sets the field to now when the object is first created and cannot be changed
    status = models.CharField(max_length=10, choices=(('draft', 'Draft'), ('published', 'Published')), default='draft') # Status of the post, either draft or published

    def __str__(self):
        return self.title