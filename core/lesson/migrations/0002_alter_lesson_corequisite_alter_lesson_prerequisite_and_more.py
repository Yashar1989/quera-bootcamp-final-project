# Generated by Django 4.2.11 on 2024-03-22 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='corequisite',
            field=models.ManyToManyField(to='lesson.lesson'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='prerequisite',
            field=models.ManyToManyField(to='lesson.lesson'),
        ),
        migrations.AlterField(
            model_name='termlesson',
            name='presentation_time',
            field=models.ManyToManyField(related_name='lessons', to='lesson.presentationtime'),
        ),
    ]
