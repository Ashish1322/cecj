# Generated by Django 4.1 on 2022-09-09 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0046_remove_technicalcollage_projectname'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Surveyscout',
        ),
    ]