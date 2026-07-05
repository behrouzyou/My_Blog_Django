from django.shortcuts import render

def home(request):
    return render(request,'index.html')
def article_detail(request):
    return render(request,'article_detail.html')
def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
def profile(request):
    return render(request,'profile.html')
def article_form(request):
    return render(request,'article_form.html')
