# Generated by Django 4.0.1 on 2022-01-31 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Name')),
                ('address', models.CharField(max_length=300)),
                ('Tag_no', models.CharField(max_length=15, verbose_name='Tag Number')),
                ('phone', models.CharField(blank=True, max_length=25, verbose_name='Contact Phone')),
                ('gadget', models.CharField(max_length=15, verbose_name='Gadget')),
                ('Time_in', models.DateTimeField(blank=True, verbose_name='Timein')),
                ('Time_out', models.DateTimeField(blank=True, verbose_name='TimeOut')),
            ],
        ),
    ]
