from django.urls import path, include
from . import views
from .views import ProductView, FeedBackView, AuthRegister, LoginUser, AboutView
from .views import basket, basket_add, basket_delete, basket_edit, view_card_add, logout_user

app_name = 'shop_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('product', ProductView.as_view(), name='product'),
    path('view_card_add/<int:product_id>', view_card_add, name='view_card_add'),
    path('contact', FeedBackView.as_view(), name='contact'),
    path('register', AuthRegister.as_view(), name='register'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('basket', basket, name='basket'),
    path('basket_add/<int:product_id>', basket_add, name='basket_add'),
    path('basket_delete/<int:id>', basket_delete, name='basket_delete'),
    path('edit/<int:id>/<int:quantity>/', basket_edit, name='basket_edit'),
    path('about', AboutView.as_view(), name='about'),
]
