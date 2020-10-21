from django.db import models


class TimespamtedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Post(TimespamtedModel):
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title
