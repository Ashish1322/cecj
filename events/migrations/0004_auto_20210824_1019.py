# Generated by Django 3.2.6 on 2021-08-24 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_collagemaking_electroinsight_projectdisplay_rangoli_technicalpresentationcse_technicalpresentationec'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TechnicalPresentationEce',
            new_name='TechnicalPresentation',
        ),
        migrations.DeleteModel(
            name='TechnicalPresentationCSE',
        ),
    ]