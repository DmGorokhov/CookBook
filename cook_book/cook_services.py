from django.db.models import F

from .models import RecipeProduct, Recipe, Product


def add_or_update_product_to_recipe(recipe_id, product_id, weight):
    RecipeProduct.objects.update_or_create(
        recipe_id=recipe_id,
        product_id=product_id,
        defaults={'weight': weight}
    )


def get_recipe_products(recipe: Recipe):
    recipe_products = (RecipeProduct.objects.filter(recipe=recipe).
                       prefetch_related('product').values_list('product__id', flat=True))
    return recipe_products


def increment_products_times_cooked(products_id: list[id]):
    Product.objects.filter(id__in=products_id).update(times_cooked=F('times_cooked') + 1)
