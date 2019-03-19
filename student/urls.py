from django.urls import path
from . import views


app_name = 'student'

urlpatterns = [
	path('', views.HomepageView.as_view(), name='homepage'),
	path('student/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('student/create/', views.StudentCreate.as_view(), name='student_create'),
    path('student/update/<int:pk>/', views.StudentUpdate.as_view(), name='student_update'),
    path('student/delete/<int:pk>/', views.StudentDelete.as_view(), name='student_delete'),
	]
