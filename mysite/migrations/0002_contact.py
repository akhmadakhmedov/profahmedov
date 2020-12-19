# Generated by Django 3.1.3 on 2020-12-09 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name_Surname', models.CharField(max_length=30)),
                ('Phone_number', models.IntegerField()),
                ('Subject', models.CharField(max_length=30)),
                ('Message', models.TextField()),
            ],
        ),
    ]