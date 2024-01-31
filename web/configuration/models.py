from django.db import models

# Create your models here.
class Configuration(models.Model):
    name = models.CharField(
        'Name',
        max_length=50,
        null=False,
        blank=False
    )
    typed = models.CharField(
        'Typed',
        max_length=255,
        help_text="Typed Like this -> Developer,Devops"
    )
    facebook = models.URLField(
        "facebook"
    )
    twitter = models.URLField(
        "Twitter"
    )
    linkedin = models.URLField(
        "LinkedIn"
    )
    instagram = models.URLField(
        "Instagram"
    )
    skype = models.URLField(
        "Skype"
    )
    
    def __str__(self, *args, **kwargs):
        return f'{self.id} {self.name}'
    
    def __unicode__(self,*args,**kwargs):
        return f'{self.id} {self.name}'
class Facts(models.Model):
    description = models.CharField(
        "Description",
        max_length = 255
    )
    clients_count = models.IntegerField(
        "Happy Clients",
        default=1
    )
    projects = models.IntegerField(
        "Projects",
        default=1
    )
    hours_support = models.IntegerField(
        "Hours Of Support",
        default=1
    )
    awards = models.IntegerField(
        "Awards",
        default=1
    )
    def __str__(self, *args, **kwargs):
        return f'{self.id} {self.clients_count}'
    
    def __unicode__(self,*args,**kwargs):
        return f'{self.id} {self.clients_count}'

class SkillDescription(models.Model):
    description = models.TextField(
        'Common Description About Skill Set'
    )

    def __str__(self):
        return "Common Description"
class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(default=0, help_text='Proficiency level in percentage')
    def __str__(self):
        return self.name
    
