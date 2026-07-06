from django.shortcuts import render
from .models import Article,Category
from django.views.generic import ListView,DetailView
class ArticleListView(ListView):
    model=Article
    template_name='index.html'
    context_object_name='articles'
    paginate_by=2

    def get_queryset(self):
        return Article.objects.all()

class ArticleDetailView(DetailView):
    model=Article
    template_name='article_detail.html'
    context_object_name='article'

    def get_queryset(self):
        return Article.objects.all()





# def home(request):
#     return render(request,'index.html')
# def article_detail(request):
#     return render(request,'article_detail.html')
def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
def profile(request):
    return render(request,'profile.html')
def article_form(request):
    return render(request,'article_form.html')
def personal(request):
    return render(request,'personal.html')
