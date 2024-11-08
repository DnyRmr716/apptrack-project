from django import forms
from .models import JobApplication
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class JobApplicationForm(forms.ModelForm):
    date_applied = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False
    )

    class Meta:
        model = JobApplication
        fields = ['application_title', 'job_title', 'company', 'job_summary', 'date_applied', 'status', 'notes']


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']