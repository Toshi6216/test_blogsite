# Generated by Django 3.2.15 on 2022-09-26 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='nickname',
            field=models.CharField(default='other', max_length=200, verbose_name='ニックネーム'),
        ),
    ]