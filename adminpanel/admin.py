from django.contrib import admin

from adminpanel.models import Images

@admin.register(Images)
class PersonAdmin(admin.ModelAdmin):
    pass