from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from mentor.models import ContactForm

urlpatterns = patterns('',
    url(r'^', 'mentor.views.mentor'),
)

