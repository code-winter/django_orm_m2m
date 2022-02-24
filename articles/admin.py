from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tags, ScopeTags


class ScopesInlineFormset(BaseInlineFormSet):
    def clean(self):
        flag = False
        for form in self.forms:
            data = form.cleaned_data
            if data:
                if data['is_main'] and not flag:
                    flag = True
                elif data['is_main'] and flag:
                    raise ValidationError('Должен быть только один основной раздел!')
        if not flag:
            raise ValidationError('Укажите основной раздел')
        return super().clean()


class ScopesInline(admin.TabularInline):
    model = ScopeTags
    formset = ScopesInlineFormset
    verbose_name = 'Раздел'
    verbose_name_plural = 'Разделы'


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    fields = ['name']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = ['title', 'published_at']
    inlines = [ScopesInline, ]
