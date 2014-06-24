from django.db import models
from django.contrib.auth.models import User, Group

NUMERICAL_SCALE = (
	(1, 1),
	(2, 2),
	(3, 3),
	(4, 4),
	(5, 5),
	(6, 6),
	(7, 7),
	(8, 8),
	(9, 9),
	(10,10),
)

class Employee(models.Model):
	user = models.OneToOneField(User)
	coach = models.ForeignKey(User, 
		limit_choices_to={'groups__name':'Coaches'},
		related_name='coach',
		null=True,
		blank=True)
	is_coach = models.BooleanField(default=False)

	def __unicode__(self):
		return self.user.first_name + ' ' + self.user.last_name

class FeedbackRequest(models.Model):
	requestor = models.ForeignKey(Employee, related_name="FeedbackRequestor")
	recipient = models.ForeignKey(Employee, related_name="RequestRecipient")


class Feedback(models.Model):
	date_given = models.DateTimeField(auto_now=True, blank=True)
	recipient = models.ForeignKey(Employee, default="", related_name="FeedbackRecipient")
	giver = models.ForeignKey(Employee, default="", related_name="FeedbackGiver")
	request = models.ForeignKey(FeedbackRequest, null=True, blank=True)
	fool_numerical_recommendation = models.PositiveIntegerField(choices=NUMERICAL_SCALE, null=True, blank=True)
	top_of_game_description = models.TextField(null=True, blank=True)
	next_level = models.TextField(null=True, blank=True)
	can_quote_giver = models.BooleanField(default=False)
	can_use_giver_name = models.BooleanField(default=False)
	summarize_only = models.BooleanField(default=False)
	coach_chat_before_delivery = models.BooleanField(default=False)
	best_judgement = models.BooleanField(default=False)






