# Generated by Django 3.0.3 on 2020-06-28 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20200607_2301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='postagem',
            new_name='post',
        ),
    ]
