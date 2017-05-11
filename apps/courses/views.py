# encoding: utf8

from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.


class CourseListView(View):
    def get(self, request):
        return render(request, "course-list.html", {})
