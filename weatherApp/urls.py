from django.urls import path
from . import views

# the url patterns
urlpatterns = [
    path('', views.index, name='home')
]