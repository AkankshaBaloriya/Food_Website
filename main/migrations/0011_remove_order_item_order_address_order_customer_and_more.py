# Generated by Django 4.1.5 on 2023-09-05 11:47

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0010_remove_order_customer"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="item",
        ),
        migrations.AddField(
            model_name="order",
            name="address",
            field=models.CharField(default="", max_length=200),
        ),
        migrations.AddField(
            model_name="order",
            name="customer",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="main.customer",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="date",
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.AddField(
            model_name="order",
            name="phone",
            field=models.CharField(default="", max_length=15),
        ),
        migrations.AddField(
            model_name="order",
            name="product",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="main.food_item",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="quantity",
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name="order",
            name="price",
            field=models.IntegerField(),
        ),
    ]
