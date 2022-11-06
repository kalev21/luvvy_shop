from django.core.cache import cache
from .models import CategoryModel


class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs) -> dict:
        context = kwargs

        product = cache.get('product')

        if not product:
            product = CategoryModel.objects.all()
            cache.set('product', product, 60)

        context['product'] = product
        return context
