from django.contrib import admin
from django.urls import path
from aloformacao.views import aloformacao

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alunos/', aloformacao),
]
