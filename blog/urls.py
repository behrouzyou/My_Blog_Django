from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('article/sample-slug/',views.article_detail,name='article-detail'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('profile/',views.profile,name='profile'),
    path('article/create/',views.article_form,name='article-create'),
    path('personal/',views.personal,name='personal'),
]
