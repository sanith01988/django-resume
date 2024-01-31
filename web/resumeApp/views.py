from typing import Any
from django.shortcuts import render
from django.views.generic import (TemplateView)
from about.models import About
from configuration.models import Configuration,Facts,Skill,SkillDescription
from resumeApp.models import Resume,Education,Experience,Testimonials,ContactDetails
from .forms import ContactForm
from django.http import JsonResponse

# Create your views here.

class HomePageTemplateView(TemplateView):
    template_name = 'index.html'
    
    def get_about_obj(self,*args,**kwargs):
        return About.objects.first()
    def get_configuration_obj(self,*args,**kwargs):
        return Configuration.objects.first()
    def get_facts_obj(self,*args,**kwargs):
        return Facts.objects.first()
    def get_skills(self, *args, **kwargs):
        return Skill.objects.all()
    def get_common_description(self, *args, **kwargs):
        common_description_obj = SkillDescription.objects.first()
        if common_description_obj:
            return common_description_obj.description
        return None
    def get_resume(self,*args,**kwargs):
        return Resume.objects.first()
    def get_education(self,resume_obj,*args,**kwargs):
        return Education.objects.filter(resume=resume_obj)
    def get_experience(self,resume_obj,*args,**kwargs):
        return Experience.objects.filter(resume=resume_obj)
    def get_testimonials(self,*args,**kwargs):
        return Testimonials.objects.all()
    def get_contact(self,*args,**kwargs):
        return ContactDetails.objects.first()
    def get_context_data(self,*args,**kwargs):
        context =  super(HomePageTemplateView,self).get_context_data(**kwargs)
        context['about_obj'] = self.get_about_obj()
        context['config_obj'] = self.get_configuration_obj()
        context['facts_obj'] = self.get_facts_obj()
        context['common_description'] = self.get_common_description()
        context['skills'] = self.get_skills()
        context['resume'] = self.get_resume()
        context['educations'] = self.get_education(context['resume'])
        context['experiences'] = self.get_experience(context['resume'])
        context['testimonials'] = self.get_testimonials()
        context['contact'] = self.get_contact()
        # context['form'] = ContactForm()
        return context



def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html', {'success_message': True})
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form})