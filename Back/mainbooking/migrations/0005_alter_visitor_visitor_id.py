# Generated by Django 5.0.1 on 2024-02-11 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainbooking', '0004_alter_booking_booking_id_alter_guide_guide_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='Visitor_ID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
