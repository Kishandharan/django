from django import forms

class inputweb(forms.Form):
    num1=forms.IntegerField(min_value=1,max_value=20,label="Enter the number")