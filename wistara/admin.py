from django.contrib import admin
from wistara.models import Reservation, Subcribe, Menu_Category, Menu, Review

# Register your models here.

@admin.register(Subcribe)
class SubcribeAdmin(admin.ModelAdmin):
    pass

@admin.register(Menu_Category)
class Menu_CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    pass

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    pass