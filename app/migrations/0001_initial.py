# Generated by Django 3.0 on 2020-02-16 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'admin',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('game', models.CharField(max_length=30)),
                ('shift', models.CharField(choices=[('Morning', 'Morning'), ('Day', 'Day'), ('Evening', 'Evening')], max_length=30)),
                ('package', models.CharField(choices=[('Basic', 'Basic'), ('Medium', 'Medium'), ('Standard', 'Standard')], max_length=30)),
                ('number', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'book',
            },
        ),
        migrations.CreateModel(
            name='Games',
            fields=[
                ('game_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('shift', models.CharField(choices=[('Morning', 'Morning'), ('Day', 'Day'), ('Evening', 'Evening')], max_length=30)),
                ('package', models.CharField(choices=[('Basic', 'Basic'), ('Medium', 'Medium'), ('Standard', 'Standard')], max_length=30)),
            ],
            options={
                'db_table': 'games',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('message', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'message',
            },
        ),
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
        migrations.RunSQL("insert into Admin(fname,lname,username,password) values('admin','admin','admin','admin')")
    ]
