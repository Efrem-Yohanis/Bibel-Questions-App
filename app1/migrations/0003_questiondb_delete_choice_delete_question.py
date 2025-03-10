# Generated by Django 5.1.4 on 2025-01-14 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_choice_id_alter_question_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=50)),
                ('book', models.CharField(blank=True, max_length=100)),
                ('question_text', models.TextField(blank=True)),
                ('choice1', models.CharField(blank=True, max_length=255)),
                ('choice2', models.CharField(blank=True, max_length=255)),
                ('choice3', models.CharField(blank=True, max_length=255)),
                ('choice4', models.CharField(blank=True, max_length=255)),
                ('answer', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
