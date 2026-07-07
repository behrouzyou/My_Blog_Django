from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        fields=['title','content','category','image','tags','status']

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'یک عنوان انتخاب کنید'}),
            'content':forms.Textarea(attrs={'class':'form-control','row':10}),
            'category':forms.Select(attrs={'class':'form-control'}),
            'image':forms.ClearableFileInput(attrs={'class':'form-control'}),
            'tags':forms.TextInput(attrs={'class':'form-control','placeholder':'برچسب را با کاما جدا کنید'}),
            'status':forms.Select(attrs={'class':'form-control'}),
        }
