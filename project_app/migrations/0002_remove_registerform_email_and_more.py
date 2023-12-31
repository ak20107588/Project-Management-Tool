# Generated by Django 4.2.4 on 2023-11-06 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registerform',
            name='email',
        ),
        migrations.RemoveField(
            model_name='registerform',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='registerform',
            name='last_name',
        ),
        migrations.AddField(
            model_name='registerform',
            name='Confirm_Password',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registerform',
            name='Password',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registerform',
            name='Email',
            field=models.EmailField(default=1, max_length=254, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registerform',
            name='First_Name',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registerform',
            name='Last_Name',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
