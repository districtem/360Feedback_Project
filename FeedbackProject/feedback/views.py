from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, ModelFormMixin, UpdateView, FormView, ModelFormMixin

from feedback.models import Employee, Feedback, FeedbackRequest
from feedback.forms import ReceiveFeedbackForm, FeedbackRequestFormset


class FeedbackRequestMixin(ModelFormMixin):
	form_class = FeedbackRequestFormset


class BaseFeedbackView(TemplateView):
	template_name = 'feedback/index.html'
	

class ReceiveFeedbackView(CreateView):
	form_class = ReceiveFeedbackForm
	initial = {
	'is_coach' : False,
	}
	template_name = 'feedback/receive.html'
	success_url = '/feedback'



class SendFeedbackView(CreateView):
	template_name = 'feedback/feedback_form.html'











