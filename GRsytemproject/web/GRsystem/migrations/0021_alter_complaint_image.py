# Generated by Django 3.2.10 on 2022-04-24 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GRsystem', '0020_alter_complaint_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
