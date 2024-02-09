# Generated by Django 5.0.1 on 2024-02-09 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Soubenir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('souvenir_code', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_available', models.BooleanField(default=False)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='products_photo/')),
            ],
        ),
    ]