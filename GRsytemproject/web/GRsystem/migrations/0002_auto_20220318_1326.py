# Generated by Django 3.2.10 on 2022-03-18 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GRsystem', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Branch',
            new_name='Department',
        ),
        migrations.AlterField(
            model_name='complaint',
            name='Type_of_complaint',
            field=models.CharField(choices=[('ClassRoom', 'ClassRoom'), ('Lecturer', 'Lecturer'), ('Management', 'Management'), ('College', 'College'), ('Other', 'Other')], max_length=200, null=True),
        ),
    ]
