from django.urls import path
from meetups import views

urlpatterns = [
    path('<slug>/', views.MeetupDetailView.as_view(), name='meetup_detail'),
    path('<slug>/add_lecture/', views.CreateLectureView.as_view(), name='create_lecture'),
    path('<slug>/<pk>/', views.UpdateLectureView.as_view(), name='update_lecture'),
]
