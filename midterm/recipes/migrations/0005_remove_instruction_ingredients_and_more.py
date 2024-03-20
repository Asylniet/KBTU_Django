# Generated by Django 4.2.1 on 2024-03-20 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0004_alter_instruction_ingredients"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="instruction",
            name="ingredients",
        ),
        migrations.AddField(
            model_name="instruction",
            name="ingredients",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="instructions",
                to="recipes.ingredient",
            ),
        ),
    ]