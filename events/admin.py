# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Event, Comment, Tag


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_display = 'name', 'author'
    search_fields = 'name', 'author__username'
    list_filter = 'is_archive',


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = 'text','created', 'author'
    search_fields = 'created', 'author__username', 'text'
    list_filter = 'is_archive',

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):

    list_display = 'text','created', 'author'
    search_fields = 'created', 'author__username', 'text'