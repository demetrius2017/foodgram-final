# Generated by Django 3.2.3 on 2023-08-03 17:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '__first__'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('id',), 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AddField(
            model_name='user',
            name='favorite_recipes',
            field=models.ManyToManyField(related_name='favorited_by_users', to='recipes.Recipe'),
        ),
        migrations.AddField(
            model_name='user',
            name='shopping_cart',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_user', to='recipes.shoppingcart'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=200, unique=True, verbose_name='Email'),
        ),
    ]
