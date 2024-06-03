from django import forms

from app1.models import student

class studentform(forms.ModelForm):
    class Meta:
        model=student
        fields=["name","college","course"]
        