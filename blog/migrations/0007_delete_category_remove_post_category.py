# Generated by Django 4.1.1 on 2022-09-22 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
    ]
