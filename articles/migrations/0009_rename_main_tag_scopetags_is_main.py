# Generated by Django 4.0.2 on 2022-02-24 00:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_alter_scopetags_article_alter_scopetags_tag_pk'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scopetags',
            old_name='main_tag',
            new_name='is_main',
        ),
    ]