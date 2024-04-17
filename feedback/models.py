from django.db import models



class Feedback(models.Model):
    text = models.CharField(max_length=30)
    rating = models.IntegerField(default=0)# оценка
    image = models.ImageField(upload_to='feedback_images/', blank=True, null=True)
    # фото
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)