# Generated by Django 3.2.6 on 2021-08-30 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_bar_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='bar',
            name='errored',
            field=models.BooleanField(default=False),
        ),
    ]
