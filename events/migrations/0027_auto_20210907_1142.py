# Generated by Django 3.1.5 on 2021-09-07 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0026_auto_20210906_0904'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aiworkshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('college_school', models.CharField(default='', max_length=200)),
                ('id1', models.FileField(upload_to='Aiworkshop/')),
            ],
        ),
        migrations.CreateModel(
            name='CECJHACKATHON',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_institution', models.CharField(choices=[('college', 'college'), ('school', 'school')], default='college', max_length=20)),
                ('college', models.CharField(default='', max_length=200)),
                ('teamname', models.CharField(default=' ', max_length=200)),
                ('name1', models.CharField(default=' ', max_length=20)),
                ('email1', models.EmailField(max_length=254)),
                ('phone1', models.CharField(default=' ', max_length=12)),
                ('branch1', models.CharField(default=' ', max_length=50)),
                ('semester1', models.CharField(blank=True, default=' ', max_length=3, null=True)),
                ('rollno1', models.CharField(blank=True, default=' ', max_length=20, null=True)),
                ('id1', models.FileField(upload_to='CECJHACKATHON/')),
                ('name2', models.CharField(default=' ', max_length=20)),
                ('email2', models.EmailField(max_length=254)),
                ('phone2', models.CharField(default=' ', max_length=12)),
                ('branch2', models.CharField(default=' ', max_length=50)),
                ('semester2', models.CharField(blank=True, default=' ', max_length=5, null=True)),
                ('rollno2', models.CharField(blank=True, default=' ', max_length=20, null=True)),
                ('id2', models.FileField(blank=True, null=True, upload_to='CECJHACKATHON/')),
            ],
        ),
        migrations.DeleteModel(
            name='Designathon',
        ),
    ]
