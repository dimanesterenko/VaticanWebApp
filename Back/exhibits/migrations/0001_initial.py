# Generated by Django 5.0.1 on 2024-02-06 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exhibit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exhibit_code', models.CharField(max_length=50)),
                ('inventory_number', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('creator_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('creation_date', models.DateField()),
                ('material', models.CharField(max_length=100)),
                ('dimensions', models.CharField(max_length=100)),
                ('acquisition_date', models.DateField()),
                ('origin', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='exhibit_photos/')),
            ],
        ),
    ]
