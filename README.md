
___
[![Maintainability](https://api.codeclimate.com/v1/badges/984f8ea6bf922dd167bc/maintainability)](https://codeclimate.com/github/DmGorokhov/CookBook/maintainability)

### Main project stack:
* Django4.2.3, Pydantic2.6, gunicorn

___
### 1. Description
The cookbook project is a small django-application.
___
### 2. Requirements
___
* Python > 3.10
* Django > 4.2
* Poetry >1.2.2
* Make (is used to run shortcut console-command)

**Poetry** is setup by the commands:

**Linux, macOS, Windows (WSL):**

```bash
curl -sSL https://install.python-poetry.org | python3 -
```
Details on installing and using the **Poetry** package are available in [official documentation](https://python-poetry.org/docs/).
To install **Poetry** you need **Python 3.7+** use the information from the official website [python.org](https://www.python.org/downloads/)

---

### 3. Installation

Cloning the repository

```bash
git clone git@github.com:DmGorokhov/CookBook.git
cd CookBook
```

Activate virtual environment

```bash
poetry shell
```
Create .env file and set environment variables using file .env.example as example.
For development purposes you can leave these variables as suggested in example.
If you would like leave example variables (do it only for developer and check purposes) type in terminal:**
```commandline
mv .env.example .env
```

Setup app
```bash
make setup
```
___
### 4. Usage

```
make dev  # starts  web developer server
```

1. Open your browser at http://127.0.0.1:8000/admin.
   In the admin panel you can manage products and recipes. 
  

2. http://localhost:8000/add_product_to_recipe with query params recipe_id, product_id, weight
Adds a specified product with a specified weight to the specified recipe.   
If the recipe already contains product, the view changes its weight in this recipe to the specified weight.
Full request look like *http://localhost:8000/add_product_to_recipe?recipe_id=1&product_id=2&weight=70*  
Request example in terminal with curl:
```
curl -X GET 'http://localhost:8000/add_product_to_recipe?recipe_id=1&product_id=2&weight=70'
```

3. http://localhost:8000/run_cook_recipe with query parameter recipe_id
Increases by one the number of prepared meals for each product in the specified recipe.
Full request look like *http://localhost:8000/run_cook_recipe?recipe_id=1*  
Request example in terminal with curl:
```
curl -X GET 'http://localhost:8000/run_cook_recipe?recipe_id=1'
```
4. http://localhost:8000/recipes_without_product with query parameter product_id
Render HTML page with a table of all recipes in which the specified product is absent or  
present in an amount less than 10 grams. 
Full request look like *http://localhost:8000/recipes_without_product?product_id=1*  
Request example in terminal with curl:
```
curl -X GET 'http://localhost:8000/recipes_without_product?product_id=1'
```
