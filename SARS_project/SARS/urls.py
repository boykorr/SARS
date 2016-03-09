from django.conf.urls import patterns, url
from SARS import views
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', views.query_construction, name='query_construction'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^abstractevaluation/$', views.abstract_evaluation, name='abstract_evaluation'),
    )
if not settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

