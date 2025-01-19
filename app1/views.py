from django.shortcuts import render, redirect, get_object_or_404
from .models import Question  # Ensure these models are defined
from django.contrib.auth import authenticate, logout
from django.contrib import messages

def question_portal(request):
    questions = Question.objects.all()
    return render(request, 'question_portal.html', {'questions': questions})

def add_question(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        book = request.POST.get('book')
        question_text = request.POST.get('Question')
        choice1 = request.POST.get('choice1')
        choice2 = request.POST.get('choice2')
        choice3 = request.POST.get('choice3')
        choice4 = request.POST.get('choice4')
        answer = request.POST.get('answer')

        # Create a new Question object and save it to the database
        Question.objects.create(
            category=category,
            book=book,
            Question_text=question_text,
            choice1=choice1,
            choice2=choice2,
            choice3=choice3,
            choice4=choice4,
            answer=answer
        )
        return redirect('question_portal')  # Redirect to a suitable page after submission

    return render(request, 'add_question.html')  # Render the form if not a POST request

def question_detail(request, id):
    question = get_object_or_404(Question, pk=id)
    return render(request, 'question_detail.html', {'question': question})

def quiz_home(request):
   

    return render(request, 'quiz_home.html')

def start_quiz(request):
    old_testament_books = Question.objects.filter(category='Old Testament').values_list('book', flat=True).distinct()
    new_testament_books = Question.objects.filter(category='New Testament').values_list('book', flat=True).distinct()

    context = {
        'old_books': list(old_testament_books),
        'new_books': list(new_testament_books),
    }
    return render(request, 'start_quiz.html', context)




def quiz_taking(request, book_name):
    questions = Question.objects.filter(book=book_name)
    question_index = int(request.POST.get('question_index', 0))  # Default to first question if not provided

    selected_answer = None
    feedback = None
    is_correct = None

    # If the form has been submitted
    if request.method == 'POST':
        answer = int(request.POST.get('answer', 0))  # Get the selected answer from the form
        current_question = questions[question_index]  # Get the current question
        selected_answer = answer
        is_correct = (answer == current_question.correct_answer)  # Check if the selected answer is correct

        # Provide feedback based on correctness
        if is_correct:
            feedback = "Correct"  # Show correct feedback
        else:
            feedback = "Incorrect"  # Show incorrect feedback

        # If the answer is correct, the user can move to the next question
        if is_correct:
            if 'next' in request.POST:
                question_index += 1  # Increment the question index to go to the next question

    # Check if there are more questions
    if question_index < len(questions):
        question = questions[question_index]  # Get the next question
        choices = [1, 2, 3, 4]  # Choices for answers
        context = {
            'book_name': book_name,
            'question': question,
            'question_index': question_index,
            'question_count': len(questions),
            'selected_answer': selected_answer,
            'is_correct': is_correct,
            'choices': choices,
            'feedback': feedback,
        }
        return render(request, "quiz_taking.html", context)

    # Redirect to the results page if all questions have been answered
    else:
        return redirect('quiz_results')

    
def quiz_results(request):
    if request.method == 'POST':
        # Collect user answers from the form submission
        user_answers = request.POST.getlist('answers')  # List of user's answers
        questions = Question.objects.filter(book=request.POST.get('book_name'))  # Get questions based on the book
        correct_answers = [question.answer for question in questions]  # Extract correct answers from the questions

        # Ensure that the number of user answers matches the number of questions
        if len(user_answers) != len(correct_answers):
            return render(request, 'quiz_results.html', {
                'score': 0,
                'total_questions': len(correct_answers),
                'results': [],
                'missed_questions': [],
            })

        score = 0
        results = []
        missed_questions = []

        # Calculate the score and prepare results
        for index, (user_answer, correct_answer) in enumerate(zip(user_answers, correct_answers)):
            is_correct = user_answer == correct_answer
            results.append({
                'question_number': index + 1,
                'user_answer': user_answer,
                'correct_answer': correct_answer,
                'is_correct': is_correct
            })
            if not is_correct:
                missed_questions.append(index + 1)
            else:
                score += 1  # Increment score if the answer is correct

        context = {
            'score': score,
            'total_questions': len(correct_answers),
            'results': results,
            'missed_questions': missed_questions,
        }
        return render(request, 'quiz_results.html', context)

    return redirect('quiz_home')  # Redirect to quiz home if not a POST request

def contact(request):
    return render(request, 'contact.html')

def about_me(request):
    return render(request, 'about_me.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            return redirect('question_portal')  # Redirect to a success page
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')

def logout_view(request):
    logout(request)  # Log the user out
    return redirect('login')