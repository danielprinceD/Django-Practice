from django.urls import path
from .views import ProductDetail

urlpatterns = [
     path('ViewData/<int:id>',ProductDetail.as_view())
]
