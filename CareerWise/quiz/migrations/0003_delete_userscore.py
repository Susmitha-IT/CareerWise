# Generated by Django 5.0.2 on 2024-02-28 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_userscore'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserScore',
        ),
    ]
