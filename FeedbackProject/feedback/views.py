from django.shortcuts import render
from django.views import generic

from feedback.models import Feedback, FeedbackGiver, FeedbackRecipient


class BaseFeedbackView(generic.TemplateView):
	template_name = 'feedback/index.html'


