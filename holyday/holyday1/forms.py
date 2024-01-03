from django import forms

class inputform(forms.Form):
    
    statecode=forms.CharField(max_length=2)
    