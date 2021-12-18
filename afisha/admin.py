from django.contrib import admin
from django.contrib.auth.models import Group, User

from .models import *

admin.site.register(Genre)
admin.site.site_header = 'Кинотеатр | ABOBA CINEMA'


class ShowInline(admin.StackedInline):
    model = Show
    extra = 1


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('film_title', 'film_year', 'get_film_age_limit_str', 'is_film_in_rent')
    list_filter = ('film_age_limit',)
    inlines = (ShowInline,)


@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = ('show_date', 'show_film',)


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review_author', 'review_text', 'review_film')


admin.site.unregister(Group)
admin.site.unregister(User)
