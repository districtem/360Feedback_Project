import functools
from django.forms.models import inlineformset_factory
from django import forms
from django.forms import widgets

from feedback.models import Employee, Feedback, FeedbackRecipient, FeedbackGiver, FeedbackInvitation


class CoachForm(forms.ModelForm):
	class Meta:
		model = FeedbackRecipient
		widgets = {
			'recipient': widgets.Select(),
            'coach': widgets.Select(),
        }

	def notify_coach(coach):
		pass


class FeedbackInviteForm(forms.ModelForm):
	class Meta:
		model = FeedbackInvitation
		widgets = {
			'invite_sender': widgets.Select(),
			'invite_accepted': widgets.HiddenInput(),
            'invite_receiver': widgets.Select(),
        }

	def send_invite(invitee):
		pass


FeedbackFormset = inlineformset_factory(FeedbackGiver, Feedback, extra=1, widgets={'fool_numerical_recommendation': widgets.RadioSelect()})