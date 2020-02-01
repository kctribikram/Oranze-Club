from django import forms
from app.models import User, Game, Admin

class UserForm(forms.ModelForm):
	class Meta:
		model=User
		fields="__all__"

class GameForm(forms.ModelForm):
	class Meta:
		model=Game
		fields='__all__'		

class AdminForm(forms.ModelForm):
	class Meta:
		model=Admin
		fields='__all__'		

				