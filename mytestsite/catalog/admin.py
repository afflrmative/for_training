from django.contrib import admin
from .models import *

# admin.site.register(Games)
# admin.site.register(Genre)
# admin.site.register(Companys)

class GamesInstanceInLine(admin.TabularInline):
    model = Games

class CompanysAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_desc')
    inlines = [GamesInstanceInLine]
admin.site.register(Companys, CompanysAdmin)
 
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Games)
class GamesAdmin(admin.ModelAdmin):
    list_display = ('game_name', 'description', 'company_name')

@admin.register(GameLibrarys)
class GameLibraryAdmin(admin.ModelAdmin):
    list_display = ('game_list', 'borrower', 'time_add', 'id')
    list_filter = ('time_add',)
    fieldsets = (
        (None, {'fields': ('game_list', 'id')}),
        ('Availability', {'fields': ('time_add', 'borrower')}),
    )
