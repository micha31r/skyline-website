# Generated by Django 3.1.7 on 2021-04-21 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermgmt', '0003_auto_20210321_0222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=models.SlugField(blank=True, max_length=64, null=True, unique=True),
        ),
    ]
