# Generated by Django 4.0.2 on 2022-02-24 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_alter_article_scope'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='scope',
            field=models.ManyToManyField(related_name='tag', through='articles.ScopeTags', to='articles.Tags', verbose_name='Разделы'),
        ),
        migrations.AlterField(
            model_name='scopetags',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.article', verbose_name='Статья'),
        ),
        migrations.AlterField(
            model_name='scopetags',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.tags', verbose_name='Раздел'),
        ),
    ]
