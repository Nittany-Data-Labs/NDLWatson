from django.conf.urls import url

from . import views

app_name = 'journal_app'
urlpatterns = [
    # ex: /journal_app/
    url(r'^$', views.index, name='index'),
    # ex: /journal_app/1/
    url(r'^(?P<journal_entry_id>[0-9]+)/$', views.detail, name = 'detail'),
    # ex: /journal_app/1/recordentry/
    url(r'^record_entry/$', views.record_entry, name = 'record_entry'),

    url(r'^submit_entry/$', views.submit_entry, name='submit_entry')
]
