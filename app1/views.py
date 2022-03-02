from rest_framework import viewsets
from .serializers import BlogPostSerializer
from .models import BlogPost

class BlogPostViewSet(viewsets.ModelViewSet):
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.all()
