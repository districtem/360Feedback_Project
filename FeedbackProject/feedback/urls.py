from django.conf.urls import patterns, url

from feedback.views import BaseFeedbackView, ChooseCoachView, SendInvitesView, SendFeedbackView

urlpatterns = patterns('',
    url(r'^$', BaseFeedbackView.as_view(), name='index'),
    url(r'^receive/(?P<pk>[\d-]+)', ChooseCoachView.as_view(), name='receive'),
    url(r'^receive/send_invites/(?P<pk>[\d-]+)', SendInvitesView.as_view(), name='send_invites'),
    url(r'^send', SendFeedbackView.as_view(), name='send'),
)