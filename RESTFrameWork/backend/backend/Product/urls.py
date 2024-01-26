from django.urls import path
from .views import ProductDetail,ProductCreate

urlpatterns = [
     path('ViewData/<int:id>',ProductDetail.as_view()),
     path('CreateAPIView',ProductCreate.as_view())
]
