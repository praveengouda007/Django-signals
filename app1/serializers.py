from .models import *
from rest_framework import serializers

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'slug', 'liked', 'notify_users']