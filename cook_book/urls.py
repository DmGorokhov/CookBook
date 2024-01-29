from django.contrib import admin
from django.urls import path

from .views import (add_product_to_recipe, cook_recipe,
                    show_recipes_without_product, HomeView)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add_product_to_recipe/', add_product_to_recipe,
         name='put_product_to_recipe'),
    path('run_cook_recipe/', cook_recipe, name='run_cook_recipe'),
    path('recipes_without_product', show_recipes_without_product,
         name='recipes_without_product'),
    path('admin/', admin.site.urls),
]
