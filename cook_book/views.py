from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404, render

from .models import Recipe, Product
from .cook_services import (add_or_update_product_to_recipe,
                            get_recipe_products,
                            increment_products_times_cooked,
                            find_recipes_withount_product)

from .utils import handle_db_errors
from .ParamsSchemas import RecipeParams, OnlyRecipeID, OnlyProductID


class HomeView(TemplateView):
    template_name = 'home.html'


@handle_db_errors
@require_http_methods(['GET'])
def add_product_to_recipe(request):
    new_recipe_params = RecipeParams(**request.GET.dict())
    add_or_update_product_to_recipe(**new_recipe_params.dict())

    return HttpResponse('Product added to recipe successfully.', status=200)


@handle_db_errors
@require_http_methods(['GET'])
def cook_recipe(request):
    recipe_id = OnlyRecipeID(**request.GET.dict()).recipe_id
    recipe = get_object_or_404(Recipe, id=recipe_id)

    recipe_products_ids = get_recipe_products(recipe)
    increment_products_times_cooked(recipe_products_ids)
    return HttpResponse("Recipe has been cooked.")


@handle_db_errors
@require_http_methods(['GET'])
def show_recipes_without_product(request):
    product_id = OnlyProductID(**request.GET.dict()).product_id
    product = get_object_or_404(Product, id=product_id)

    recipes = find_recipes_withount_product(product_id)

    context = {'recipes': recipes,
               'product_name': product.name}
    return render(request, 'recipes_index_without_product.html', context)
