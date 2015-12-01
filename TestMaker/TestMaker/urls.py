'''
testMaker/urls.py
'''

from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from testMaker.models import Test

urlpatterns = patterns('',
                       url(r'^', ListView.as_view(
                           queryset=Test.objects.all().order_by("-date")[:10],
                           template_name="testMaker.html")),

                       )