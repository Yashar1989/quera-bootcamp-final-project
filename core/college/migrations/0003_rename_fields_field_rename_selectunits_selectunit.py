# Generated by Django 4.2.11 on 2024-03-25 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_assistant_faculty_alter_professor_faculty'),
        ('lesson', '0002_alter_presentationtime_day'),
        ('college', '0002_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Fields',
            new_name='Field',
        ),
        migrations.RenameModel(
            old_name='SelectUnits',
            new_name='SelectUnit',
        ),
    ]