from django.urls import path
from schedule import views

app_name = 'schedule'

urlpatterns = [
    path('<int:event_id>/', views.ScheduleView.as_view(), name='meetup-detail'),
    path('', views.ScheduleView.as_view(), name='schedule'),
]
