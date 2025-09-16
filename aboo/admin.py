from django.contrib import admin
from .models import Project,Skill,Service,ContactMessage,Technology

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','completed_date','is_featured')
    list_filter = ('is_featured', 'completed_date')
    search_fields = ('title', 'description')
    slug = {'slug': ("title,")}

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name','category','get_technology', 'show_on_website')
    list_filter = ('category', 'technology', 'show_on_website')
    list_editable = ['show_on_website']

    def get_technology(self, obj):
        return ", ".join([tech.name for tech in obj.technology.all()])
    get_technology.short_description = 'Technology'

@admin.register(Technology)
class Technology(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    search_fields = ('title', 'description')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'timestamp', 'is_read')
    list_filter = ('is_read', 'timestamp')
    readonly_fields = ('timestamp',)
    list_editable = ('is_read', )
