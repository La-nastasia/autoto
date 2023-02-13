from django.urls import path
from apps.api.catalog.views import ProductListView, ProductDetailView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView, CategoryDetailView, CategoryListView, \
    CategoryCreateView, CategoryUpdateView, CategoryDeleteView

urlpatterns = [
    path('', CategoryListView.as_view()),
    path('<int:pk>/', CategoryDetailView.as_view()),
    path('create/', CategoryCreateView.as_view()),
    path('update/<int:pk>/', CategoryUpdateView.as_view()),
    path('delete/<int:pk>/', CategoryDeleteView.as_view()),
    path('product/', ProductListView.as_view()),
    path('product/<int:pk>/', ProductDetailView.as_view()),
    path('product/create/', ProductCreateView.as_view()),
    path('product/update/<int:pk>/', ProductUpdateView.as_view()),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view()),
]