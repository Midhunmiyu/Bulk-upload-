from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from data.models import Person


# Register your models here.
@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    pass