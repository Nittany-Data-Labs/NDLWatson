from django.conf.urls import url

from . import views

app_name = 'journal_app'
urlpatterns = [
    # ex: /journal_app/
    url(r'^$', views.index, name='index'),
    url(r'^(?P<journal_entry_id>[0-9]+)/$', views.detail, name = 'detail'),
    url(r'^record_entry/$', views.record_entry, name = 'record_entry'),
    url(r'^submit_entry/$', views.submit_entry, name='submit_entry'),
    url(r'^view_registration/$', views.view_registration, name = 'view_registration'),
    url(r'^submit_registration$', views.submit_registration, name='submit_registration'),
    url(r'^view_login/$', views.view_login, name='view_login'),
    url(r'^submit_login/$', views.submit_login, name = 'submit_login'),
    url(r'^user_logout/$', views.user_logout, name = 'user_logout')
]
