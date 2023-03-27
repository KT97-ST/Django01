from django.urls import path

from . import views

app_name = 'login'
urlpatterns = [
    path('', views.LoginClass.as_view(), name="login"),
    path('viewuser/', views.ViewUser.as_view(), name="viewuser"),
    path('view-product/', views.view_product, name="view-product"),
]
