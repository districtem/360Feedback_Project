from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, ModelFormMixin, UpdateView, FormView

from feedback.models import Employee, Feedback, FeedbackGiver, FeedbackRecipient
from feedback.forms import CoachForm, FeedbackInviteForm, FeedbackFormset


class BaseFeedbackView(TemplateView):
	template_name = 'feedback/index.html'
	

class ChooseCoachView(UpdateView):
	model = Employee
	form_class = CoachForm
	template_name = 'feedback/receive.html'

	def get_initial(self):
		initial = super(ChooseCoachView, self).get_initial()
		initial['recipient'] = Employee.objects.get(id=self.kwargs['pk'])
		return initial

	def form_valid(self, form):
		form.notify_coach()
		return super(ChooseCoachView, self).form_valid(form)

	def get_success_url(self):
		return '/feedback/receive/send_invites/'+ self.kwargs['pk']



class SendInvitesView(CreateView):
	model = FeedbackRecipient
	form_class = FeedbackInviteForm
	template_name = 'feedback/send_invites.html'
	success_url = '/feedback'

	def get_initial(self):
		initial = super(SendInvitesView, self).get_initial()
		initial['invite_sender'] = FeedbackRecipient.objects.get(id=self.kwargs['pk'])
		return initial

	def form_valid(self, form):
		form.send_invite()
		return super(SendInvitesView, self).form_valid(form)


class SendFeedbackView(CreateView):
	form_class = FeedbackFormset
	template_name = 'feedback/feedback_form.html'











