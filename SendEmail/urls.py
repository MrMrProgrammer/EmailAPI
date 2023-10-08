from django.urls import path
from . import views

urlpatterns = [
    path('SendEmailAPI', views.SendEmailView.as_view(), name='SendEmailAPI'),
]

