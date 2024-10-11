from django import forms
from.models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('fname', 'lname', 'email', 'password', 'age')
        widgets = {
            'password': forms.PasswordInput(),  # Added password field with password input widget
            'age': forms.NumberInput(),  # Added age field with number input widget
        }