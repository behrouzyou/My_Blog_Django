from django.urls import path
from .views import ProfileView,ProfileUpdateView
app_name='accounts'
urlpatterns = [
    path('profile/<str:username>/',ProfileView.as_view(),name='profile'),
    path('profile/<str:username>/edit/',ProfileUpdateView.as_view(),name='profile_edit'),
]
