# Generated by Django 3.2.10 on 2022-04-01 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GRsystem', '0008_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Image',
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]