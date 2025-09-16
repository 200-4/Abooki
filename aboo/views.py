from django.shortcuts import render, redirect,get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import Project,Skill,Service


# Create your views here.

def home(request):
    featured_projects = Project.objects.filter(is_featured=True)[:3]
    skills = Skill.objects.filter(show_on_website=True)
    services = Service.objects.all()

    context = {
        'featured_projects': featured_projects,
        'skills': skills,
        'services': services,
    }
    return render(request, 'aboo/index.html', context)

def projects(request):
    all_projects = Project.objects.all().order_by('-completed_date')
    return render(request, 'aboo/projects.html', {'project': all_projects})
def hire_me(request):
    services = Service.objects.all()
    return render(request, 'aboo/hire.html', {'services':services})
def learn_more(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    return render(request, 'aboo/learn_more.html', {'service': service})



def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        messages = request.POST.get('message')

        #save to database

        from .models import ContactMessage
        ContactMessage.objects.create(
            name = name,
            email=email,
            subject=subject,
            messages=messages
        )

        #Send email notification
        send_mail(
            f'Portfolio Contact: {subject}',
            f'From: {name} ({email})\n\n{messages}',
            settings.DEFAULT_FROM_EMAIL,
            [settings.CONTACT_EMAIL],
            fail_silently=False, 
        )

        messages.success(request, 'Your message has been sent successfully')
        return redirect('home')
    return render(request, 'aboo/contact.html')

