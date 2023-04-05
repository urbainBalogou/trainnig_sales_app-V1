from django.contrib import admin
from .models import Formation


class FormationAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'prix')
    search_fields = ['nom']


admin.site.register(Formation, FormationAdmin)

# Register your models here.
