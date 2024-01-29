from django.urls import path
from .views import(
     ProductDetail,
     ProductCreate,
     ProductListCreateAPIView,
     ProductListAPI,
     ProductUpdateAPI,
     ProductDestroyAPI
)
from .views import product_mixin_generic_view
urlpatterns = [
     path('ViewData/<int:id>',ProductDetail.as_view()),
     path('CreateAPIView',ProductCreate.as_view()),
     path('CreateListView',ProductListCreateAPIView.as_view()),
     path('ListAPI',ProductListAPI.as_view()),
     path('Update/<int:pk>',ProductUpdateAPI.as_view()),
     path("Destroy/<int:id>",ProductDestroyAPI.as_view()),
     path('list_mixin',product_mixin_generic_view)
]
