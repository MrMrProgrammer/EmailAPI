from django.contrib import admin
from .models import Log


class showLog(admin.ModelAdmin):
    list_display = ["ip", "host", "password", "to", "subject", "content", "jalali_datetime"]


admin.site.register(Log, showLog)
