from django.contrib import admin

from ..models import Peca


@admin.register(Peca)
class PecaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nome',
        'preco',
        'quantidade',
    ]

    search_fields = [
        'id',
        'nome',
    ]

    list_per_page = 20
