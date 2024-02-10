from django.db import models

# Create your models here.
class News(models.Model):
    news_title = models.CharField(max_length=255)
    news_date = models.DateField()
    news_author = models.CharField(max_length=100)
    news_category = models.CharField(max_length=100)
    news_description = models.TextField()
    news_image = models.ImageField(upload_to='news_images/')
    news_status = models.CharField(max_length=20)

    def __str__(self):
        return self.news_title