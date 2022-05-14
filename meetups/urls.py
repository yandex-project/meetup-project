from django.urls import path
from meetups import views

urlpatterns = [
    path('<slug>/', views.MeetupDetailView.as_view(), name='meetup_detail')
]
