# Generated by Django 4.0.4 on 2022-06-16 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='fine',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
