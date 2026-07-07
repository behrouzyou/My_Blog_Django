from django.shortcuts import render,redirect,
from .models import Article,Category
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .forms import ArticleForm,CommentForm
from django.urls import reverse_lazy,reverse
from django.contrib import messages

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
        return Article.published.all()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.filter(active=True)
        context['comment_form'] = CommentForm()
        return context


    def post(self,request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect('account_login')
        self.object=self.get_object()
        form=CommentForm(request.POST)

        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.article=self.object
            new_comment.author=request.user
            new_comment.save()
            messages.success(request, 'نظر شما پس از تایید منتشر میشود.')
            return redirect(reverse('article_detail',kwargs={'slug':self.object.slug}))
        else:
            context=self.get_context_data(**kwargs)
            context['comment_form']=form
            return self.render_to_response(context)




# def home(request):
#     return render(request,'index.html')
# def article_detail(request):
#     return render(request,'article_detail.html')
def login(request):
    return render(request,'accounts/login.html')
def signup(request):
    return render(request,'accounts/signup.html')


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
