
from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('assign/<str:pk>', views.assign, name='assign'),
    path('students', views.student, name='student'),
    path('assignsection', views.assignsection, name='assignsection'),
    path('advisors', views.advisor, name='advisor'),
    path('addstu', views.addstu, name='addstu'),
    path('updstu/<str:pk>', views.updstu, name='updstu'),
    path('addadv', views.addadv, name='addadv'),
    path('updadv/<str:pk>', views.updadv, name='updadv'),
    path('delete_stu/<str:pk>', views.delete_stu, name='delete_stu'),
    path('delete_adv/<str:pk>', views.delete_adv, name='delete_adv'),
    path('student_list', views.student_list, name='student_list'),

]
