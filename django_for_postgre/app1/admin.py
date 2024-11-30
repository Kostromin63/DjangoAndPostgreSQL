from django.contrib import admin
from .models import Topic, News, PgTabl1, PgTabl2

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = "id", "name", "description"
    search_fields = "name",


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = "topic", "title", "created_at", "is_published",
    list_filter = "topic", "is_published",
    search_fields = "title", "content",
    list_per_page = 5

@admin.register(PgTabl1)
class PgTabl1Admin(admin.ModelAdmin):
    list_display = "name",
    list_filter = "name",
    search_fields = "name",
    list_per_page = 5


@admin.register(PgTabl2)
class PgTabl2Admin(admin.ModelAdmin):
    list_display = "name", "age", "height",
    list_filter = "name",
    search_fields = "name",
    list_per_page = 5
