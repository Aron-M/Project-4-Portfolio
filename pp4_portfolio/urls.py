"""
URL configuration for pp4_portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from my_pf import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.display_all, name='all'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('edit-personal-details/', views.display_edit_personal_details, name='edit-personal-details'),
    path('edit-headings/', views.display_edit_headings, name='edit-headings'),
    path('edit-skills/<int:skill_id>/', views.display_edit_skills, name='edit-skills'),
    path('edit-projects/<int:project_id>/', views.display_edit_projects, name='edit-projects'),
    path('home/', views.display_all, name='home')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
