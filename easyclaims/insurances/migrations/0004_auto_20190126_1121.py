# Generated by Django 2.1.5 on 2019-01-26 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurances', '0003_auto_20190126_1119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='insurance',
            name='id',
        ),
        migrations.AlterField(
            model_name='insurance',
            name='insurance_policy_id',
            field=models.CharField(blank=True, max_length=120, primary_key=True, serialize=False),
        ),
    ]