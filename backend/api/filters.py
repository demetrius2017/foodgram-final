import django_filters as filters
from django.forms.widgets import CheckboxInput
from recipes.models import Ingredient, Recipe
from users.models import User


# Фильтр для ингредиентов
class IngredientFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr="istartswith")

    class Meta:
        model = Ingredient
        fields = ("name",)


# Фильтр для рецептов
class RecipeFilter(filters.FilterSet):
    author = filters.ModelChoiceFilter(queryset=User.objects.all())
    is_in_shopping_cart = filters.BooleanFilter(
        widget=CheckboxInput(), label="В корзине."
    )
    is_favorited = filters.BooleanFilter(
        widget=CheckboxInput(), label="В избранных."
    )
    tags = filters.AllValuesMultipleFilter(
        field_name="tags__slug", label="Ссылка"
    )

    class Meta:
        model = Recipe
        fields = ["is_favorited", "is_in_shopping_cart", "author", "tags"]
