# Generated by Django 3.1.5 on 2021-09-06 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0025_auto_20210906_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cgccodathon',
            name='id1',
            field=models.FileField(upload_to='CGCCODATHON/'),
        ),
    ]
