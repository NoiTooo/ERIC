# Generated by Django 3.1.6 on 2021-02-13 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_auto_20210212_0252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='default.png', upload_to='media/profile_pics'),
        ),
    ]
