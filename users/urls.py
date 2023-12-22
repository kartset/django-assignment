from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:test_id>/", views.getOne, name="getOne"),
    path("json/", views.getOneJSON, name="getOneJSON" ),
    path('create/', views.create, name='create'),

]