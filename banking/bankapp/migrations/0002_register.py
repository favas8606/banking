# Generated by Django 3.1.8 on 2023-11-03 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('zip', models.IntegerField(max_length=6)),
                ('district', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('age', models.IntegerField(max_length=10)),
                ('gender', models.CharField(max_length=20)),
                ('phone', models.IntegerField(max_length=10)),
                ('email', models.CharField(max_length=30)),
                ('type_ac', models.CharField(max_length=30)),
                ('details', models.CharField(max_length=30)),
            ],
        ),
    ]
