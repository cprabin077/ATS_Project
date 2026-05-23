from django.shortcuts import render, redirect
from .models import Candidate, Job
from .forms import CandidateForm, JobForm
from .utils import extract_resume_text
from .ai import calculate_ats_score, get_recommendation


def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'job/job_list.html', {'jobs': jobs})

def job_create(request):
    form = JobForm()
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    return render(request, 'job/job_form.html', {'form': form})


def candidate_list(request):
    candidates = Candidate.objects.all()
    return render(request, 'candidate/candidate_list.html', {'candidates': candidates})


def candidate_create(request):
    form = CandidateForm()
    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            candidate = form.save()
            resume_text = extract_resume_text(candidate.resume.path)
            job = candidate.applied_job
            score = calculate_ats_score(job.description + ' ' + job.required_skills, resume_text)
            candidate.ats_score = score
            candidate.recommendation = get_recommendation(score)
            candidate.save()
            return redirect('candidate_list')
    return render(request, 'candidate/candidate_form.html', {'form': form})