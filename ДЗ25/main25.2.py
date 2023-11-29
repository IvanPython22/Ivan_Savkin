class Recipe:
    def __init__(self, name, author, recipe_type, description, video_link, ingredients, cuisine):
        self.name = name
        self.author = author
        self.recipe_type = recipe_type
        self.description = description
        self.video_link = video_link
        self.ingredients = ingredients
        self.cuisine = cuisine

    def get_name(self):
        return self.name

    def get_author(self):
        return self.author

    def get_recipe_type(self):
        return self.recipe_type

    def get_description(self):
        return self.description

    def get_video_link(self):
        return self.video_link

    def get_ingredients(self):
        return self.ingredients

    def get_cuisine(self):
        return self.cuisine

    def set_name(self, name):
        self.name = name

    def set_author(self, author):
        self.author = author

    def set_recipe_type(self, recipe_type):
        self.recipe_type = recipe_type

    def set_description(self, description):
        self.description = description

    def set_video_link(self, video_link):
        self.video_link = video_link

    def set_ingredients(self, ingredients):
        self.ingredients = ingredients

    def set_cuisine(self, cuisine):
        self.cuisine = cuisine


class RecipeModel:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def remove_recipe(self, recipe):
        self.recipes.remove(recipe)

    def get_all_recipes(self):
        return self.recipes


class RecipeView:
    @staticmethod
    def display_recipe(recipe):
        return f'Название рецепта: {recipe.get_name()}\n' \
               f'Автор рецепта: {recipe.get_author()}\n' \
               f'Тип рецепта: {recipe.get_recipe_type()}\n' \
               f'Описание: {recipe.get_description()}\n' \
               f'Ссылка на видео: {recipe.get_video_link()}\n' \
               f'Ингредиенты: {", ".join(recipe.get_ingredients())}\n' \
               f'Кухня: {recipe.get_cuisine()}\n'

    def display_recipes(self, recipes):
        for recipe in recipes:
            print(self.display_recipe(recipe))


class RecipeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_recipe(self, recipe):
        self.model.add_recipe(recipe)

    def remove_recipe(self, recipe):
        self.model.remove_recipe(recipe)

    def print_all_recipes(self):
        recipes = self.model.get_all_recipes()
        self.view.display_recipes(recipes)


recipe1 = Recipe('Паста Карбонара', 'Итальянский Шеф', 'Второе блюдо', 'Очень вкусная паста', 'youtube.com',
                 ['Спагетти', 'Бекон', 'Яйца', 'Сыр Пармезан'], 'Итальянская')
recipe2 = Recipe('Бефстроганов', 'Шеф Повар Вася', 'Горячее блюдо', 'Популярное блюдо из говядины', 'youtube.com',
                 ['Говядина', 'Лук', 'Сыр', 'Сметана', 'Картофель'], 'Русская')
recipe3 = Recipe('Салат Цезарь', 'Французский Эмильен', 'Холодное блюдо', 'Изысканный салат', 'youtube.com',
                 ['Копченая курица', 'Яйца', 'Листья салата', 'Сыр', 'Помидоры черри'], 'Французская')

model = RecipeModel()
view = RecipeView()
controller = RecipeController(model, view)

controller.add_recipe(recipe1)
controller.add_recipe(recipe2)
controller.add_recipe(recipe3)

controller.print_all_recipes()
