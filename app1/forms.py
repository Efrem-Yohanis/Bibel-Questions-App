from django import forms
from .models import QuestionForm

class QuestionForm(forms.ModelForm):
    class Meta:
        model = QuestionForm
        fields = ['question_text', 'correct_answer', 'option_a', 'option_b', 'option_c', 'option_d', 'category', 'book']