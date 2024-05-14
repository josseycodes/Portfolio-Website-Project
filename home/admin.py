from django.contrib import admin
from .models import Portfolio, About, Skill, Category, Home

# Register your models here.

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['title', 'link']

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['id']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'percentage']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['title']




