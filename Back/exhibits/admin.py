from django.contrib import admin

# Register your models here.
from .models import Exhibit

from mainbooking.models import Visitor,Responsible,Booking,Guide, Ticket
from souvenirshop.models import Souvenir
from news.models import News
class ExibitAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "creator_name")

admin.site.register(Exhibit,ExibitAdmin)
admin.site.register(Visitor)
admin.site.register(Responsible)
admin.site.register(Booking)
admin.site.register(Ticket)
admin.site.register(Guide)
admin.site.register(Souvenir)
admin.site.register(News)