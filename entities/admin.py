from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Entity, Hero, Origin, Villian

admin.site.register(Category)
# admin.site.register(Entity)
# admin.site.register(Hero)
# admin.site.register(Origin)
admin.site.register(Villian)


@admin.register(Origin)
class OriginAdmin(admin.ModelAdmin):
    list_display = ("name", 'hero_count', 'villain_count',)
    list_per_page = 1
    # date_hierarchy = 'added_on'

    # list_displa = [field.name for field in Origin._meta.get_fields()]
    # print(list_displa)

    def hero_count(self, obj):
        return obj.hero_set.count()

    def villain_count(self, obj):
        return obj.villian_set.count()


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'headshot', 'headshot_image',)
    # readonly_fields = ['not_editable_field', 'father', 'mother', 'spouse',]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["name", "alternative_name", "father", "mother", "spouse", "not_editable_field",]
        else:
            return ["father", "mother", "spouse", "not_editable_field",]
    # exclude = ['father', 'mother', 'spouse',]

    def headshot_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.headshot.url,
            # width=obj.headshot.width,
            width=50,
            # height=obj.headshot.height,
            height=40,
        )
    )
