from django.contrib import admin
from .models import PlanetarySystem, Planet, Star
from django.contrib.admin import RelatedOnlyFieldListFilter

@admin.register(Star)
class Star(admin.ModelAdmin):
    readonly_fields = ('get_planetary_system',)
#поля, которые будут отображаться в списке объектов
    list_display = ('id', 'name',  'is_published', 'get_planetary_system', 'status', 'aged')

#поля, которые будут ссылками на страницу редактирования
    list_display_links = ('id', 'name')

#поля, по которым можно будет фильтровать
    list_filter = [
        'status',
        ('planetary_system', RelatedOnlyFieldListFilter),]

#поля, по которым будет работать поиск
    search_fields = ('name', 'description', 'planetary_system')

#автоматическое заполнение слога на основе другого поля
    prepopulated_fields = {"slug": ("name",)}

#  специальный метод для отображения значения
    @staticmethod
    def get_planetary_system(obj):
        return ", ".join([ps.name for ps in obj.planetary_system.all()])
    get_planetary_system.short_description = 'Планетарные системы'

@admin.register(Planet)
class Planet(admin.ModelAdmin):

#поля, которые будут отображаться в списке объектов
    list_display = ('id', 'name',  'is_published', 'planetary_system', 'aged')

#поля, которые будут ссылками на страницу редактирования
    list_display_links = ('id', 'name')

#поля, по которым можно будет фильтровать
    list_filter = ('is_published', 'planetary_system')

#поля, по которым будет работать поиск
    search_fields = ('name', 'description', 'planetary_system')

#автоматическое заполнение слога на основе другого поля
    prepopulated_fields = {"slug": ("name",)}

@admin.register(PlanetarySystem)
class PlanetarySystemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

    