from django.urls import path
from . import views


urlpatterns = [
    path('' , views.home , name="home" ),
    path('<int:post_id>/' , views.blog_details , name='details_page'),
    path('new_url/' , views.new_url, name="new_url_page"),
    path('deprecated_url/' , views.deprecated_url, name="deprecated_url_page"),
]