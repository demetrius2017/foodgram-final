from api.views import (
    AddAndDeleteSubscribe,
    AddDeleteFavoriteRecipe,
    AddDeleteShoppingCart,
    IngredientsViewSet,
    RecipesViewSet,
    TagsViewSet,
    Tokens,
    UsersViewSet,
    set_password,
)
from django.urls import include, path
from rest_framework.routers import DefaultRouter

app_name = "api"

router = DefaultRouter()
router.register("users", UsersViewSet)
router.register("tags", TagsViewSet)
router.register("ingredients", IngredientsViewSet)
router.register("recipes", RecipesViewSet)


# Аутентификация
auth_patterns = [
    path("auth/token/login/", Tokens.as_view(), name="login"),
    path("users/set_password/", set_password, name="set_password"),
    path("", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
]

# Работа с рецептами и подписками
recipe_patterns = [
    path(
        "users/<int:user_id>/subscribe/",
        AddAndDeleteSubscribe.as_view(),
        name="subscribe",
    ),
    path(
        "recipes/<int:recipe_id>/favorite/",
        AddDeleteFavoriteRecipe.as_view(),
        name="favorite_recipe",
    ),
    path(
        "recipes/<int:recipe_id>/shopping_cart/",
        AddDeleteShoppingCart.as_view(),
        name="shopping_cart",
    ),
]

urlpatterns = [
    *auth_patterns,
    *recipe_patterns,
    path("", include(router.urls)),
]
