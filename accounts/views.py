from django.shortcuts import render
from django.views.generic import DetailView,UpdateView
from .models import CustomUser
from .forms import UserUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
class ProfileView(DetailView):
    model = CustomUser
    template_name = "profile.html"
    context_object_name='profile_user'
    slug_field='username'
    slug_url_kwarg='username'

class ProfileUpdateView(UpdateView,LoginRequiredMixin,UserPassesTestMixin):
    model=CustomUser
    form_class=UserUpdateForm
    template_name='profile_edit.html'
    slug_field='username'
    slug_url_kwarg='username'



    def get_success_url(self):
        return reverse_lazy('account:profile',kwargs={'username':self.request.user.username })
    def test_func(self):
        profile=self.object.get()
        return self.request.user == profile
