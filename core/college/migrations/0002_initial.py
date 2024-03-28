# Generated by Django 4.2.11 on 2024-03-28 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('lesson', '0001_initial'),
        ('college', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='selectunit',
            name='on_demand_courses',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lesson.lesson'),
        ),
        migrations.AddField(
            model_name='field',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='college.department'),
        ),
        migrations.AddField(
            model_name='department',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departments', to='college.faculty'),
        ),
        migrations.AddField(
            model_name='department',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.professor'),
        ),
        migrations.AddField(
            model_name='department',
            name='professors',
            field=models.ManyToManyField(related_name='departments', to='account.professor'),
        ),
    ]
