from django.urls import path

from . import views

app_name = 'news'
urlpatterns = [
    path('', views.index, name="index"),
    path('add/', views.add_post, name="add"),
    path('email/', views.email_view, name="email"),
    path('processemail/', views.process_email, name="processemail"),
]
