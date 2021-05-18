from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from forum.forms.user import CustomUserCreationForm, CustomUserChangeForm
from forum.models.user import User
from forum.models.forum import Forum
from forum.models.thread import Thread
from forum.models.post import Post
from forum.models.receptionist import Receptionist


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, CustomUserAdmin)
admin.site.register(Forum)
admin.site.register(Thread)
admin.site.register(Post)
admin.site.register(Receptionist)
