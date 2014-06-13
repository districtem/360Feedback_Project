from django import forms

from feedback.models import Feedback, FeedbackRecipient, FeedbackGiver


class CoachForm(forms.ModelForm):
	class Meta:
		model = FeedbackRecipient
		fields = ['coach']

	def notify_coach(coach):
		pass

class FeedbackForm(forms.ModelForm):
	class Meta:
		model = Feedback
		fields = []