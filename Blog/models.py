from django.db import models



class Article(models.Model):
    titel=models.CharField(max_length=100)
    text=models.TextField()
    status=models.BooleanField()


    def __str__(self):

        return self.titel

