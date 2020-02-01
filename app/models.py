from django.db import models

class User(models.Model):
	user_id=models.AutoField(auto_created=True,primary_key=True)
	fname=models.CharField(max_length=30)
	lname=models.CharField(max_length=30)
	email=models.CharField(max_length=50)
	number=models.IntegerField()
	user_name=models.CharField(max_length=30)
	password=models.CharField(max_length=50)
	repassword=models.CharField(max_length=50)

	class Meta:
		db_table="user"

class Game(models.Model):
	game_id=models.AutoField(auto_created=True,primary_key=True)
	name=models.CharField(max_length=30)
	price=models.IntegerField()
	shift=models.CharField(max_length=30)

	class Meta:
		db_table="game"


class Admin(models.Model):
	id=models.AutoField(auto_created=True,primary_key=True)
	fname=models.CharField(max_length=30)
	lname=models.CharField(max_length=30)
	username=models.CharField(max_length=30)
	password=models.CharField(max_length=30)
	class Meta:
		db_table="admin"