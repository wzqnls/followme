#!/usr/bin/env python
# encoding: utf-8

"""
@author: lee 
@file: urls.py
@time: 2017/3/13 18:04
"""

from django.conf.urls import url

from .views import CourseListView


urlpatterns = [
    # 课程列表页
    url(r'^list/$', CourseListView.as_view(), name='course_list'),
]