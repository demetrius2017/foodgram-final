from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(
        "Email",
        max_length=200,
        unique=True,
    )
    first_name = models.CharField("Имя", max_length=150)
    last_name = models.CharField("Фамилия", max_length=150)
    shopping_cart = models.OneToOneField(
        "recipes.ShoppingCart", on_delete=models.SET_NULL, null=True
    )
    favorite_recipes = models.ManyToManyField(
        "recipes.Recipe", related_name="favorited_by_users"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ("id",)

    def __str__(self):
        return self.email
