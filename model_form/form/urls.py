from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.student_create, name='student_create'),
    path('add/',views.student_list, name='student_list'),
    path('details/<int:pk>' ,views.student_details , name='student_details'),
    path('edit/<int:pk>', views.student_edit, name='student_edit'),
    path('delete/<int:pk>/', views.student_delete, name='student_delete'),

]
