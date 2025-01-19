from django.urls import path
from .views import (
    add_question, 
    quiz_results, 
    login, 
    quiz_home, 
    quiz_taking, 
    logout_view, 
    start_quiz, 
    about_me, 
    question_portal, 
    question_detail, 
    contact
)

urlpatterns = [
    path('add_question/', add_question, name='add_question'),
    path('question_detail/<int:id>/', question_detail, name='question_detail'),
    path('question_portal/', question_portal, name='question_portal'),

    path('', quiz_home, name='quiz_home'),  
    path('start_quiz/', start_quiz, name='start_quiz'),
    path('quiz_taking/<str:book_name>/', quiz_taking, name='quiz_taking'),
    path('quiz_results/', quiz_results, name='quiz_results'),

    path('contact/', contact, name='contact'),
    path('about_me/', about_me, name='about_me'),
    path('admin_site/', login, name='login'),
    path('logout/', logout_view, name='logout'),
]