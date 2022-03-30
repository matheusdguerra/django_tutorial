from django.urls import path
from django_tutorial.core.views import index

urlpatterns = [
    path('', index, name='index'),
]
