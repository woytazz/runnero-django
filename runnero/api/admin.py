from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, UserProfile, Challenge, UserActiveChallenge, UserDoneChallenge, Prize, UserPrize


# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'is_staff', 'is_active',)
    list_filter = ('id', 'email', 'first_name', 'last_name', 'is_staff', 'is_active',)
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


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'travelled_dist', 'points',)
    search_fields = ('user',)
    ordering = ('user',)


@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ('for_level', 'description', 'start_at', 'end_at', 'points', 'distance',)


@admin.register(UserActiveChallenge)
class UserActiveChallengeAdmin(admin.ModelAdmin):
    list_display = ('user', 'challenge',)


@admin.register(UserDoneChallenge)
class UserDoneChallengeAdmin(admin.ModelAdmin):
    list_display = ('user', 'challenge',)


@admin.register(Prize)
class PrizeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'points', 'png', 'shop_name',)


@admin.register(UserPrize)
class UserPrizeAdmin(admin.ModelAdmin):
    list_display = ('user', 'prize',)
