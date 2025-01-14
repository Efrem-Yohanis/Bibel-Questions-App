from django.shortcuts import render, redirect
from .models import Question, Choice  # Ensure these models are defined

def question_create(request):
    if request.method == 'POST':
        # Retrieve data from the request
        category = request.POST.get('category')
        book = request.POST.get('book')
        question_text = request.POST.get('question_text')
        answers = [
            request.POST.get('answer_1'),
            request.POST.get('answer_2'),
            request.POST.get('answer_3'),
            request.POST.get('answer_4'),
        ]
        correct_answer = request.POST.get('correct_answer')  # Get the correct answer

        # Create and save the Question instance
        question = Question(
            category=category,
            book=book,
            question_text=question_text
        )
        question.save()

        # Save each answer as a Choice and highlight the correct one
        for answer in answers:
            choice = Choice(
                question=question,
                text=answer.strip()  # Remove any leading/trailing whitespace
            )
            choice.save()

            # Mark the correct choice
            if answer.strip() == correct_answer.strip():
                choice.is_correct = True  # Assuming you modify the Choice model to include this field
                choice.save()

        return redirect('question_list')  # Redirect to your question list page

    # Render the form for GET requests
    return render(request, 'question_create.html')


def quiz_home(request):
    # List of books for Old Testament and New Testament
    old_testament_books = [
        'Genesis', 'Exodus', 'Leviticus', 'Numbers', 'Deuteronomy',
        'Joshua', 'Judges', 'Ruth', '1 Samuel', '2 Samuel',
        '1 Kings', '2 Kings', '1 Chronicles', '2 Chronicles',
        'Ezra', 'Nehemiah', 'Esther', 'Job', 'Psalms',
        'Proverbs', 'Ecclesiastes', 'Song of Solomon', 'Isaiah',
        'Jeremiah', 'Lamentations', 'Ezekiel', 'Daniel', 'Hosea',
        'Joel', 'Amos', 'Obadiah', 'Jonah', 'Micah', 'Nahum',
        'Habakkuk', 'Zephaniah', 'Haggai', 'Zechariah', 'Malachi'
    ]

    new_testament_books = [
        'Matthew', 'Mark', 'Luke', 'John', 'Acts', 'Romans',
        '1 Corinthians', '2 Corinthians', 'Galatians', 'Ephesians',
        'Philippians', 'Colossians', '1 Thessalonians', '2 Thessalonians',
        '1 Timothy', '2 Timothy', 'Titus', 'Philemon', 'Hebrews',
        'James', '1 Peter', '2 Peter', '1 John', '2 John',
        '3 John', 'Jude', 'Revelation'
    ]

    context = {
        'old_testament_books': old_testament_books,
        'new_testament_books': new_testament_books,
    }

    return render(request, 'quiz_home.html', context)



def book_questions(request, book):
    # Retrieve questions related to the selected book
    questions = Question.objects.filter(book=book).prefetch_related('choices')  # Optimize queries
    question_index = int(request.GET.get('question_index', 0))

    if question_index >= len(questions):
        return redirect('quiz_home')  # Redirect if no more questions

    current_question = questions[question_index]
    context = {
        'book': book,
        'question': current_question,
        'choices': current_question.choices.all(),
        'question_index': question_index,
        'total_questions': len(questions),
    }
    return render(request, 'book_questions.html', context)



def submit_answer(request, book):
    if request.method == 'POST':
        selected_choice_id = request.POST.get('selected_choice')
        question_index = int(request.POST.get('question_index', 0))
        total_questions = int(request.POST.get('total_questions', 0))

        # Here you can implement logic to save the user's answer
        # For example, you could save it to a model or session

        # Redirect to the next question or finish if it's the last question
        if question_index + 1 < total_questions:
            return redirect(f'{book}/?question_index={question_index + 1}')
        else:
            return redirect('quiz_home')  # Redirect to quiz home or results page

    return redirect('quiz_home')  # Fallback redirection





def question_portal(request):
    return render(request, 'question_portal.html')