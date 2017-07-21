# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField('用户名', max_length=50)
    password = models.CharField('密码', max_length=50)
    class_name = models.CharField('所属班级', max_length=10)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户'


QUES_TYPE_CHOICE = (
    ('1', '选择题'),
    ('2', '编程题')
)

COURSE_CHOICE = (
    ('1', 'Python'),
    ('2', 'HTML5'),
    ('3', 'JAVA')
)


class Question(models.Model):
    course = models.CharField('学科', max_length=10, choices=COURSE_CHOICE, default='1', null=True)
    type = models.CharField('题目类型', max_length=2, choices=QUES_TYPE_CHOICE, default='1')
    score = models.CharField('分数', max_length=10)
    level = models.CharField('难度系数', max_length=10)
    title = models.TextField('题目标题', null=True)
    sub_title = models.TextField('题目选项', null=True)
    answer = models.CharField('答案', max_length=50)
    ques_ext = models.CharField('其他', max_length=255, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '题目'
        verbose_name_plural = '题目'


class Record(models.Model):
    username = models.CharField('用户名', max_length=50)
    ques_id = models.CharField('题目序号', max_length=10)
    status = models.CharField('答题状态', max_length=10, null=True)
    score = models.CharField('分数', max_length=10, null=True)
    times = models.CharField('考试次数', max_length=10, null=True)
    update_time = models.DateTimeField('更新时间', auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '记录'
        verbose_name_plural = '记录'

