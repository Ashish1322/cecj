# Generated by Django 4.1 on 2022-09-09 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0048_surveyscout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyscout',
            name='id3',
            field=models.FileField(blank=True, null=True, upload_to='Surveyscout/'),
        ),
        migrations.AlterField(
            model_name='surveyscout',
            name='id4',
            field=models.FileField(blank=True, null=True, upload_to='Surveyscout/'),
        ),
        migrations.AlterField(
            model_name='surveyscout',
            name='id5',
            field=models.FileField(blank=True, null=True, upload_to='Surveyscout/'),
        ),
    ]
