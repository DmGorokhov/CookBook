from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from .cook_services import add_or_update_product_to_recipe


@require_http_methods(['GET'])
def add_product_to_recipe(request):
    recipe_id = request.GET.get('recipe_id')
    product_id = request.GET.get('product_id')
    weight = request.GET.get('weight')

    add_or_update_product_to_recipe(recipe_id, product_id, weight)
    return HttpResponse('Product added to recipe successfully.', status=200)


def cook_recipe(request):
    pass


def show_recipes_without_product(request):
    pass
