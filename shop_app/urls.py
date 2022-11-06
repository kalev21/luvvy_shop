from django.urls import path, include
from . import views
from .views import ProductView, FeedBackView, AuthRegister, LoginUser, logout_user, basket
from .views import basket_add, basket_delete

app_name = 'shop_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('product', ProductView.as_view(), name='product'),
    path('contact', FeedBackView.as_view(), name='contact'),
    path('register', AuthRegister.as_view(), name='register'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('basket', basket, name='basket'),
    path('basket_add/<int:product_id>', basket_add, name='basket_add'),
    path('basket_delete/<int:id>', basket_delete, name='basket_delete'),
]
