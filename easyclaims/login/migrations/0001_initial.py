# Generated by Django 2.1.5 on 2019-01-25 19:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('postcode', models.IntegerField()),
                ('dob', models.DateField()),
                ('created_at', models.DateField(default=datetime.datetime.now)),
            ],
        ),
    ]