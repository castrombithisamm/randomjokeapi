from django.db import models

class DryJoke(models.Model):
    joke = models.CharField(max_length=1000)
    author = models.CharField(max_length=50)
    


    def __str__(self):
        return self.joke + ' ' + self.author
