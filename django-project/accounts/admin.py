import os

from django.contrib import admin
from django.contrib.auth.models import User

from accounts.models import ChefPermissionsRequest, RedFlag, Complaint
from accounts.models import TerminateAccountRequest, CreateAccountRequest

from dishes.models import Diner, Chef

@admin.register(CreateAccountRequest)
class CreateAccountRequestAdmin(admin.ModelAdmin):
    """
    Django ModelAdmin class for providing the Approve/Reject Create Account
    Request functionality.
    """
    list_display = [
        "email",
        "username",
        "first_name",
        "last_name",
        "status",
        "user"
    ]
    actions = ["approve_request", "reject_request"]

    def get_queryset(self, request):
        """
        Limit the CreateAccountRequest queryset to those that are pending.
        """
        qs = super(CreateAccountRequestAdmin, self).get_queryset(request)
        return qs.filter(status=CreateAccountRequest.PENDING)

    def approve_request(self, request, queryset):
        """
        Create an account for each approved Create Account Request.
        """
        for createAccountRequest in queryset:
            # Create the User object.
            # Generate a random password
            password = User.objects.make_random_password()
            pass_file = "{}_password.txt".format(createAccountRequest.username)
            with open(pass_file, "w") as fh:
                print(password, file=fh)
            # "email" the person their random password. For this project that
            # will simply be printing the random password to stdout
            username = createAccountRequest.username
            email = createAccountRequest.email
            user = User(username=username, email=email)
            user.set_password(password)
            user.save()
            # Create Diner object.
            diner = Diner.objects.create(user=user)
            # Update the status of this Create Account Request
            createAccountRequest.status = CreateAccountRequest.APPROVED
            createAccountRequest.save()

    def reject_request(self, request, queryset):
        """
        Set the status of each rejected request to rejected.
        """
        for createAccountRequest in queryset:
            createAccountRequest.status = CreateAccountRequest.REJECTED
            createAccountRequest.save(update_fields=["status"])

@admin.register(ChefPermissionsRequest)
class ChefPermissionsRequestAdmin(admin.ModelAdmin):
    """
    Django ModelAdmin class for providing the Grant/Deny Chef Permissions
    Request functionality.
    """
    list_display = [
        "user",
        "first_dish",
        "second_dish",
        "third_dish",
        "bio",
    ]
    actions = ["grant_request", "deny_request"]

    def get_queryset(self, request):
        """
        Limit the ChefPermissionsRequest queryset to those that are pending.
        """
        qs = super(ChefPermissionsRequestAdmin, self).get_queryset(request)
        return qs.filter(status=ChefPermissionsRequest.PENDING)

    def first_dish(self, chefPermissionsRequest):
        if chefPermissionsRequest.first_dish_image:
            url = chefPermissionsRequest.first_dish_image.url
            head, fname = os.path.split(url)
            url = os.path.join("/static", fname)
            return '<a href="{url}">{dish_name}</a>'.format(
                    url=url,
                    dish_name=chefPermissionsRequest.first_dish_name
                )
        else:
            return chefPermissionsRequest.first_dish_name

    first_dish.allow_tags = True

    def second_dish(self, chefPermissionsRequest):
        if chefPermissionsRequest.second_dish_image:
            url = chefPermissionsRequest.second_dish_image.url
            head, fname = os.path.split(url)
            url = os.path.join("/static", fname)
            return '<a href="{url}">{dish_name}</a>'.format(
                    url=url,
                    dish_name=chefPermissionsRequest.second_dish_name
                )
        else:
            return chefPermissionsRequest.second_dish_name

    second_dish.allow_tags = True

    def third_dish(self, chefPermissionsRequest):
        if chefPermissionsRequest.third_dish_image:
            url = chefPermissionsRequest.third_dish_image.url
            head, fname = os.path.split(url)
            url = os.path.join("/static", fname)
            return '<a href="{url}">{dish_name}</a>'.format(
                    url=url,
                    dish_name=chefPermissionsRequest.third_dish_name
                )
        else:
            return chefPermissionsRequest.third_dish_name

    third_dish.allow_tags = True

    def bio(self, chefPermissionsRequest):
        if chefPermissionsRequest.video_biography:
            url = chefPermissionsRequest.video_biography.url
            head, fname = os.path.split(url)
            url = os.path.join("/static", fname)
            return '<a href="{url}">Bio</a>'.format(url=url)
        else:
            return "(No Bio found)"

    bio.allow_tags = True


    def grant_request(self, request, queryset):
        for chefPermissionsRequest in queryset:
            # Create Chef object for this user.
            user = chefPermissionsRequest.user
            name = user.first_name + user.last_name
            chef = Chef.objects.create(user=user)
            # Update the status of this Chef Permissions Request
            chefPermissionsRequest.status = ChefPermissionsRequest.APPROVED
            chefPermissionsRequest.save()

    def deny_request(self, request, queryset):
        for chefPermissionsRequest in queryset:
            chefPermissionsRequest.status = ChefPermissionsRequest.REJECTED
            chefPermissionsRequest.save()

@admin.register(RedFlag)
class RedFlagAdmin(admin.ModelAdmin):
    """
    Django ModelAdmin class for providing the Review Red Flag functionality.
    """
    actions = ["close_red_flag"]

    def close_red_flag(self, request, queryset):
        print("Rut rut rut rut")

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    """
    Django ModelAdmin class for providing the Review Complaint functionality.
    """
    actions = ["close_complaint"]

    def close_complaint(self, request, queryset):
        print("Woop woop woop woop")

@admin.register(TerminateAccountRequest)
class TerminateAccountRequestAdmin(admin.ModelAdmin):
    """
    Django ModelAdmin class for providing the Delete User Account
    functionality.
    """
    list_display = ["user"]
    actions = ["delete_account"]

    def delete_account(self, request, queryset):
        for terminateAccountRequest in queryset:
            user = terminateAccountRequest.user
            user.delete()
