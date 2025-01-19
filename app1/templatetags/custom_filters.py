from django import template

register = template.Library()

@register.filter
def get_choice(question, choice_number):
    return getattr(question, f'choice{choice_number}')