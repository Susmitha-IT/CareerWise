# Generated by Django 5.0.2 on 2024-02-28 15:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('quiz', '0003_delete_userscore'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserScore',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
    ]
