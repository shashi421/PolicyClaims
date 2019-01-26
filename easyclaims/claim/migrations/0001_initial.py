# Generated by Django 2.1.5 on 2019-01-26 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('insurances', '0004_auto_20190126_1121'),
        ('login', '0004_auto_20190125_2040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('claim_name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('address', models.CharField(max_length=500)),
                ('typeOfClaim', models.CharField(choices=[('car', 'Car Claim'), ('home', 'Home Claim'), ('health', 'Health Claim')], default='', max_length=6)),
                ('details', models.CharField(max_length=500)),
                ('status', models.CharField(default='', max_length=500)),
                ('is_approved', models.BooleanField(default=False)),
                ('claim_created_time', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('claim_id', models.CharField(blank=True, max_length=120, primary_key=True, serialize=False)),
                ('policy_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insurances.Insurance')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.User')),
            ],
        ),
    ]