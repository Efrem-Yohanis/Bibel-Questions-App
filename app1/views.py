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
    old_testament_books = Question.objects.filter(category='Old').values_list('book', flat=True).distinct()
    new_testament_books = Question.objects.filter(category='New').values_list('book', flat=True).distinct()

    context = {
        'old_books': list(old_testament_books),
        'new_books': list(new_testament_books),
    }
    return render(request, 'start_quiz.html', context)


from django.shortcuts import render, redirect
from .models import Question

def quiz_taking(request, book_name):
    # Assuming Question model has a 'book' field and 'correct_answer'
    questions = Question.objects.filter(book=book_name).order_by('id')
    question_index = int(request.POST.get('question_index', 0))

    if request.method == 'POST':
        answer = int(request.POST.get('answer'))  # Assume answer is passed as an integer
        current_question = questions[question_index]

        # Check if the answer is correct
        is_correct = answer == current_question.correct_answer

        # Store the result for display
        selected_answer = answer

        # Move to the next question
        question_index += 1
    else:
        selected_answer = None
        is_correct = None

    if question_index < len(questions):
        question = questions[question_index]
        choices = [1, 2, 3, 4]  # List of choice numbers
        context = {
            'book_name': book_name,
            'question': question,
            'question_index': question_index,
            'selected_answer': selected_answer,
            'is_correct': is_correct,
            'choices': choices  # Pass the list of choices
        }
        return render(request, "quiz_taking.html", context)
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