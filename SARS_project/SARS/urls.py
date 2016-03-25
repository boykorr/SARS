from django.conf.urls import patterns, url
from SARS import views
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^basicsearch/$', views.basic_query, name='basic_search'),
    url(r'^advancedsearch/$', views.advanced_query, name='advanced_search'),
    url(r'^userguide/$', views.user_guide, name='user_guide'),
    url(r'^reviews/$', views.reviews, name='reviews'),
    url(r'^abstractevaluation/$', views.abstract_evaluation, name='abstract_evaluation'),
    url(r'^documentevaluation/$', views.document_evaluation, name='document_evaluation'),
    url(r'^documentresults/$', views.document_results, name='document_results'),
    url(r'^successfulregistration/$', views.successful_registration, name='registration_register'),
    )

if not settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
