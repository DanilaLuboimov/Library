from django.contrib import admin

from .models import User, Feedback


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "first_name", "email")


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "short_message", "created_at", "is_answer")
    readonly_fields = (
        "email", "message", "first_name", "phone_number", "created_at"
    )

    def short_message(self, object):
        if len(object.message) > 50:
            return object.message[:50]
        return object.message

    short_message.short_description = "Короткое сообщение"


admin.site.register(User, UserAdmin)
admin.site.register(Feedback, FeedbackAdmin)
