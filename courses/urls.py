from django.urls import path

from .views import CourseView, CourseListView, CourseCreateView, CourseUpdateView, CourseDeleteView

urlpatterns = [
    path('', CourseListView.as_view(), name='course-list'),
    path('<int:id>/', CourseView.as_view(), name='course-detail'),
    path('<int:id>/update', CourseUpdateView.as_view(), name='course-update'),
    path('<int:id>/delete', CourseDeleteView.as_view(), name='course-delete'),
    path('create/', CourseCreateView.as_view(), name='course-create'),

]