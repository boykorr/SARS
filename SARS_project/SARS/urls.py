from django.conf.urls import patterns, url
from SARS import views
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^basic_search/$', views.basic_query, name='basic_search'),
    url(r'^advanced_search/$', views.advanced_query, name='advanced_search'),
    url(r'^user_guide/$', views.user_guide, name='user_guide'),
    #url(r'^register/$', views.register, name='register'),
    #url(r'^login/$', views.user_login, name='login'),
    #url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^abstractevaluation/$', views.abstract_evaluation, name='abstract_evaluation'),
    url(r'^documentevaluation/$', views.document_evaluation, name='document_evaluation'),
    #url(R'^accounts/register/$', views.successful_registration, name='registration_register'),
    url(r'^successfulregistration/$', views.successful_registration, name='registration_register'),
    )

if not settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
