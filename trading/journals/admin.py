from django.contrib import admin

from .models import Journal


class JournalAdmin(admin.ModelAdmin):
    list_display = ["open_time", "ticker", "side"]


admin.site.register(Journal, JournalAdmin)
