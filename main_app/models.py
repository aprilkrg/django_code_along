from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    premiere_date = models.DateField(auto_now=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shows', default=None)
    
    class Rating(models.IntegerChoices):
        LIKE_IT = 1
        LOVE_IT = 2
        GOTTA_HAVE_IT = 3
    review = models.IntegerField(choices=Rating.choices)

    def __str__(self):
        return self.title  