from django.shortcuts import render, get_object_or_404, redirect
from .models import JobApplication
from .forms import JobApplicationForm, SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login


def landing_page(request):
    return render(request, 'main_app/home.html')

def about(request):
    return render(request, 'main_app/about.html')

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(request.POST.get('next') or 'application_list')
    else:
        form = SignUpForm()
    return render(request, 'main_app/sign_up.html', {'form': form})


@login_required
def application_detail(request, pk):
    application = get_object_or_404(JobApplication, pk=pk)
    return render(request, 'main_app/application_detail.html', {'application': application})


@login_required
def application_list(request):
    applications = JobApplication.objects.filter(user=request.user)
    return render(request, 'main_app/application_list.html', {'applications': applications})

@login_required
def application_create(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            job_application = form.save(commit=False)
            job_application.user = request.user
            job_application.save()
            return redirect('application_list')
    else:
        form = JobApplicationForm()
    return render(request, 'main_app/application_form.html', {'form': form})

@login_required
def application_update(request, pk):
    application = get_object_or_404(JobApplication, pk=pk, user=request.user)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect('application_list')
    else:
        form = JobApplicationForm(instance=application)
    return render(request, 'main_app/application_form.html', {'form': form})

@login_required

def application_delete(request, pk):
    application = get_object_or_404(JobApplication, pk=pk)
    if request.method == 'POST':
        application.delete()
        return redirect('application_list')
    return render(request, 'main_app/application_confirm_delete.html', {'application': application})