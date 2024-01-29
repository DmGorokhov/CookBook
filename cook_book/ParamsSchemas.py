from pydantic import BaseModel


class RecipeParams(BaseModel):
    recipe_id: int
    product_id: int
    weight: int


class OnlyRecipeID(BaseModel):
    recipe_id: int


class OnlyProductID(BaseModel):
    product_id: int
