from .models import Stock_in,Stock_out
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import User

class stock_in_form(forms.ModelForm):
    class Meta:
        model = Stock_in
        fields = "__all__"
class stock_out_form(forms.ModelForm):
    class Meta:
        model = Stock_out
        fields = "__all__"
        
    widgets ={
        
    }
    
class SignUpForm(UserCreationForm):
#p
   class Meta:
      model = User 
      fields = ('username', 'password1', 'password2')