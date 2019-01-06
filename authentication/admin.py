from django.contrib import admin
from django.contrib.auth import get_user_model


# customize admin view
User = get_user_model()


class UserAdmin(admin.ModelAdmin):

    list_display = ('pk', 'email', 'active', 'admin', 'staff')
    list_display_links = list_display
    list_per_page = 20
    readonly_fields = ('register',)
    list_filter = ('active', 'admin', 'staff')

    search_fields = ('pk', 'email',)
    ordering = ('pk',)


admin.site.register(User, UserAdmin)
