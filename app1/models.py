from django.db import models

class Question(models.Model):
    CATEGORY_CHOICES = [
        ('Old Testament', 'Old Testament'),
        ('New Testament', 'New Testament'),
        # Add other categories as needed
    ]

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, blank=True)
    book = models.CharField(max_length=100, blank=True)
    Question_text = models.TextField()
    choice1 = models.CharField(max_length=255, blank=True)
    choice2 = models.CharField(max_length=255, blank=True)
    choice3 = models.CharField(max_length=255, blank=True)
    choice4 = models.CharField(max_length=255, blank=True)
    correct_answer = models.PositiveSmallIntegerField()  # 1, 2, 3, or 4 to represent the correct choice

    def __str__(self):
        return self.Question_text

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"