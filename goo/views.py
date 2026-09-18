from django.shortcuts import render
from django.views import View
from .models import Post
from django.http import HttpResponse
# Create your views here.



class PostListView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'post_list.html', {'posts': posts})
    

