from django.contrib import admin
from app.introduction.models import VisitorGroup, Place, TicketPrice, Message


@admin.register(VisitorGroup)
class VisitorGroupAdmin(admin.ModelAdmin):
    list_display = [
        "code",
    ]


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = [
        "code",
        "title",
        "image",
        "time",
        "date",
        "rule",
        "detail",
        "registerDateTime",
    ]
    exclude = ("registerDateTime",)


@admin.register(TicketPrice)
class TicketPriceAdmin(admin.ModelAdmin):
    list_display = [
        "price",
        "group",
        "place",
    ]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = [
        "code",
        "name",
        "family",
        "email",
        "subject",
        "text",
        "registerDate",
        "isActive",
    ]
    exclude = ("registerDate",)
