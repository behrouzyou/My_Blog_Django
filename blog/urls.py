from django.urls import path
from .views import login,signup,profile,article_form,personal,ArticleListView,ArticleDetailView
urlpatterns = [
    path('article/(?P<slug>[-a-zA-Z0-9_]+)/\\Z',ArticleDetailView.as_view(),name='article-detail'),
    path('login/',login,name='login'),
    path('signup/',signup,name='signup'),
    path('profile/',profile,name='profile'),
    path('article/create/',article_form,name='article-create'),
    path('personal/',personal,name='personal'),
    path('',ArticleListView.as_view(),name='home')
]
