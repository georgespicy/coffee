from django.contrib import admin
from wistara.models import Subcribe

# Register your models here.

@admin.register(Subcribe)
class SubcribeAdmin(admin.ModelAdmin):
    pass