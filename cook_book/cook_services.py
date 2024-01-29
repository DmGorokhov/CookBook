from django.db.models import F, Q

from .models import RecipeProduct, Recipe, Product


def add_or_update_product_to_recipe(recipe_id, product_id, weight):
    RecipeProduct.objects.update_or_create(
        recipe_id=recipe_id,
        product_id=product_id,
        defaults={'weight': weight}
    )


def get_recipe_products(recipe: Recipe):
    recipe_products = (RecipeProduct.objects.filter(recipe=recipe).
                       prefetch_related('product').
                       values_list('product__id', flat=True))
    return recipe_products


def increment_products_times_cooked(products_id: list[id]):
    (Product.objects.filter(id__in=products_id).
     update(times_cooked=F('times_cooked') + 1))


def find_recipes_withount_product(product_id: int):
    min_weight_for_accounting = 10  # grams
    recipes_without_product = Recipe.objects.filter(
        ~Q(recipe_products__product__id=product_id) | Q(recipe_products__weight__lt=min_weight_for_accounting)  # noqa E501
    )
    return recipes_without_product
