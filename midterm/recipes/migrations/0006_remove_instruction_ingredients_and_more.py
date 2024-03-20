# Generated by Django 4.2.1 on 2024-03-20 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0005_remove_instruction_ingredients_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="instruction",
            name="ingredients",
        ),
        migrations.AddField(
            model_name="instruction",
            name="ingredients",
            field=models.ManyToManyField(
                related_name="instructions", to="recipes.ingredient"
            ),
        ),
    ]