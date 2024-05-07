from django import forms

class inputdat(forms.Form):
    gmail = forms.CharField(max_length=50,required=True)
    psw = forms.CharField(max_length=50,required=True,widget=forms.PasswordInput())
    
class inputdat1(forms.Form):
    name = forms.CharField(max_length=50,required=True)
    gmail = forms.CharField(max_length=50,required=True)
    psw = forms.CharField(max_length=50,required=True,widget=forms.PasswordInput())
    psw1 = forms.CharField(max_length=50,required=True,widget=forms.PasswordInput())