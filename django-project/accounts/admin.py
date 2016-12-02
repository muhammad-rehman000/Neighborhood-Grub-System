from django.contrib import admin
from accounts.models import ChefPermissionsRequest, RedFlag

@admin.register(ChefPermissionsRequest)
class ChefPermissionsRequestAdmin(admin.ModelAdmin):
    """
    Django ModelAdmin class for providing the Grant/Deny Chef Permissions
    Request functionality.
    """
    actions = ["grant_request", "deny_request"]

    def grant_request(self, request, queryset):
        print("What what what what")

    def deny_request(self, request, queryset):
        print("Yut yut yut yut")

@admin.register(RedFlag)
class RedFlagAdmin(admin.ModelAdmin):
    """
    Django ModelAdmin class for providing the Review Red Flag functionality.
    """
    actions = ["close_red_flag"]

    def close_red_flag(self, request, queryset):
        print("Rut rut rut rut")
