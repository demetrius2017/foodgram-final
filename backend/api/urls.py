from api.views import IngredientsViewSet, RecipesViewSet, TagsViewSet, UserList
from django.urls import include, path
from rest_framework.routers import DefaultRouter

app_name = "api"

router = DefaultRouter()
router.register("users", UserList)
router.register("tags", TagsViewSet)
router.register("ingredients", IngredientsViewSet)
router.register("recipes", RecipesViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
]
