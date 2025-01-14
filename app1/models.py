from django.db import models

class Question(models.Model):
    CATEGORY_CHOICES = [
        ('OT', 'Old Testament'),
        ('NT', 'New Testament'),
    ]
    
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    book = models.CharField(max_length=50)
    question_text = models.CharField(max_length=255)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)  # Field to mark the correct answer

    def __str__(self):
        return self.text