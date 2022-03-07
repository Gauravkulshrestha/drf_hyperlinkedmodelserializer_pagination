# Generated by Django 4.0.3 on 2022-03-07 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('emp_id', models.IntegerField()),
                ('mobile', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
