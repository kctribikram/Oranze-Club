# Generated by Django 3.0 on 2020-01-27 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('number', models.IntegerField()),
                ('user_name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=50)),
                ('repassword', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
