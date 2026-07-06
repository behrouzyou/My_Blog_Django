from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
  fieldsets = (
      (None, {
          "fields": ('username','password'

          )
      }),('اطلاعات شخصی',{'fields':('frist_name','last_name','email','bio')}),
      ('دسترسی ها',{'fields':('is_active','is_staff','is_superuser','groups','user_permissions')})
      ,('تاریخ های مهم',{'fields':('data_joined','last_login')}),
  )
  list_display=('email','username','first_name','last_name','is_staff')
  search_fields=('email','username','first_name','last_name')
  list_filter=('is_staff','is_superuser','is_active','groups')
  ordering=('email',)

admin.site.register(CustomUser,CustomUserAdmin)
