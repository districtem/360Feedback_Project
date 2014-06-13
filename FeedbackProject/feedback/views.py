from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import FormView

from feedback.models import Feedback, FeedbackGiver, FeedbackRecipient
from feedback.forms import CoachForm


class BaseFeedbackView(generic.TemplateView):
	template_name = 'feedback/index.html'
	

class GetFeedbackView(generic.FormView):
	form_class = CoachForm
	template_name = 'feedback/get_base.html'
	success_url = 'feedback/get_givers.html'

	def form_valid(self, form):
		form.notify_coach()
		return super(GetFeedbackView, self).form_valid(form)


class GiveFeedbackView(generic.TemplateView):
	model = FeedbackGiver
	template_name = 'feedback/give_base.html'