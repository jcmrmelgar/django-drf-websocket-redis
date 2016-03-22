from django.conf.urls import url, include
from . import api, views

urlpatterns = [
	# API Urls
	url(r'^api/', include(api.router.urls)),
	url(r'^api/', include(api.canal_router.urls)),
	# Views Urls
	url(r'^$', views.Canales.as_view(), name='canales'),
	url(r'^(?P<slug>[\w-]+)/$', views.Canal.as_view(), name='canal'),
]