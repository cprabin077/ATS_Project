from django import forms
from .models import Candidate, Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter job title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Enter job description'
            }),
            'required_skills': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Python, Django, SQL, ML'
            }),
        }


class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        exclude = ['ats_score', 'recommendation']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter full name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone number'
            }),
            'applied_job': forms.Select(attrs={
                'class': 'form-select'
            }),
            'resume': forms.FileInput(attrs={
                'class': 'form-control'
            }),
        }