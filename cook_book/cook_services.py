from .models import RecipeProduct



def add_or_update_product_to_recipe(recipe_id, product_id, weight):
    RecipeProduct.objects.update_or_create(
        recipe_id=recipe_id,
        product_id=product_id,
        defaults={'weight': weight}
    )
