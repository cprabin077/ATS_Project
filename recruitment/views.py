from django.shortcuts import get_object_or_404, render, redirect
from .models import Candidate, Job
from .forms import CandidateForm, JobForm
from .utils import extract_resume_text
from .ai import calculate_ats_score, get_recommendation

#-------------------------- JOB ---------------------------------

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
        else:
            print(form.errors)   # check errors here

    return render(request, 'job/job_form.html', {'form': form})

def job_edit(request, id):
    job = get_object_or_404(Job, id=id)
    form = JobForm(instance=job)

    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('job_list')

    return render(request, 'job/job_form.html', {'form': form})


def job_delete(request, id):
    job = get_object_or_404(Job, id=id)
    job.delete()
    return redirect('job_list')


#----------------------------- CANDIDATE ----------------------------------

def candidate_list(request):
    candidates = Candidate.objects.all()
    return render(request, 'candidate/candidate_list.html', {'candidates': candidates})


def candidate_create(request):
    form = CandidateForm()

    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES)

        if form.is_valid():
            try:
                # Save candidate first
                candidate = form.save()
                print("Candidate saved!")

                # Extract resume text
                resume_text = extract_resume_text(candidate.resume.path)
                print("Resume text extracted!")

                # Calculate ATS score
                job = candidate.applied_job
                score = calculate_ats_score(
                    job.description + " " + job.required_skills,
                    resume_text
                )

                candidate.ats_score = score
                candidate.recommendation = get_recommendation(score)
                candidate.save()

                print("ATS score updated!")
                return redirect('candidate_list')

            except Exception as e:
                print("ERROR:", e)

        else:
            print("FORM ERRORS:", form.errors)

    return render(request, 'candidate/candidate_form.html', {'form': form})


def candidate_edit(request, id):
    candidate = get_object_or_404(Candidate, id=id)
    form = CandidateForm(instance=candidate)

    if request.method == 'POST':
        form = CandidateForm(
            request.POST,
            request.FILES,
            instance=candidate
        )

        if form.is_valid():
            candidate = form.save()

            resume_text = extract_resume_text(candidate.resume.path)
            job = candidate.applied_job

            score = calculate_ats_score(
                job.description + " " + job.required_skills,
                resume_text
            )

            candidate.ats_score = score
            candidate.recommendation = get_recommendation(score)
            candidate.save()

            return redirect('candidate_list')

    return render(
        request,
        'candidate/candidate_form.html',
        {'form': form}
    )


def candidate_delete(request, id):
    candidate = get_object_or_404(Candidate, id=id)
    candidate.delete()
    return redirect('candidate_list')