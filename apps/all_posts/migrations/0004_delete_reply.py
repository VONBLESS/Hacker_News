# Generated by Django 5.0.3 on 2024-03-18 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('all_posts', '0003_reply'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Reply',
        ),
    ]