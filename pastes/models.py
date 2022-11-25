from django.db import models
from django.apps import apps
from random import SystemRandom
from django.urls import reverse
from django.utils import timezone

config = apps.get_app_config("pastes")

def generate_keys(length, key_type):
    if key_type == "secret":
        key = "".join([SystemRandom().choice(config.SECRET_KEY_CHOICES) for i in range(length)])
        try:
            Paste.objects.get(secret_key=key)
        except Paste.DoesNotExist:
            return key
        return generate_key(length=length + 1,key_type="secret")
    if key_type == "user":
        key = "".join([SystemRandom().choice(config.USER_KEY_CHOICES) for i in range(length)])
        return key


class Paste(models.Model):
    secret_key = models.CharField(max_length=255, unique=True, null=True, blank=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    lang = models.CharField(max_length=30)
    created_on = models.DateTimeField(auto_now_add=True)
    expired_on = models.DateTimeField(null=True, blank=True)
    view_count = models.PositiveIntegerField(default=0, null=True, blank=True)
    user_key = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.title

    def is_expired(self):
        if self.expired_on == None:
            return False
        current_datetime = timezone.now()
        if self.expired_on < current_datetime:
            return True
        else:
            return False

    def save(self, session, *args, **kwargs):
        if not self.secret_key:
            self.secret_key = generate_keys(length=config.SECRET_KEY_LENGTH, key_type="secret")
        if not self.user_key:
            try:
                self.user_key = session["user_key"]
            except KeyError:
                key = generate_keys(length=config.USER_KEY_LENGTH, key_type="user")
                self.user_key = key
                session["user_key"] = key
            
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('pastedetail', kwargs={'slug_key' : self.secret_key})
    
    def get_absolute_raw_url(self):
        return reverse('paste_raw_view', kwargs={'slug_key' : self.secret_key})
