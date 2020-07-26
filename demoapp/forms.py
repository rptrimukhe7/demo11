from django import forms
from demoapp.models import Student

# class StudentForm(forms.Form):
#     first_name = forms.CharField(max_length = 200)  
#     last_name = forms.CharField(max_length = 200)  
#     roll_number = forms.IntegerField()  

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"