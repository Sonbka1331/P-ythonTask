# Generated by Django 3.2 on 2023-05-17 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KeySkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=4)),
                ('key_skills', models.CharField(max_length=250)),
                ('added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
