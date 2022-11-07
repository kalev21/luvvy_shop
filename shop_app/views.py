from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from .utils import DataMixin
from .forms import FeedBackForm, RegisterUserForm, LoginUserForm
from .models import ProductModel, Basket
from django.http import JsonResponse
from django.template.loader import render_to_string

from django.views.generic import ListView, View, CreateView


def index(request):
    return render(request, 'shop_app/index.html')


class ProductView(ListView):
    model = ProductModel
    template_name = 'shop_app/product.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return ProductModel.objects.order_by('-id')


class FeedBackView(View):
    def get(self, request):
        form = FeedBackForm()
        return render(request, 'shop_app/contact.html', context={'form': form})

    def post(self, request):
        bound_form = FeedBackForm(request.POST)
        if bound_form.is_valid():
            bound_form.save()
        return render(request, 'shop_app/contact.html', context={'form': bound_form})


class AuthRegister(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'shop_app/auth/register.html'
    success_url = reverse_lazy('shop_app:login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context |= self.get_user_context(title='Регистрация')
        return context


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'shop_app/auth/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context |= self.get_user_context(title='Авторизация')
        return context

    def get_success_url(self):
        return reverse_lazy('shop_app:product')


def logout_user(request):
    logout(request)
    return redirect('shop_app:product')


@login_required
def basket(request):
    basket_items = Basket.objects.filter(user=request.user).order_by('product__category')
    context = {
        'products': basket_items,
        'baskets': Basket.objects.filter(user=request.user)
    }
    return render(request, 'shop_app/basket.html', context)


@login_required
def basket_add(request, product_id=None):
    """Добавление товаров в Корзину"""

    product = ProductModel.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        cart = Basket(user=request.user, product=product)
        cart.quantity = 1
        cart.save()
        return HttpResponseRedirect(reverse('shop_app:product'))
    else:
        cart = baskets.first()
        cart.quantity += 1
        cart.save()
        return HttpResponseRedirect(reverse('shop_app:product'))


@login_required
def basket_delete(request, id=None):
    """Удаление товаров из корзины"""

    cart = Basket.objects.get(id=id)
    cart.delete()
    return HttpResponseRedirect(reverse('shop_app:basket'))


def basket_edit(request, id, quantity):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        cart = Basket.objects.get(id=id)
        if quantity > 0:
            cart.quantity = quantity
            cart.save()
        else:
            cart.delete()
        products = Basket.objects.filter(user=request.user)
        context = {'products': products}
        result = render_to_string('shop_app/basket.html', context)
        return JsonResponse({'result': result})



