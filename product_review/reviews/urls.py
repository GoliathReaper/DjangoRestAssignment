from django.urls import path
from .views import (
    ProductListCreateView, ProductDetailView,
    ReviewCreateView, ProductReviewsListView
)

urlpatterns = [
    path('products/', ProductListCreateView.as_view()),
    path('products/<int:pk>/', ProductDetailView.as_view()),
    path('products/<int:product_id>/reviews/', ProductReviewsListView.as_view()),
    path('reviews/', ReviewCreateView.as_view()),
]
