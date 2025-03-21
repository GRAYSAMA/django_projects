from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('products/', views.products),
    path('products/details/<int:id>', views.details, name='details')
]