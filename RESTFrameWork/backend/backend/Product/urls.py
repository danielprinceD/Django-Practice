from django.urls import path
from .views import ProductDetail,ProductCreate,ProductListCreateAPIView

urlpatterns = [
     path('ViewData/<int:id>',ProductDetail.as_view()),
     path('CreateAPIView',ProductCreate.as_view()),
     path('CreateListView',ProductListCreateAPIView.as_view())
]
