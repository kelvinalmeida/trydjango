from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Course
from .forms import CreateCourseForm

# Create your views here.

class CourseObjectMixin(object):
    model = Course

    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Course, id = id)

        return obj


class CourseDeleteView(CourseObjectMixin, View):
    template_name = 'courses/course_delete.html'
    
    def get(self, request, id=None):
        obj = self.get_object()

        context = {
            "obj": obj,
        }

        return render(request, self.template_name, context)
    
    def post(self, request, id=None):
        
        obj = self.get_object()

        if obj is not None:
            obj.delete()
            return redirect('/courses/')
        
        context = {}

        return render(request, self.template_name, context)
    
class CourseUpdateView(CourseObjectMixin, View):
    template_name = 'courses/course_update.html'
    
    def get(self, request, id=None):
        obj = self.get_object()

        if obj is not None:
            form = CreateCourseForm(instance=obj)

        context = {
            "form": form,
            "obj": obj
        }

        return render(request, self.template_name, context)
    
    def post(self, request, id=None):
        
        obj = self.get_object()

        if obj is not None:
            form = CreateCourseForm(request.POST, instance=obj)

        if form.is_valid():
            form.save()
            form = CreateCourseForm()

        context = {
            "form": form,
            "obj": obj
        }

        return render(request, self.template_name, context)

class CourseCreateView(View):
    template_name = 'courses/course_create.html'

    def get(self, request, id=None):
        form = CreateCourseForm()
        context = {
            "form": form
        }

        return render(request, self.template_name, context)
    
    def post(self, request, id=None):
        form = CreateCourseForm(request.POST)
        
        if form.is_valid():
            form.save()
            form = CreateCourseForm()

        context = {
            "form": form
        }

        return render(request, self.template_name, context)


class CourseView(CourseObjectMixin, View):
    template_name = 'courses/course_detail.html'

    def get(self, request, id=None):
        context = {}
        
        obj = self.get_object()
        context['object'] = obj

        return render(request, self.template_name, context)

class CourseListView(View):
    template_name = 'courses/course_list.html'
    queryset = Course.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, id=None):

        context = {
            "objects": self.get_queryset()
        }

        return render(request, self.template_name, context)