# Generated by Django 3.2.10 on 2022-04-22 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GRsystem', '0011_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='Type_of_complaint',
            field=models.CharField(choices=[('ClassRoom', 'ClassRoom'), ('Teacher', 'Teacher'), ('Management', 'Management'), ('College', 'College'), ('Other', 'Other')], max_length=200, null=True),
        ),
    ]
