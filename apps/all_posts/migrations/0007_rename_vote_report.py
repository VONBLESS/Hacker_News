# Generated by Django 5.0.3 on 2024-03-20 12:01

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('all_posts', '0006_rename_flags_article_number_of_report_vote'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Vote',
            new_name='Report',
        ),
    ]