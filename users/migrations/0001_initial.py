# Generated by Django 5.0 on 2023-12-21 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_id', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('role', models.CharField(max_length=30)),
                ('department', models.CharField(max_length=30)),
                ('active', models.BooleanField(default=True)),
                ('createdAt', models.DateTimeField(auto_now=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
