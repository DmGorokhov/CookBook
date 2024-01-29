from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Product Name')
    times_cooked = models.IntegerField(default=0)
    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated_at"), auto_now=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(
        max_length=255, verbose_name='Recipe Name')
    products = models.ManyToManyField(
        Product, through='RecipeProduct', related_name='recipe_products'
    )

    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated_at"), auto_now=True)

    def __str__(self):
        return self.name


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

    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated_at"), auto_now=True)

    class Meta:
        unique_together = ('recipe', 'product',)
