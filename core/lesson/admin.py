from django.contrib import admin

from .models import Lesson, Term, PresentationTime, TermLesson, RegisteredLesson

# Register your models here.
admin.site.register(Lesson)
admin.site.register(Term)
admin.site.register(PresentationTime)
admin.site.register(TermLesson)
admin.site.register(RegisteredLesson)
