from django.contrib import admin

# Register your models here.
from hello.models import Question,Choice


class QuestionAdmin(admin.ModelAdmin):
    # 展示的字段
    list_display = ('question_text', 'pub_date')

    # 右侧过滤器
    list_filter = ['pub_date']

    # 查询字段
    search_fields = ['name']


admin.site.register(Question,QuestionAdmin)








admin.site.register(Choice)
