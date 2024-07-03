# Generated by Django 5.0.2 on 2024-02-28 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0003_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('department', models.CharField(max_length=100)),
                ('doctor', models.CharField(max_length=100)),
            ],
        ),
    ]
