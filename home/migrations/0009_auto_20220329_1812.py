# Generated by Django 3.2.5 on 2022-03-29 12:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20220329_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='service',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.service'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patientuser',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 29, 18, 12, 28, 919855)),
        ),
    ]