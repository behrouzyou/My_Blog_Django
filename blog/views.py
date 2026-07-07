from django.shortcuts import render
from .models import Article,Category
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .forms import ArticleForm
from django.urls import reverse_lazy
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

class ArticleCreateView(LoginRequiredMixin,CreateView):
    model=Article
    form_class=ArticleForm
    template_name='article_form.html'
    success_url=reverse_lazy('home')

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model:Article
    form_class=ArticleForm
    template_name='article_form.html'
    success_url=reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        article=self.get_object()
        return self.request.user == article.author
    def get_queryset(self):
        return Article.objects.all()
class ArticleDeleteView(LoginRequiredMixin,DeleteView,UserPassesTestMixin):
    model=Article
    template_name='article_confirm_delete.html'
    success_url=reverse_lazy('home')

    def test_func(self):
        article=self.get_object()
        return self.request.user==article.author

# def article_form(request):
#     return render(request,'article_form.html')
def personal(request):
    return render(request,'personal.html')
