from django.db import models
from django.contrib.auth.models import User

class JobApplication(models.Model):
    JOB_STATUS_CHOICES = [
        ('🟡Applied', '🟡Applied'),
        ('🔵Interviewing', '🔵Interviewing'),
        ('🟢Accepted', '🟢Accepted'),
        ('🔴Rejected', '🔴Rejected'),
        ('🟠No Response', '🟠No Response'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    application_title = models.CharField(max_length=100, default="Untitled Application")
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    job_summary = models.TextField(max_length=500, default="No summary provided")
    date_applied = models.DateField()
    status = models.CharField(max_length=20, choices=JOB_STATUS_CHOICES)
    notes = models.TextField(max_length=250, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.application_title} - {self.job_title} at {self.company}"
