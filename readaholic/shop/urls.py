from django.urls import path
from . import views 


urlpatterns = [
    path('', views.home, name = 'shop-home'),
    path('shop/<int:book_id>/', views.detail, name = 'detail')
]