from django import forms
from app.models import User, Games, Admin, Book

class UserForm(forms.ModelForm):
	class Meta:
		model=User
		fields="__all__"

class GameForm(forms.ModelForm):
	class Meta:
		model=Games
		fields='__all__'		

class AdminForm(forms.ModelForm):
	class Meta:
		model=Admin
		fields='__all__'

class BookForm(forms.ModelForm):
	class Meta:
		model=Book
		fields='__all__'				

				