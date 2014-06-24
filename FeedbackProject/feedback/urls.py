from django.conf.urls import patterns, url

from feedback.views import BaseFeedbackView, ReceiveFeedbackView, SendFeedbackView

urlpatterns = patterns('',
    url(r'^$', BaseFeedbackView.as_view(), name='index'),
    url(r'^receive', ReceiveFeedbackView.as_view(), name='receive-feedback'),
    url(r'^send', SendFeedbackView.as_view(), name='send-feedback'),
)