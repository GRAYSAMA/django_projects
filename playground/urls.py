from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.products),
    path('products/details/<int:id>', views.details, name='details')
]