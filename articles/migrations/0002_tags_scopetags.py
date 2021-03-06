# Generated by Django 4.0.2 on 2022-02-24 00:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Раздел',
                'verbose_name_plural': 'Разделы',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ScopeTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_tag', models.BooleanField(default=False, verbose_name='Основной?')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='primary_art', to='articles.article', verbose_name='Статья')),
                ('tag_pk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='primary_tags', to='articles.tags', verbose_name='Раздел')),
            ],
        ),
    ]
