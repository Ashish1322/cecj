# Generated by Django 4.1 on 2022-09-09 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0036_floatingconcreteboat_robolympics_techcharades_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groupdiscussion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_institution', models.CharField(choices=[('college', 'college'), ('school', 'school')], default='college', max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('college_school', models.CharField(default='', max_length=200)),
                ('branch_class', models.CharField(default=' ', max_length=50)),
                ('semester', models.IntegerField(blank=True, null=True)),
                ('roll_no', models.IntegerField(blank=True, null=True)),
                ('id1', models.FileField(upload_to='Groupdiscussion/')),
            ],
        ),
        migrations.CreateModel(
            name='Masterminds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_institution', models.CharField(choices=[('college', 'college'), ('school', 'school')], default='college', max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('college_school', models.CharField(default='', max_length=200)),
                ('branch_class', models.CharField(default=' ', max_length=50)),
                ('semester', models.IntegerField(blank=True, null=True)),
                ('roll_no', models.IntegerField(blank=True, null=True)),
                ('id1', models.FileField(upload_to='Masterminds/')),
            ],
        ),
        migrations.CreateModel(
            name='Mechrelay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_institution', models.CharField(choices=[('college', 'college'), ('school', 'school')], default='college', max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('college_school', models.CharField(default='', max_length=200)),
                ('branch_class', models.CharField(default=' ', max_length=50)),
                ('semester', models.IntegerField(blank=True, null=True)),
                ('roll_no', models.IntegerField(blank=True, null=True)),
                ('id1', models.FileField(upload_to='Mechrelay/')),
            ],
        ),
        migrations.CreateModel(
            name='Surveyscout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_institution', models.CharField(choices=[('college', 'college'), ('school', 'school')], default='college', max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('college_school', models.CharField(default='', max_length=200)),
                ('branch_class', models.CharField(default=' ', max_length=50)),
                ('semester', models.IntegerField(blank=True, null=True)),
                ('roll_no', models.IntegerField(blank=True, null=True)),
                ('id1', models.FileField(upload_to='Surveyscout/')),
            ],
        ),
        migrations.CreateModel(
            name='TechnicalquizCe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_institution', models.CharField(choices=[('college', 'college'), ('school', 'school')], default='college', max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('college_school', models.CharField(default='', max_length=200)),
                ('branch_class', models.CharField(default=' ', max_length=50)),
                ('semester', models.IntegerField(blank=True, null=True)),
                ('roll_no', models.IntegerField(blank=True, null=True)),
                ('id1', models.FileField(upload_to='TechnicalquizCe/')),
            ],
        ),
    ]