from django.contrib import admin
from .models import Employees, Author, Book, Roles, User, User_details, UserData
# admin.site.register() using this to store our data base in admin

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date')
    list_filter = ('author', 'publication_date')
    search_fields = ('title', 'author__name')


@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'employee_name', 'employee_number', 'employee_age')


@admin.register(Roles, )
class RolesAdmin(admin.ModelAdmin):
    list_display = ('id_role', 'work_roles')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'name', 'email', 'password', 'id_role', 'years_of_experience', 'employee_num')


@admin.register(User_details)
class User_detailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_role', 'user_id')


@admin.register(UserData)
class UserDataAdmin(admin.ModelAdmin):
    list_display = (
        'user_name',
        'email',
        'password')
