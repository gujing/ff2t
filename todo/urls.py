from django.conf.urls import patterns, url

from todo import views

__author__ = 'Gin'

urlpatterns = patterns('',
	url(r'^$', views.IndexView.as_view(), name='index')
	# url(r'^(?P<task_id>\d+)/$', views.get_task, name='detail'),
	# url(r'^all/$', views.get_all_task, name='all'),
	# url(r'^add/$', views.add_task, name='add')
)