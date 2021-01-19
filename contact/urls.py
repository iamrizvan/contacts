from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('new_contact/', views.new_contact, name='new_contact'),
    path('edit/<str:pk>/', views.edit, name='edit'),
    path('profile/<str:pk>/', views.profile, name='profile'),
    path('delete/<str:pk>/', views.delete, name='delete')
]
