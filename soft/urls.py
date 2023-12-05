from django.urls import path
from . import views

urlpatterns = [path("", views.drinks_list), path('<int:id>', views.drinks_detail)]
