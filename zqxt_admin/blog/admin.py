from django.contrib import admin
from.models import Article, Person
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'update_time')


class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name',)


admin.site.register(Article, ArticleAdmin) #ArticleAdmin相当于把field的内容显示到了admin的列表上
admin.site.register(Person, PersonAdmin)
