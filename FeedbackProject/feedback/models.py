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

class Employee(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	is_coach = models.BooleanField()
	is_available_to_coach = models.BooleanField(default=False)
	email = models.EmailField(max_length=75, null=True, blank=True)

	def __unicode__(self):
		return self.first_name + ' ' + self.last_name


class FeedbackRecipient(models.Model):
	recipient = models.ForeignKey(Employee, default="")
	coach = models.ForeignKey(Employee, default="This Fool does not yeat have a feedback coach", 
		limit_choices_to={'is_coach': True}, related_name='RecipientCoach'
	)

	def __unicode__(self):
		return self.recipient.__unicode__()


class FeedbackGiver(models.Model):
	giver = models.ForeignKey(Employee, default="")
	can_quote_giver = models.BooleanField(default=False)
	can_use_giver_name = models.BooleanField(default=False)
	summarize_only = models.BooleanField(default=False)
	coach_chat_before_delivery = models.BooleanField(default=False)
	best_judgement = models.BooleanField(default=False)

	def __unicode__(self):
		return 'Feedback Recipient:' + self.feedback.recipient.__unicode__() + 'Feedback Giver:' + self.giver.__unicode__()


class Feedback(models.Model):
	date_given = models.DateTimeField(auto_now=True, blank=True)
	recipient = models.ForeignKey(FeedbackRecipient, default="")
	giver = models.ForeignKey(FeedbackGiver, default="")
	fool_numerical_recommendation = models.PositiveIntegerField(choices=NUMERICAL_SCALE, null=True, blank=True)
	top_of_game_description = models.TextField(null=True, blank=True)
	next_level = models.TextField(null=True, blank=True)





class FeedbackInvitation(models.Model):
	invite_sender = models.ForeignKey(FeedbackRecipient)
	invite_receiver = models.ForeignKey(Employee)
	invite_accepted = models.BooleanField(default=False)





