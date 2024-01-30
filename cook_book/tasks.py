from celery import shared_task
from .cook_services import increment_products_times_cooked, get_recipe_products


@shared_task
def update_products_times_cooked(recipe_id: int):
    recipe_products_ids = get_recipe_products(recipe_id)
    increment_products_times_cooked(recipe_products_ids)
