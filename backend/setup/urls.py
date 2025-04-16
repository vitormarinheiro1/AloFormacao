from django.contrib import admin
from django.urls import path
from forum.views import forum

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alunos/', forum),
]
