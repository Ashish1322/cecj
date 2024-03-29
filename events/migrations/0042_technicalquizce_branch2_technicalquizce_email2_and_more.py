# Generated by Django 4.1 on 2022-09-09 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0041_techcharades_teamname'),
    ]

    operations = [
        migrations.AddField(
            model_name='technicalquizce',
            name='branch2',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='technicalquizce',
            name='email2',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='technicalquizce',
            name='id2',
            field=models.FileField(blank=True, null=True, upload_to='TechnicalquizCe/'),
        ),
        migrations.AddField(
            model_name='technicalquizce',
            name='name2',
            field=models.CharField(default=' ', max_length=20),
        ),
        migrations.AddField(
            model_name='technicalquizce',
            name='phone2',
            field=models.CharField(default=' ', max_length=12),
        ),
        migrations.AddField(
            model_name='technicalquizce',
            name='rollno2',
            field=models.CharField(blank=True, default=' ', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='technicalquizce',
            name='semester2',
            field=models.CharField(blank=True, default=' ', max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='technicalquizce',
            name='teamname',
            field=models.CharField(default='', max_length=50),
        ),
    ]
