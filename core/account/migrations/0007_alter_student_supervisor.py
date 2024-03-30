# Generated by Django 4.2.11 on 2024-03-30 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_remove_student_supervisor_student_supervisor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='supervisor',
            field=models.ForeignKey(default='cf1df455-e983-49a9-96df-8bf7c3fd4b7c', on_delete=django.db.models.deletion.PROTECT, related_name='supervisor', to='account.professor'),
        ),
    ]
