from django.contrib import admin
from .models import Question, Choice,Category,Product


# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Category)
admin.site.register(Product)
admin.site.site_header = 'webbanhang'
