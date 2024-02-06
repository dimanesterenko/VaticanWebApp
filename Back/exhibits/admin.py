from django.contrib import admin

# Register your models here.
from .models import Exhibit

class ExibitAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "creator_name")

admin.site.register(Exhibit,ExibitAdmin)