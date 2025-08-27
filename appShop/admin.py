from django.contrib import admin
from unfold.admin import ModelAdmin
from appShop.models import *
from unfold.contrib.filters.admin import SliderNumericFilter,  AllValuesCheckboxFilter
from unfold.contrib.forms.widgets import WysiwygWidget


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }
    autocomplete_fields = ['category']

    list_display = ['title', 'category', 'price']
    list_display_links = ['title', 'category', 'price']
    search_fields = ['title', 'description']

    list_filter = [
        ('price', SliderNumericFilter),
        ('category__title', AllValuesCheckboxFilter)
    ]
    list_filter_sheet = False
    list_filter_submit = True


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ['title', 'position']
    list_display_links = ['title', 'position']
    search_fields = ['title']

    list_filter = [
        ('position', SliderNumericFilter)
    ]

    list_filter_sheet = False
    list_filter_submit = True
