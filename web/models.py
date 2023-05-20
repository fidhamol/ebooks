from django.db import models
from django.contrib.auth.models import User

LANG_CHOICE=(
        ('eng','English'),
        ('mal','Malayalam'),
        ('ara','Arabic'),
    )

class Book(models.Model):
    language = models.CharField(max_length=3,choices=LANG_CHOICE)
    year=models.IntegerField()
    name = models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    price=models.FloatField()
    image=models.ImageField(upload_to='Books_image')
    description=models.TextField()
    pdf=models.FileField(upload_to='Book/')

    def __str__(self):
        return self.name

class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)