from django.contrib import admin

from apps.tasks.models import Comment, Task, State, Priority


def admin_model(model):
    class CustomAdmin(admin.ModelAdmin):
        list_display = [field.name for field in model._meta.fields]

    return CustomAdmin


admin.site.register
admin.site.register(Comment, admin_model(Comment))
admin.site.register(Task, admin_model(Task))
admin.site.register(State, admin_model(State))
admin.site.register(Priority, admin_model(Priority))
