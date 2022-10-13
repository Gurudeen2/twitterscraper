from django.db import models

class twttb(models.Model):
        username = models.CharField(max_length=100, blank=True)
        source = models.CharField(max_length=100, blank=True)
        url = models.CharField(max_length=100, blank=True)
        language = models.CharField(max_length=100, blank=True)
        content = models.TextField(blank=True)

        def __str__(self):
            return self.username
   


