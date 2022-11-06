from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import ProductModel, CategoryModel, FeedBackModel, UserDressModel, Basket
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'image_show', 'size', 'description', 'price', 'colour')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description', 'size')
    list_filter = ('name', 'price', 'size', 'colour')
    prepopulated_fields = {'slug': ('name', )}

    def image_show(self, obj):      # Добавление миниатюры картинки в админке
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return "None"

    image_show.__name__ = "Картинка"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class FeedBackAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'message')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('name', 'email')


class UserDressAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone', 'first_name', 'last_name', 'is_staff')
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "middle_name", "email")}),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions"),
                            }),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
        (_("Info"), {"fields": ("phone", "avatar", "gender")}),
    )


admin.site.register(ProductModel, ProductAdmin)
admin.site.register(CategoryModel, CategoryAdmin)
admin.site.register(FeedBackModel, FeedBackAdmin)
admin.site.register(UserDressModel, UserDressAdmin)
admin.site.register(Basket)
