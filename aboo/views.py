from django.shortcuts import render, redirect,get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import Project,Skill,Service
from django.http import JsonResponse


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
        message = request.POST.get('message')

        #save to database

        # from .models import ContactMessage
        # ContactMessage.objects.create(
        #     name = name,
        #     email=email,
        #     subject=subject,
        #     message=message
        # )
       data = {
            "Messages": [
                {
                    "From": {
                        "Email": settings.MAILJET_SENDER,
                        "Name": name
                    },
                    "To": [
                        {
                            "Email": settings.CONTACT_EMAIL,  # Your inbox
                            "Name": "Josh"
                        }
                    ],
                    "Subject": subject,
                    "TextPart": f"From: {name} ({email})\n\n{message}",
                }
            ]
        }

        response = requests.post(
            "https://api.mailjet.com/v3.1/send",
            auth=(settings.MAILJET_API_KEY, settings.MAILJET_API_SECRET),
            json=data
        )

        if response.status_code == 200:
            # return JsonResponse({"success": True, "message": "Message sent successfully"})
            return redirect("/?success=1")
        else:
            # return JsonResponse({"success": False, "error": response.text})
            return redirect("/?error=1")
       # If GET request, just go home
      return redirect("/")

