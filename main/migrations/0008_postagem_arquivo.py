# Generated by Django 3.0.3 on 2020-04-21 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200228_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='postagem',
            name='arquivo',
            field=models.ImageField(blank=True, upload_to='static'),
        ),
    ]
