# Generated by Django 3.0.3 on 2020-04-21 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20200421_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postagem',
            name='arquivo',
            field=models.ImageField(blank=True, upload_to='static/media'),
        ),
    ]
