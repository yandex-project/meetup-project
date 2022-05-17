from django.contrib.auth.decorators import login_required
from django.urls import path
from meetups import views


urlpatterns = [
    path('add_meetup/', login_required(views.CreateMeetupView.as_view()), name='create_meetup'),
    path('<slug>/', views.MeetupDetailView.as_view(), name='meetup_detail'),
    path('<slug>/update_meetup/', views.UpdateMeetupView.as_view(), name='update_meetup'),
    path('<slug>/add_lecture/', views.CreateLectureView.as_view(), name='create_lecture'),
    path('<slug>/<pk>/', views.UpdateLectureView.as_view(), name='update_lecture'),
]
