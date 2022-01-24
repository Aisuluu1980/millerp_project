from django.contrib import admin
from webapp.models import Project, News, Message


# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subject')


admin.site.register(Project)
admin.site.register(News)
admin.site.register(Message)
