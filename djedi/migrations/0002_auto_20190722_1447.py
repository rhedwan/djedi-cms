# Generated by Django 2.2.3 on 2019-07-22 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("djedi", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="node",
            name="is_published",
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
