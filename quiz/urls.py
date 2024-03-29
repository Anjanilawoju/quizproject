from django.urls import path
from quiz import views

app_name = 'quiz'

urlpatterns = [
    path('',views.user_login,name='user_login'),
    path('index/',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('logout/',views.user_logout,name='user_logout'),
    path('quiz/',views.quizpage,name='quiz'),
]