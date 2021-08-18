from django.contrib import admin
from .models import QuizeName, Questions, SingelAnswer, Client


class SingelAnswerInline(admin.StackedInline):
    model = SingelAnswer
    extra = 0

class QuestionsInline(admin.StackedInline):
    model = Questions
    extra = 0
    inlines = [SingelAnswerInline, ]

@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'quize', 'question']
    list_display_links = ['id', 'quize', 'question']
    inlines = [SingelAnswerInline, ]

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'userName']

@admin.register(QuizeName)
class QuizeNameAdmin(admin.ModelAdmin):
    list_display = ['name', 'dataStart', 'dateFinish', 'status']
    list_display_links = ['name', 'dataStart', 'dateFinish', ]
    list_editable = ['status',]
    inlines = [QuestionsInline,]