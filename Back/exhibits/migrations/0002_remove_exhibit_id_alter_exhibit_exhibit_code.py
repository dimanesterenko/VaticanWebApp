# Generated by Django 5.0.1 on 2024-02-06 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibits', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exhibit',
            name='id',
        ),
        migrations.AlterField(
            model_name='exhibit',
            name='exhibit_code',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
