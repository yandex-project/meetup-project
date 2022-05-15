from django.urls import path
from meetups import views

urlpatterns = [
    path('<slug>/', views.MeetupDetailView.as_view(), name='meetup_detail'),
    path('<slug>/add/', views.CreateLectureView.as_view(), name='create_lecture'),
]
