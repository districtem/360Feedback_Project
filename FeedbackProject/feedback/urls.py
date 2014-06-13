from django.conf.urls import patterns, url

from feedback.views import BaseFeedbackView

urlpatterns = patterns('',
    url(r'^$', BaseFeedbackView.as_view(), name='index'),
    url(r'^/get_feedback/', )
)