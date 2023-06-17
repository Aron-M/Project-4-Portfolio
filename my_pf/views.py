from django.shortcuts import render, get_object_or_404, redirect
from .models import PersonalDetails, Headings, Project, Skills, SkillCategory
from .forms import PersonalDetailsForm, HeadingsForm, SkillsForm, ProjectForm
from django.contrib import messages
from django.core.files.storage import default_storage

def display_skills_page(request):
    return render(request, 'pages/skills.html')

def display_all(request):
    data = PersonalDetails.objects.all()
    skills = Skills.objects.all()
    category = SkillCategory.objects.all()
    projects = Project.objects.all()
    headings = Headings.objects.all()
    context = {
        'data': data, 'headings': headings, 'projects': projects, 'skills': skills, 'category': category
        }
    if request.path == "home/":
        return render(request, 'pages/home-page.html', context )
    else: 
        return render(request, 'pages/home-page.html', context )


def dashboard_view(request):
    skills = Skills.objects.all()
    skill = get_object_or_404(Skills, id=11)
    project = get_object_or_404(Project, id=23)
    context = {
        'skill': skill, 'project': project, 'skills': skills
    }
    return render(request, 'pages/dashboard.html')

def display_edit_personal_details(request):
    data = PersonalDetails.objects.all()
    personal_details_form = PersonalDetailsForm()
    detail = get_object_or_404(PersonalDetails)
    if request.method == 'POST':
        personal_details_form = PersonalDetailsForm(request.POST, instance=detail)
        if personal_details_form.is_valid():
            data.image = request.FILES['image']
            personal_details_form.save()
            return redirect('edit-personal-details')
    personal_details_form = PersonalDetailsForm(instance=detail)
    context = {
        'data': data, 'personal_details_form': personal_details_form
        }
    if request.path == "edit-personal-details/":
        return render(request, 'pages/edit-personal-details.html', context )
    else: 
                return render(request, 'pages/edit-personal-details.html', context )


from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

def display_edit_headings(request):
    all_headings = Headings.objects.all()
    heading = get_object_or_404(Headings)

    if request.method == 'POST':
        headings_form = HeadingsForm(request.POST, request.FILES, instance=heading)
        if headings_form.is_valid():
            if 'profile_image' in request.FILES:
                old_image = heading.profile_image
                if old_image:
                    default_storage.delete(old_image.path)
                heading.profile_image = request.FILES['profile_image']
            headings_form.save()
            return redirect('edit-headings')
    else:
        headings_form = HeadingsForm(instance=heading)

    context = {
        'headings': all_headings,
        'headings_form': headings_form
    }

    return render(request, 'pages/edit-headings.html', context)



def display_edit_skills(request, skill_id):
    skill = get_object_or_404(Skills, id=skill_id)
    skills_form = SkillsForm(instance=skill)
    skills = Skills.objects.all()
    category = SkillCategory.objects.all()
    
    if request.method == 'POST':
        skills_form = SkillsForm(request.POST, instance=skill)
        if skills_form.is_valid():
            Skills.image = request.FILES['image']
            skills_form.save()
            messages.success(request, 'Skills updated successfully.')
            return redirect('edit-skills', skill_id=skill.id)
        else:
            messages.error(request, 'Error updating skills.')
    
    context = {
        'skill': skill,
        'skills_form': skills_form,
        'category': category,
        'skills': skills
    }
    return render(request, 'pages/edit-skills.html', context)



def display_edit_projects(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project_form = ProjectForm(instance=project)
    projects = Project.objects.all()

    if request.method == 'POST':
        project_form = ProjectForm(request.POST, instance=project)
        if project_form.is_valid():
            project.image = request.FILES['image']
            project_form.save()
            return redirect('edit-projects', project_id=project.id)
        else:
            messages.error(request, 'Error updating skills.')

    context = {
        'projects': projects,
        'project_form': project_form,
        'project': project
    }
    return render(request, 'pages/edit-projects.html', context)


def add_skill(request):
    skills = Skills.objects.all()
    skills_form = SkillsForm()
    category = SkillCategory.objects.all()
    if request.method == 'POST':
        skills_form = SkillsForm(request.POST)
        if skills_form.is_valid():
            skills_form.save()
            return redirect('add-skill')
    else:
        context = {
            'skills': skills,
            'skills_form': skills_form,
            'category': category
        }
        return render(request, 'pages/add-skill.html', context)


def add_project(request):
    if request.method == 'POST':
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            project = project_form.save(commit=False)
            project.image = request.FILES['image']
            project.save()
            return redirect('add-project')
    else:
        project_form = ProjectForm()

    projects = Project.objects.all()
    context = {
        'projects': projects,
        'project_form': project_form
    }
    return render(request, 'pages/add-project.html', context)





