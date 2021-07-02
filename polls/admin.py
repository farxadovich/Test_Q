from django.contrib import admin
from polls.models import Questions, Category, Choice


admin.site.register(Questions)
admin.site.register(Category)
admin.site.register(Choice)