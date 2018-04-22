from django.urls import path

from . import views

app_name = 'district'
urlpatterns = [
    path('store/', views.store, name='store'),
    path('create/', views.create, name='create')
]
