from django.db import models

from news.models.common import BaseModel

# Create your models here.
class Sample(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Sample2(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Sample3(BaseModel):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title