from django.db import models

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

class BaseEmployee(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	is_coach = models.BooleanField()


class FeedbackRecipient(BaseEmployee):
	coach = models.ForeignKey(BaseEmployee, default="This Fool does not yeat have a feedback coach", 
		limit_choices_to={'is_coach': True}, related_name='RecipientCoach'
	)


class FeedbackGiver(BaseEmployee):
	can_quote_giver = models.BooleanField(default=False)
	can_use_giver_name = models.BooleanField(default=False)
	summarize_only = models.BooleanField(default=False)
	coach_chat_before_delivery = models.BooleanField(default=False)
	best_judgement = models.BooleanField(default=False)


class Feedback(models.Model):
	date_given = models.DateTimeField(auto_now=True, blank=True)
	feedback = models.TextField(null=True, blank=True)
	recipient = models.ForeignKey(FeedbackRecipient, default="")
	giver = models.ForeignKey(FeedbackGiver, default="")
	fool_numerical_recommendation = models.PositiveIntegerField(choices=NUMERICAL_SCALE, null=True, blank=True)
	top_of_game_description = models.TextField(null=True, blank=True)
	next_level = models.TextField(null=True, blank=True)