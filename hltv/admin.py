from django.contrib import admin
from .models import *


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("first","last")}
    list_display =['nickname','age','country','rating']
    list_filter = ['current_team']


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display =['title']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display =['name']


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display =['team1', 'team2']

@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin):
    list_display =['name']

@admin.register(UserAddon)
class UserAddonAdmin(admin.ModelAdmin):
    pass


@admin.register(MatchComment)
class MatchCommentAdmin(admin.ModelAdmin):
    list_display = ['text','match']