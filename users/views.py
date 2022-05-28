from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from users.forms import UserForm, RegistrationForm
from users.models import User
from datetime import datetime


class ProfilePage(View):
    template_name = 'users/profile.html'

    def get(self, request):
        user = request.user
        user_form = UserForm(instance=user)

        context = {
            'user_form': user_form,
            'user': user,
            # 'owner_meetups': user.my_meetups.prefetch_related('tags').order_by('date'),
            # 'participant_meetups': user.meetups.prefetch_related('tags').order_by('date'),
            'owner_meetups': user.my_meetups.filter(
                date__gte=datetime.today()
            ).prefetch_related('tags').order_by('date'),
            'participant_meetups': user.meetups.filter(
                date__gte=datetime.today()
            ).prefetch_related('tags').order_by('date'),
        }
        return render(request, self.template_name, context=context)

    def post(self, request):
        user_form = UserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('profile')
        else:
            user = request.user

            context = {
                'user_form': user_form,
                'user': user,
                # 'owner_meetups': user.my_meetups.prefetch_related('tags').order_by('date'),
                # 'participant_meetups': user.meetups.prefetch_related('tags').order_by('date'),
                'owner_meetups': user.my_meetups.filter(
                    date__gte=datetime.today()
                ).prefetch_related('tags').order_by('date'),
                'participant_meetups': user.meetups.filter(
                    date__gte=datetime.today()
                ).prefetch_related('tags').order_by('date'),
            }
            return render(request, self.template_name, context=context)


class UserDetail(View):
    template_name = 'users/user_detail.html'

    def get(self, request, pk):
        user = get_object_or_404(
            User.objects.only('email', 'first_name', 'last_name', 'description', 'avatar'),
            pk=pk
        )
        context = {
            'user': user,
        }
        return render(request, self.template_name, context=context)


class UserList(View):
    template_name = 'users/all_users.html'

    def get(self, request):
        users = User.objects.all()

        context = {
            'users': users
        }
        return render(request, self.template_name, context=context)


class SignupView(View):
    template_name = 'users/auth/signup.html'

    def get(self, request):
        form = RegistrationForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            return redirect('login')
        else:
            context = {'form': form}
            return render(request, self.template_name, context)
