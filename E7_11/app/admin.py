from django.contrib import admin
from .models import Advert, Comment, Tag

admin.site.site_title = "Объявления"
admin.site.site_header = "Объявления"


@admin.register(Advert)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("author", "created")
    list_display_links = ("author",)
    list_filter = ("author",)
    search_fields = ("author",)


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ("author", "created")
    list_display_links = ("author",)
    list_filter = ("author",)
    search_fields = ("author",)


admin.site.register(Tag)