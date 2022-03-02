from rest_framework import routers
from .views import BlogPostViewSet
from django.urls import path, include
from . import views


router = routers.DefaultRouter()
router.register('blog', views.BlogPostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

