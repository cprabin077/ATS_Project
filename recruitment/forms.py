from django import forms
from .models import Candidate, Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'


class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = '__all__'