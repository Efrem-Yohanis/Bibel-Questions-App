# Generated by Django 5.1.4 on 2025-01-17 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_alter_questiondb_options_alter_questiondb_answer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questiondb',
            name='category',
            field=models.CharField(blank=True, choices=[('Old', 'Old'), ('New', 'New')], max_length=50),
        ),
    ]
