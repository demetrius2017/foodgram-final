from api.views import UserList, about_me
from django.urls import include, path
from rest_framework.routers import DefaultRouter

# , IngredientsViewSet, RecipeViewSet,
#                        TagsViewSet)

app_name = "api"

router = DefaultRouter()
# router.register('tags', TagsViewSet)
# router.register('ingredients', IngredientsViewSet)
# router.register('recipes', RecipeViewSet)
router.register("users/", UserList)

urlpatterns = [
    path("", include(router.urls)),
    path("", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
]
