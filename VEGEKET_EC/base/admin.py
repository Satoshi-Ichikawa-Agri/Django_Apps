from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from base.models import Item, Category, Tag, User, Profile, Order
from base.forms import UserCreationForm


class TagInline(admin.TabularInline):
    """
    """
    model = Item.tags.through


class ItemAdmin(admin.ModelAdmin):
    """
    """
    inlines = [TagInline] # 新しいタグ項目
    exclude = ['tags'] # デフォルトのタグ項目を除外


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class CustomUserAdmin(UserAdmin):
    """
    """
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password',)}),
        (None, {'fields': ('is_active', 'is_admin',)})
    )
    
    list_display = ('username', 'email', 'is_active',)
    list_filter = ()
    ordering = ()
    filter_horizontal = ()

    add_fieldsets = (
        (None, {'fields': ('username', 'email', 'is_active',)}),
    )

    add_form = UserCreationForm
    inlines = (ProfileInline,)



admin.site.register(Item, ItemAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Order)

admin.site.unregister(Group) # 管理画面から非表示

