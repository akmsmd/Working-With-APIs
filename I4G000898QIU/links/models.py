from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify


User = get_user_model()

class Link (models.Model):
    target_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(max_length=20, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.target_url

    def save(self, *args, **kwargs):  # new
        if not self.identifier:
            self.identifier = slugify(self.target_url)
        return super().save(*args, **kwargs)