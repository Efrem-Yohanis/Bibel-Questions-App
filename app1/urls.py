from django.urls import path
from .views import question_create,quiz_home,book_questions,submit_answer,question_portal

urlpatterns = [

    
    path('test', quiz_home, name='quiz_home'),
    path('create/', question_create, name='question_create'),
    path('quiz/<str:book>/', book_questions, name='book_question'),
    path('quiz/<str:book>/submit/', submit_answer, name='submit_answer'),  
    path('question_portal/', question_portal, name='question_portal'),  

    
  
]