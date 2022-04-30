from django.contrib import admin

from meetups.models import Tag, Meetup


@admin.register(Meetup)
class MeetupAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date', 'place')
    list_display_links = ('name', 'description')
    filter_horizontal = ('tags', 'lecturers', 'users')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
