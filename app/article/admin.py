from django.contrib import admin
from app.article.models import Author, Article, ArticleGroup, ArticleGallery


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "family",
        "email",
        "phone",
        "slug",
        "education",
        "job",
        "isActive",
    ]
    ordering = ["name", "family", "isActive"]
    prepopulated_fields = {"slug": ("name", "family")}


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "image",
        "slug",
        "text",
        "word",
        "description",
        "article",
        "registerDate",
        "publishDate",
        "updateDate",
        "seen",
        "isActive",
    ]
    prepopulated_fields = {"slug": ("title", "author")}
    ordering = ["title", "author", "isActive"]


@admin.register(ArticleGroup)
class ArticleGroupAdmin(admin.ModelAdmin):
    list_display = [
        "title"
    ]


@admin.register(ArticleGallery)
class ArticleGalleryAdmin(admin.ModelAdmin):
    list_display = [
        "article",
        "image",
    ]
