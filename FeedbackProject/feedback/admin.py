from django.contrib import admin
from feedback.models import Employee, FeedbackRecipient, Feedback, FeedbackGiver

admin.site.register(Employee)
admin.site.register(FeedbackRecipient)
admin.site.register(Feedback)
admin.site.register(FeedbackGiver)
