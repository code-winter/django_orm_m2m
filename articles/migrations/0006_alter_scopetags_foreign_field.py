# Generated by Django 4.0.2 on 2022-02-24 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_scopetags_foreign_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scopetags',
            name='foreign_field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='is_main', to='articles.tags', to_field='boolean_tags'),
        ),
    ]
