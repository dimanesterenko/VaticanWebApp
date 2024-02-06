from django.db import models

class Exhibit(models.Model):
    exhibit_code = models.IntegerField(primary_key=True)  # Код експонату
    inventory_number = models.CharField(max_length=50)  # Номер інвентарю
    title = models.CharField(max_length=100)
    creator_name = models.CharField(max_length=100)  # ПІБ твореця
    description = models.TextField()  # Опис
    creation_date = models.DateField()  # Дата створення
    material = models.CharField(max_length=100)  # Матеріал
    dimensions = models.CharField(max_length=100)  # Розміри
    acquisition_date = models.DateField()  # Дата придбання
    origin = models.CharField(max_length=100)  # Походження
    location = models.CharField(max_length=100)  # Розміщення
    photo = models.ImageField(upload_to='media/exhibit_photos/', null=True, blank=True)  # Фото експонату

    def __str__(self):
        return self.title