# Generated by Django 2.2 on 2019-06-15 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190614_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', null=True, upload_to='profile_pics/'),
        ),
    ]
