# Generated by Django 4.0.4 on 2022-05-21 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DryJoke',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joke', models.CharField(max_length=1000)),
                ('author', models.CharField(max_length=50)),
            ],
        ),
    ]
