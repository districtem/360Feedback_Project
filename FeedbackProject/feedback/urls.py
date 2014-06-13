from django.conf.urls import patterns, url

from feedback.views import BaseFeedbackView, GetFeedbackView, GiveFeedbackView

urlpatterns = patterns('',
    url(r'^$', BaseFeedbackView.as_view(), name='index'),
    url(r'^get_feedback/', GetFeedbackView.as_view(), name='get_feedback'),
    url(r'^give_feedback/', GiveFeedbackView.as_view(), name='give_feedback'),
)