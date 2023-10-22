from django.shortcuts import render, get_object_or_404

from django.views import View
from .models import Course

# Create your views here.

class CourseView(View):
    template_name = 'courses/course_detail.html'

    def get(self, request, id=None):
        context = {}

        if not id == None:
            obj = get_object_or_404(Course, id = id)
            context['object'] = obj

        return render(request, self.template_name, context)