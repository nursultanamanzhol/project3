# Generated by Django 4.0.2 on 2022-05-03 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_alter_registration_options_posts_url_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='url',
        ),
    ]
