from django.db import models
from taggit.managers import TaggableManager
from django.conf import settings
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100,unique=True,verbose_name='نام دسته بندی')
    slug = models.SlugField(max_length=100,unique=True,allow_unicode=True,blank=True)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name,allow_unicode=True)
        super().save(*args,**kwargs)
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

class Article(models.Model):
    STATUS_CHOICES = [
        ('draft','پیش نویس'),
        ('published','منتشر شده'),
    ]
    title = models.CharField(max_length=200,verbose_name='عنوان مقاله')
    slug = models.SlugField(max_length=200,unique=True,allow_unicode=True,blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,verbose_name='نویسنده',related_name='articles')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True,verbose_name='دسته بندی')
    content = models.TextField(verbose_name='محتوا')
    image = models.ImageField(upload_to='articles/%Y%m%d/',null=True,blank=True,verbose_name='تصویر شاخص')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='تاریخ بروزرسانی')
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft',verbose_name='وضعیت')
    tags = TaggableManager(verbose_name='برچسب ها')

    def __str__(self):
        return self.title
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title,allow_unicode=True)
        super().save(*args,**kwargs)
    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        ordering = ['-created_at']
