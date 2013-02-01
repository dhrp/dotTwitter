from django.contrib import admin
from main.models import Tweet, Query, UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class TweetAdmin(admin.ModelAdmin):
    model = Tweet
    list_display = ('id', 'created_at', 'from_user_name', 'text')
    search_fields = ['from_user_name']
    list_filter = ['keyword']


class QueryAdmin(admin.ModelAdmin):
    model = Query
    list_display = ('id', 'keywords')


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    max_num = 1
    can_delete = False


class UserAdmin(UserAdmin):
    model = User, UserProfile
    inlines = [UserProfileInline]


admin.site.register(Tweet, TweetAdmin)
admin.site.register(Query, QueryAdmin)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)