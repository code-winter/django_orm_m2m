# Generated by Django 4.0.2 on 2022-02-24 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_tags_scopetags'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='scopes',
            field=models.ManyToManyField(related_name='tag', through='articles.ScopeTags', to='articles.Tags', verbose_name='Разделы'),
        ),
    ]
