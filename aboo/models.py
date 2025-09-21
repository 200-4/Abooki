from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    slug = models.SlugField(max_length=100)
    project_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True)
    completed_date = models.DateField(default=timezone.now)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Technology(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('DATA_SCIENCE', 'Data Science'),
        ('WEB_DEVELOPMENT', 'Web Development'),
        ('TOOLS', 'Tools & Technologies')
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True,null=True)
    skill_icon = model.CharField(max_length=50,default='fa fa-user')
    # proficiency = models.IntegerField(default=80)
    technology = models.ManyToManyField(Technology, related_name='skills', blank=True)

    show_on_website = models.BooleanField(default=True)



    def __str__(self):
        return self.name

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon_class = models.CharField(max_length=50, default='fas fa-laptop')
    price = models.CharField(max_length=50, default='$50/hour')
    slug = models.SlugField(max_length=100, null=True, blank=True)
    overview = models.TextField(blank=True,null=True)
    challenges = models.TextField(blank=True, null=True)
    solutions = models.TextField(blank=True, null=True)
    technologies = models.ManyToManyField(Technology, blank=True)
    conclusion = models.TextField(blank=True, null=True)
    image1 = models.ImageField(upload_to='services/', blank=True, null=True)
    image2 = models.ImageField(upload_to='services/', blank=True, null=True)




    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    timestamp = models.DateField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.subject}"



