from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from toys.models import Address, Tag, Toy, User, Company, Employee
from toys.service.send_salary_report import send_employee_slaray_report
from toys.service.send_weekly_report import send_weekly_toys_count


class ToyTagsInlineModel(admin.StackedInline):
    model = Toy.tags.through
    extra = 1


def send_weekly_email_report(modeladmin, request, queryset):
    if queryset.count() != 1:
        modeladmin.message_user(request, 'Multiple user selected, please choose one and only one. ', messages.ERROR)
        return HttpResponseRedirect(request.get_full_path())
    user = queryset.first()
    if not user.email:
        modeladmin.message_user('Selected user does not have email address', messages.ERROR)

        return HttpResponseRedirect(request.get_full_path())

    send_weekly_toys_count(user)

    modeladmin.message_user(request, 'Wekkly report sent to user email: %s' % user.email, messages.INFO)
    return HttpResponseRedirect(request.get_full_path())


@admin.register(Toy)
class ToyAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'price', 'user']
    empty_value_display = '-empty-'
    autocomplete_fields = ['tags', ]
    fieldsets = (
        (None, {
            'fields': ('name', 'user', 'description',)
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('photo', 'price', 'tags',),
        }),
    )
    inlines = (ToyTagsInlineModel,)
    search_fields = ['user__first_name', ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    actions_on_top = False
    actions_on_bottom = True
    search_fields = ['name']
    readonly_fields = ('created_at', 'updated_at')


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ['first_name', 'last_name', 'password_change_link']
    readonly_fields = ('password_change_link',)

    fieldsets = (
        (None, {'fields': ('username', 'password', 'password_change_link',)}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    def password_change_link(self, obj):
        html = format_html(f'<a href ="/admin/toys/user/{obj.pk}/password/" >Change password</a> ')
        return html


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['street', 'city', 'zip_code']

class CompanyEmployeeInline(admin.StackedInline):
    model = Employee
    extra = 0

def send_company_report(modeladmin, request, queryset):
    str =''
    for company in queryset:

        if not company.email:
            modeladmin.message_user( request,f'Selected company {company.name} does not have email address ', messages.ERROR)

        send_employee_slaray_report(company)
        str +='Salary report sent to company email: %s \t'% company.email

    modeladmin.message_user(request, str, messages.INFO)
    return HttpResponseRedirect(request.get_full_path())



@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']
    date_hierarchy = 'updated_at'


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    inlines = [
        CompanyEmployeeInline,
    ]
    actions = [ send_company_report ]
