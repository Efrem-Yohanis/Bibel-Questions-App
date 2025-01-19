from django import template

register = template.Library()

@register.filter(name='get_choice')
def get_choice(question, choice_number):
    """
    A custom filter to get the choice text for a given choice number.
    (1, 2, 3, 4 corresponds to choice1, choice2, choice3, choice4)
    """
    choices = {
        1: question.choice1,
        2: question.choice2,
        3: question.choice3,
        4: question.choice4
    }
    return choices.get(choice_number, '')
