from django.db import models

# Create your models here

class CustomerFeedback(models.Model):
   
    name = models.CharField(max_length=100)
    message = models.TextField()
    rating = models.PositiveIntegerField(default=0)
    edited = models.BooleanField(default=False)

    def __str__(self):
        return self.name

