from django.contrib import admin
from feedback.models import Employee, Feedback, FeedbackRequest

admin.site.register(Employee)
admin.site.register(Feedback)
admin.site.register(FeedbackRequest)
