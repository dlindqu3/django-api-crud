# Generated by Django 4.0.5 on 2022-07-01 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('location', models.CharField(max_length=256)),
                ('temperature', models.IntegerField()),
            ],
        ),
    ]
