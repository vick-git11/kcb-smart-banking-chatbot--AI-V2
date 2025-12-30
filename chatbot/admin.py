from django.contrib import admin
from .models import FAQ, ChatLog

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question",)
    search_fields = ("question",)

@admin.register(ChatLog)
class ChatLogAdmin(admin.ModelAdmin):
    list_display = ("user_message", "intent", "risk", "route", "created_at")
    search_fields = ("user_message", "intent", "risk")
    list_filter = ("risk", "route", "created_at")
