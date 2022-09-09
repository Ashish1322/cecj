# Generated by Django 4.1 on 2022-09-09 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0047_delete_surveyscout'),
    ]

    operations = [
        migrations.CreateModel(
            name='Surveyscout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectname', models.CharField(default=' ', max_length=100)),
                ('name3', models.CharField(default=' ', max_length=20)),
                ('email3', models.EmailField(default='', max_length=254)),
                ('phone3', models.CharField(default=' ', max_length=12)),
                ('branch3', models.CharField(default=' ', max_length=50)),
                ('semester3', models.CharField(blank=True, default=' ', max_length=5, null=True)),
                ('rollno3', models.CharField(blank=True, default=' ', max_length=20, null=True)),
                ('id3', models.FileField(blank=True, null=True, upload_to='ProjectDisplay/')),
                ('name4', models.CharField(default=' ', max_length=20)),
                ('email4', models.EmailField(default='', max_length=254)),
                ('phone4', models.CharField(default=' ', max_length=12)),
                ('branch4', models.CharField(default=' ', max_length=50)),
                ('semester4', models.CharField(blank=True, default=' ', max_length=5, null=True)),
                ('rollno4', models.CharField(blank=True, default=' ', max_length=20, null=True)),
                ('id4', models.FileField(blank=True, null=True, upload_to='ProjectDisplay/')),
                ('name5', models.CharField(default=' ', max_length=20)),
                ('email5', models.EmailField(default='', max_length=254)),
                ('phone5', models.CharField(default=' ', max_length=12)),
                ('branch5', models.CharField(default=' ', max_length=50)),
                ('semester5', models.CharField(blank=True, default=' ', max_length=5, null=True)),
                ('rollno5', models.CharField(blank=True, default=' ', max_length=20, null=True)),
                ('id5', models.FileField(blank=True, null=True, upload_to='ProjectDisplay/')),
                ('type_institution', models.CharField(choices=[('college', 'college'), ('school', 'school')], default='college', max_length=20)),
                ('college', models.CharField(default='', max_length=200)),
                ('teamname', models.CharField(default=' ', max_length=200)),
                ('name1', models.CharField(default=' ', max_length=20)),
                ('email1', models.EmailField(max_length=254)),
                ('phone1', models.CharField(default=' ', max_length=12)),
                ('branch1', models.CharField(default=' ', max_length=50)),
                ('semester1', models.CharField(blank=True, default=' ', max_length=3, null=True)),
                ('rollno1', models.CharField(blank=True, default=' ', max_length=20, null=True)),
                ('id1', models.FileField(upload_to='Rangoli/')),
                ('name2', models.CharField(default=' ', max_length=20)),
                ('email2', models.EmailField(max_length=254)),
                ('phone2', models.CharField(default=' ', max_length=12)),
                ('branch2', models.CharField(default=' ', max_length=50)),
                ('semester2', models.CharField(blank=True, default=' ', max_length=5, null=True)),
                ('rollno2', models.CharField(blank=True, default=' ', max_length=20, null=True)),
                ('id2', models.FileField(blank=True, null=True, upload_to='Rangoli/')),
            ],
        ),
    ]