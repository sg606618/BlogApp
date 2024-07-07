from django.contrib import admin
from account.models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('email',)
    list_filter = ('email',)

