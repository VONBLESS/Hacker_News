# Generated by Django 5.0.3 on 2024-03-25 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('all_posts', '0002_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]