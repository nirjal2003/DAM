# Generated by Django 3.2.5 on 2022-04-23 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='appointment',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.appointment'),
        ),
    ]