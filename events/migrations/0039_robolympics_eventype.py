# Generated by Django 4.1 on 2022-09-09 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0038_bplan'),
    ]

    operations = [
        migrations.AddField(
            model_name='robolympics',
            name='eventype',
            field=models.CharField(default='', max_length=200),
        ),
    ]
