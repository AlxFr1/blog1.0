# Generated by Django 4.0.1 on 2022-02-05 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_hillel', '0002_remove_comment_user_name_delete_userurl'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='post_id',
        ),
    ]