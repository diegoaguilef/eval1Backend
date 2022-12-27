# Generated by Django 4.1.2 on 2022-12-27 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_user_address_user_commune_user_image_user_phone_and_more"),
        ("printers", "0005_shoppingcart"),
    ]

    operations = [
        migrations.AddField(
            model_name="shoppingcart",
            name="enabled",
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name="Sale",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("invoice", models.TextField(unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("shopping_carts", models.ManyToManyField(to="printers.shoppingcart")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sold_items",
                        to="users.user",
                    ),
                ),
            ],
            options={
                "ordering": ["created_at"],
            },
        ),
    ]