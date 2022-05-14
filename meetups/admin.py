from django.contrib import admin

from meetups.models import Tag, Meetup, Lecture
from maps.admin import MeetupMarkerInline


@admin.register(Meetup)
class MeetupAdmin(admin.ModelAdmin):
    inlines = (MeetupMarkerInline,)
    fieldsets = (
        ('Важная информация', {'fields': ('name', 'description', 'date', 'place')}),

        ('Дополнительная информация', {'fields': ('website', 'tags', 'is_visible'), }),

        ('Люди', {'fields': ('owner', 'users')}),
    )
    list_display = ('name', 'description', 'date', 'place')
    list_display_links = ('name', 'description')
    filter_horizontal = ('tags', 'users',)


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ('name', 'meetup')
    list_display_links = ('name',)
    filter_horizontal = ('lectors',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
