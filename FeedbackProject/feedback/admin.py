from django.contrib import admin
from feedback.models import BaseEmployee, FeedbackRecipient, Feedback, FeedbackGiver

admin.site.register(BaseEmployee)
admin.site.register(FeedbackRecipient)
admin.site.register(Feedback)
admin.site.register(FeedbackGiver)
