from django.contrib import admin

from .models import (
    FavoriteRecipe,
    Ingredient,
    Recipe,
    RecipeIngredient,
    RecipeTag,
    ShoppingCart,
    Subscribe,
    Tag,
)

EMPTY_MSG = "-пусто-"


class RecipeTagAdmin(admin.StackedInline):
    model = RecipeTag
    autocomplete_fields = ("tag",)


class RecipeIngredientAdmin(admin.StackedInline):
    model = RecipeIngredient
    autocomplete_fields = ("ingredient",)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "get_author",
        "name",
        "text",
        "cooking_time",
        "get_tags",
        "get_ingredients",
        "pub_date",
        "get_favorite_count",
    )
    search_fields = (
        "name",
        "cooking_time",
        "author__email",
        "ingredients__name",
    )
    list_filter = (
        "pub_date",
        "tags",
    )
    inlines = (
        RecipeTagAdmin,
        RecipeIngredientAdmin,
    )
    empty_value_display = EMPTY_MSG

    @admin.display(description="Электронная почта автора")
    def get_author(self, obj):
        return obj.author.email

    @admin.display(description="Тэги")
    def get_tags(self, obj):
        list_ = [_.name for _ in obj.tags.all()]
        return ", ".join(list_)

    @admin.display(description=" Ингредиенты ")
    def get_ingredients(self, obj):
        return "\n ".join(
            [
                f"{_.ingredient.name} - {_.amount} "
                f"{_.ingredient.measurement_unit}."
                for _ in obj.recipe.all()
            ]
        )

    @admin.display(description="В избранном")
    def get_favorite_count(self, obj):
        return obj.favorite_recipe.count()


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "color",
        "slug",
    )
    search_fields = (
        "name",
        "slug",
    )
    empty_value_display = EMPTY_MSG


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "measurement_unit",
    )
    search_fields = (
        "name",
        "measurement_unit",
    )
    empty_value_display = EMPTY_MSG


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "follower",
        "following",
        "created",
    )
    search_fields = (
        "follower__email",
        "following__email",
    )
    empty_value_display = EMPTY_MSG


@admin.register(FavoriteRecipe)
class FavoriteRecipeAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "get_recipe", "get_count")
    empty_value_display = EMPTY_MSG

    @admin.display(description="Рецепты")
    def get_recipe(self, obj):
        return [_.name for _ in obj.recipe.all()[:5]]

    @admin.display(description="В избранных")
    def get_count(self, obj):
        return obj.recipe.count()


@admin.register(ShoppingCart)
class SoppingCartAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "get_recipe", "get_count")
    empty_value_display = EMPTY_MSG

    @admin.display(description="Рецепты")
    def get_recipe(self, obj):
        return [_.name for _ in obj.recipe.all()]

    @admin.display(description="В избранных")
    def get_count(self, obj):
        return obj.recipe.count()
