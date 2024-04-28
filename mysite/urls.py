from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView
from .forms import *


urlpatterns = [
    path('', home),
    path('item/add/<int:id>/', add_to_cart, name='add_item'),
    path('item/delete/', clear_cart, name='clear_cart'),
    path('basket/', cart_view, name='cart'),
    path('product/', product_detail, name='product_detail'),
    path('category/<int:id>', category_detail, name='category_detail'),
    path('create/order/', create_order, name='create_order'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('panel/', panel),
    path('logout/', logout_user),
    path('order-detail/<int:id>/', order_detail),
    path('accounts/profile/', redirect_home),
]
