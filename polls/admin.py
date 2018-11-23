from django.contrib import admin
from polls.models import Choice, Poll
from polls import models
# Register your models here.

# admin.site.register(models.Poll)


# class PollAdmin(admin.ModelAdmin):
#     # 字段展示排序
#     fields = ['pub_date', 'question']
#
# admin.site.register(models.Poll, PollAdmin)

# admin.site.register(models.Choice)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'pub_date')
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Poll, PollAdmin)