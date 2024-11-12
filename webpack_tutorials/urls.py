from django.urls import path
from . import views

urlpatterns = [
    path('core', views.webpack_index, name='webpack_index'),
]