from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify

# signals imports
from django.dispatch import receiver
from django.db.models.signals import (
pre_save,
post_save,
pre_delete,
post_delete,
m2m_changed,
)


User = settings.AUTH_USER_MODEL

@receiver(pre_save, sender=User)
def user_pre_save_receiver(sender, instance, *args, **kwargs):
    """
     before saved in the database
     """
    print(instance.username, instance.id)
# pre_save.connect(user_pre_save_receiver, sender=User)


@receiver(post_save, sender=User)
def user_post_save_receiver(sender, instance, created, *args, **kwargs):
    """
     after saved in the database
     """
    if created:
        print("send email to", instance.username)
        # trigger pre_save
        # instance.save()
        # trigger post_save
    else:
        print(instance.username, "was just saved")
# post_save.connect(user_post_save_receiver, sender = User)


class BlogPost(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, null=True)
    liked = models.ManyToManyField(User, blank=True)
    notify_users = models.BooleanField(default=False)
    notify_users_timestamp = models.DateTimeField(blank=True, null=True, auto_now_add=False)
    active = models.BooleanField(default=True)


