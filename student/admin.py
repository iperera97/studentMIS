from django.contrib import admin
from .models import Student, Registration


class RegAdmin(admin.ModelAdmin):

    list_display = ('pk', 'student', 'batch')


class RegAdminForm(admin.TabularInline):

    model = Registration
    exclude = ['pk', ]


class StudentAdmin(admin.ModelAdmin):

    list_display = ('pk', 'first_name', 'email')
    list_filter = ('register', 'title')
    inlines = (RegAdminForm,)


# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.register(Registration, RegAdmin)
