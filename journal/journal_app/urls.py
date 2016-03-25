from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /journal_app/
    url(r'^$', views.index, name='index'),
    # ex: /journal_app/1/
    url(r'^(?P<journal_entry_id>[0-9]+)/$', views.detail, name = 'detail'),
    # ex: /journal_app/1/recordentry/
    url(r'^(?P<journal_entry_id>[0-9]+)/recordentry/$', views.recordentry, name = 'recordentry'),
]
