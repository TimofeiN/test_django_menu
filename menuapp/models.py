from django.db import models
from django.urls import reverse


class Menu(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')
    url = models.CharField(max_length=100, blank=True)
    named_url = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        if self.named_url:
            return reverse(self.named_url)
        else:
            return self.url

