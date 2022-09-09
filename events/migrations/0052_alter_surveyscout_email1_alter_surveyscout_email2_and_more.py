# Generated by Django 4.1 on 2022-09-09 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0051_bplan_branch2_bplan_email2_bplan_id2_bplan_name2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyscout',
            name='email1',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='surveyscout',
            name='email2',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='surveyscout',
            name='id1',
            field=models.FileField(upload_to='Surveyscout/'),
        ),
        migrations.AlterField(
            model_name='surveyscout',
            name='id2',
            field=models.FileField(blank=True, null=True, upload_to='Surveyscout/'),
        ),
    ]