# Generated by Django 3.2.6 on 2021-08-24 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BreakTheStrategy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('college', models.CharField(default='', max_length=200)),
                ('branch', models.CharField(default=' ', max_length=50)),
                ('id1', models.FileField(upload_to='BreakTheStrategy/')),
            ],
        ),
        migrations.RemoveField(
            model_name='designathon',
            name='College',
        ),
        migrations.AddField(
            model_name='designathon',
            name='college',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='designathon',
            name='teamname',
            field=models.CharField(default=' ', max_length=200),
        ),
    ]
