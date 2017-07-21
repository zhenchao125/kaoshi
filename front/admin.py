# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Question, Record


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('course', 'type', 'score', 'level','title', 'sub_title', 'answer')


class RecordAdmin(admin.ModelAdmin):
    list_display = ('username', 'ques_id', 'status', 'score', 'times', 'update_time')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Record, RecordAdmin)
