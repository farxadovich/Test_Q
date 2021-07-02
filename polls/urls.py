from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from polls.views import index, savollar, check


urlpatterns = [
    path('', index, name='index'),
    path('questions/<int:category_id>', savollar, name='questions'),
    path('questions/check/', check, name='check')
]