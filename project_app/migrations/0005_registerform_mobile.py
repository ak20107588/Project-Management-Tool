# Generated by Django 4.2.4 on 2023-11-07 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0004_projecttask_assignusername_projecttask_taskusername'),
    ]

    operations = [
        migrations.AddField(
            model_name='registerform',
            name='Mobile',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
    ]
