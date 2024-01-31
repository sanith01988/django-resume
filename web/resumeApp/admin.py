from django.contrib import admin
from .models import Resume,Education,Experience,Award,Testimonials,ContactDetails
# Register your models here.

@admin.register(Resume)
class ResumeModelAdmin(admin.ModelAdmin):
    pass

@admin.register(Education)
class EducationModelAdmin(admin.ModelAdmin):
    list_filter = ('resume',)
    search_fields = ('degree','institution',)

@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
@admin.register(Experience)
class ExperienceModelAdmin(admin.ModelAdmin):
    list_filter = ('resume',)
    search_fields = ('title','company',)
    filter_horizontal = ('awards',)

@admin.register(Testimonials)
class TestimonialsModelAdmin(admin.ModelAdmin):
    pass

@admin.register(ContactDetails)
class ContactDetailsModelAdmin(admin.ModelAdmin):
    pass