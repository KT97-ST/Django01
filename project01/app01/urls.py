from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('listquestion/', views.viewlistquestion, name="viewlistquestion"),
    path('detailquestion/<int:question_id>', views.detailView, name="detail"),
    path('choicevote/<int:question_id>', views.choiceVote, name="choicevote"),

]
