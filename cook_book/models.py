from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Product Name')
    times_cooked = models.IntegerField(default=0)


class Recipe(models.Model):
    name = models.CharField(
        max_length=255, verbose_name='Recipe Name')
    products = models.ManyToManyField(
        Product, through='RecipeProduct', related_name='recipe_products'
    )


class RecipeProduct(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='recipe_products',
        verbose_name='Recipe'
    )
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT,
        related_name='products_in_recipe', verbose_name='Product'
    )
    weight = models.IntegerField(null=False)

    class Meta:
        unique_together = ('recipe', 'product',)
