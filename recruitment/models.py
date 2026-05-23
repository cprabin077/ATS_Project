from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    required_skills = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    resume = models.FileField(upload_to='resumes/')
    applied_job = models.ForeignKey(Job, on_delete=models.CASCADE)
    ats_score = models.FloatField(default=0)
    recommendation = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

