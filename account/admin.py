from django.contrib import admin
from account.models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'email',)
    list_filter = ('username', 'email',)

