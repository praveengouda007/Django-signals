from .models import BlogPost
from django.utils.text import slugify
from django.dispatch import receiver
from django.utils import timezone
from django.db.models.signals import (
pre_save,
post_save,
pre_delete,
post_delete,
m2m_changed,
)
from asgiref.sync import sync_to_async
import asyncio


@receiver(pre_save, sender=BlogPost)
def blog_post_pre_save(sender, instance, *args, **kwargs):
    print(instance)
    if not instance.slug:
        instance.slug = slugify(instance.title)
        print(instance.slug)


@receiver(post_save, sender=BlogPost)

async def blog_post_post_save(sender, instance, created, *args, **kwargs):

    if created:
        print("notify users")
        instance.notify_users = True
        instance.save()

#Asynchronous
# blog_post_save = sync_to_async(blog_post_post_save, thread_sensitive=True)
# print(blog_post_save)


@receiver(pre_delete, sender=BlogPost)
def blog_post_pre_delete(sender, instance, *args, **kwargs):
    # move or make a backup of this data
    print(f"{instance.id} will be removed")

# pre_delete.connect(blog_post_pre_delete, sender=BlogPost)


@receiver(post_delete, sender=BlogPost)
def blog_post_post_delete(sender, instance, *args, **kwargs):

    print(f"{instance.id} has removed")

# post_delete.connect(blog_post_post_delete, sender=BlogPost)


@receiver(m2m_changed, sender=BlogPost.liked.through)
def blog_post_liked_changed(sender, instance, action, *args, **kwargs):
    # print(args, kwargs)
    # print(action)
    if action == 'pre_add':
        print('Was added')
        qs = kwargs.get("model").objects.filter(pk__in=kwargs.get('pk_set'))
        """instead of above line, we can also use this by adding arguments in function i.e., model,pk_Set"""
        # qs = model.objects.filter(pk__in='pk_set')
        print(qs.count())

