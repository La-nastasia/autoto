from django.urls import path
from apps.catalog.views import CategoryIndexView,ProductsByCategoryView,ProductsDetailView

urlpatterns = [
    path('',CategoryIndexView.as_view(),name='catalog'),
    path('<str:slug>/',ProductsByCategoryView.as_view(),name='categories'),
    path('product/<str:slug>/',ProductsDetailView.as_view(),name='product')
]