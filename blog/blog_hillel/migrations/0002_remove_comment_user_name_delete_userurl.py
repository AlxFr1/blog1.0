# Generated by Django 4.0.1 on 2022-02-05 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_hillel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user_name',
        ),
        migrations.DeleteModel(
            name='UserUrl',
        ),
    ]