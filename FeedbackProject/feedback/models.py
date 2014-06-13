from django.db import models

class BaseEmployee(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	is_coach = models.BooleanField()


class FeedbackRecipient(models.Model):
	coach = models.ForeignKey(BaseEmployee, default="This Fool does not yeat have a feedback coach", limit_choices_to={'is_coach': True})


class Feedback(models.Model):
	date_given = models.DateTimeField(auto_now=True, blank=True)
	feedback = models.TextField(null=True, blank=True)
	recipient = models.ForeignKey(FeedbackRecipient, default="")
	

class FeedbackGiver(models.Model):
	feedback_to_give = models.ForeignKey(Feedback, null=True, blank = True)
