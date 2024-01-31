from django.contrib import admin
from .models import Configuration,Facts,Skill,SkillDescription

# Register your models here.

@admin.register(Configuration)
class ConfigurationModelAdmin(admin.ModelAdmin):
    pass

@admin.register(Facts)
class FactsModelAdmin(admin.ModelAdmin):
    pass

@admin.register(Skill)
class SkillModelAdmin(admin.ModelAdmin):
    pass
@admin.register(SkillDescription)
class SkillModelDescription(admin.ModelAdmin):
    pass