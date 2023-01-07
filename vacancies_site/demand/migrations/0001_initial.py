# Generated by Django 3.2.6 on 2023-01-07 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DemandData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('data', models.CharField(max_length=500)),
                ('individual_id', models.CharField(max_length=100)),
                ('added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
