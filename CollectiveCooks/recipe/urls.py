from django.urls import path
from . import views

app_name = 'recipe'

urlpatterns = [
    path('add', views.add_recipe_view, name="add_recipe"),
]
