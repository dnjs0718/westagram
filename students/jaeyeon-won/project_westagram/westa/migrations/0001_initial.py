# Generated by Django 3.1.7 on 2021-04-02 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
