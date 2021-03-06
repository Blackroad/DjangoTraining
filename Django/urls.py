"""Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from students.views import groups, students, visits
from .settings import MEDIA_ROOT, DEBUG


urlpatterns = [
    # students urls
    path('', students.students_list, name='students_list'),
    path('students/add', students.students_add, name='students_add'),
    path(r'students/<int:sid>/edit', students.students_edit, name='students_edit'),
    path(r'students/<int:sid>/delete', students.students_delete, name='students_delete'),
    # students urls
    path('groups/', groups.groups_list, name='groups'),
    path('groups/add', groups.groups_add, name='groups_add'),
    path(r'groups/<int:gid>/edit', groups.groups_edit, name='groups_edit'),
    path(r'groups/<int:gid>/delete', groups.groups_delete, name='groups_delete'),
    # visits urls
    path('visits/', visits.visits_list, name='visits'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

