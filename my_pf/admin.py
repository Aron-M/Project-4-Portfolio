from django.contrib import admin
from .models import PersonalDetails, Headings, Project, Skill, SkillCategory


admin.site.register(PersonalDetails)
admin.site.register(Headings)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(SkillCategory)
