from django.db import models

class TermModificationRequest(models.Model):
    # student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # added_course = models.ForeignKey(Course, related_name='added_courses', on_delete=models.CASCADE)
    # removed_course = models.ForeignKey(Course, related_name='removed_courses', on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)

class ReviewRequest(models.Model):
    # student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # course = models.ForeignKey(Course, on_delete=models.CASCADE)
    review_text = models.TextField()
    response = models.TextField(blank=True, null=True)

class EmergencyRemovalRequest(models.Model):
    # student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # course = models.ForeignKey(Course, on_delete=models.CASCADE)
    request_result = models.CharField(max_length=50)
    student_comment = models.TextField()
    admin_comment = models.TextField()
