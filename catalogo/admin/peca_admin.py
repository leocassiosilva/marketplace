from django.contrib import admin

from ..models import Peca
from import_export.admin import ImportExportModelAdmin


@admin.register(Peca)
class PecaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
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
