from django.contrib import admin

from server.accounts.models import CustomUser

admin.site.register(CustomUser)
