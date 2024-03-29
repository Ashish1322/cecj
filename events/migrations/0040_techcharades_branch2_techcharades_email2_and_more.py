# Generated by Django 4.1 on 2022-09-09 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0039_robolympics_eventype'),
    ]

    operations = [
        migrations.AddField(
            model_name='techcharades',
            name='branch2',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='techcharades',
            name='email2',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='techcharades',
            name='id2',
            field=models.FileField(blank=True, null=True, upload_to='Techcharades/'),
        ),
        migrations.AddField(
            model_name='techcharades',
            name='name2',
            field=models.CharField(default=' ', max_length=20),
        ),
        migrations.AddField(
            model_name='techcharades',
            name='phone2',
            field=models.CharField(default=' ', max_length=12),
        ),
        migrations.AddField(
            model_name='techcharades',
            name='rollno2',
            field=models.CharField(blank=True, default=' ', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='techcharades',
            name='semester2',
            field=models.CharField(blank=True, default=' ', max_length=5, null=True),
        ),
    ]
