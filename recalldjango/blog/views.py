from django.shortcuts import render
from .models import Blog
from django.http import HttpResponse
def get_user(req):
    name = Blog.objects.get(id=1)
    return HttpResponse(
        '''
        <h1>Hello</h1>
        ''' + str(name.id) + 
        name.name + 
        name.subject +
        name.body 
        
    )