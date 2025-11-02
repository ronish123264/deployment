from django.shortcuts import render
from rest_framework import generics
from posts.models import Post
from .serializers import PostSerializer
from rest_framework.response  import Response
# Create your views here.



class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

    def delete (self, request, *args, **kwargs):
        Post.objects.all().delete()
        return Response(status= 204)
   

class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'

