from django.urls import path
from users import views
from django.contrib.auth.decorators import login_required
import django.contrib.auth.views as admin_views

urlpatterns = [
    path('users/<int:pk>/', views.UserDetail.as_view(), name='detail_users'),
    path('users/', views.UserList.as_view(), name='all_users'),
    path('profile/', login_required(views.ProfilePage.as_view()), name='profile'),
    path('signup/', views.SignupView.as_view(), name='signup'),

    # Django login
    path(
        'login/',
        admin_views.LoginView.as_view(template_name='users/auth/login.html'),
        name='login'
    ),
    path(
        'logout/',
        admin_views.LogoutView.as_view(template_name='users/auth/logout.html'),
        name='logout'
    ),
    path(
        'password_change/',
        admin_views.PasswordChangeView.as_view(template_name='users/auth/password_change.html'),
        name='password_change'
    ),
    path(
        'password_change/done/',
        admin_views.PasswordChangeDoneView.as_view(template_name='users/auth/password_change_done.html'),
        name='password_change_done'
    ),
    path(
        'password_reset/',
        admin_views.PasswordResetView.as_view(template_name='users/auth/password_reset.html'),
        name='password_reset'
    ),
    path(
        'password_reset/done/',
        admin_views.PasswordResetDoneView.as_view(template_name='users/auth/password_reset_done.html'),
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        admin_views.PasswordResetConfirmView.as_view(template_name='users/auth/reset.html'),
        name='password_reset_confirm'
    ),
    path(
        'reset/done/',
        admin_views.PasswordResetCompleteView.as_view(template_name='users/auth/reset_done.html'),
        name='password_reset_complete'
    ),
]
