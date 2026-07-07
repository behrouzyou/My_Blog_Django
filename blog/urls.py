from django.urls import path
from .views import (login,signup,personal,ArticleListView,
                    ArticleDetailView,ArticleCreateView,ArticleUpdateView,ArticleDeleteView,
                    SearchResultView)
urlpatterns = [
    path('article/(?P<slug>[-a-zA-Z0-9_]+)/\\Z',ArticleDetailView.as_view(),name='article-detail'),
    path('login/',login,name='login'),
    path('signup/',signup,name='signup'),
    path('article/new/',ArticleCreateView.as_view() ,name='article-create'),
    path('article/(?P<slug>[-a-zA-Z0-9_]+)/\\Z/edit/',ArticleUpdateView.as_view(),name='article_update'),
    path('article/(?P<slug>[-a-zA-Z0-9_]+)/\\Z/delete/',ArticleDeleteView.as_view(),name='article_delete'),
    path('personal/',personal,name='personal'),
    path('',ArticleListView.as_view(),name='home'),
    path('search/',SearchResultView.as_view(),name='search')
]
