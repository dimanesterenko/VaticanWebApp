# Generated by Django 5.0.1 on 2024-02-11 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainbooking', '0005_alter_visitor_visitor_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='Visitor_ID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
