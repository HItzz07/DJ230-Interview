# Generated by Django 5.0.4 on 2024-04-21 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0004_rename_book_id_reservation_book_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="circulation",
            name="return_date",
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="fulfilment_date",
            field=models.DateField(null=True),
        ),
    ]