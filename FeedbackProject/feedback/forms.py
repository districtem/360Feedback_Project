import functools
from django.forms.models import inlineformset_factory, modelformset_factory
from django import forms
from django.forms import widgets

from feedback.models import Employee, Feedback, FeedbackRequest


class ReceiveFeedbackForm(forms.ModelForm):
	class Meta:
		model = Employee
		widgets = {
			'user': widgets.HiddenInput(),
            'coach': widgets.Select(),
            'is_coach': widgets.HiddenInput()
        }

	def notify_coach(coach):
		pass

FeedbackRequestFormset = modelformset_factory(FeedbackRequest, extra=3)