"""
TWLight URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
"""

from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView


from TWLight.applications.urls import urlpatterns as applications_urls
from TWLight.graphs.urls import csv_urlpatterns as csv_urls
from TWLight.graphs.views import DashboardView
from TWLight.resources.urls import urlpatterns as partners_urls
from TWLight.users import authorization as auth
from TWLight.users.urls import urlpatterns as users_urls
from TWLight.users.views import TermsView

from .views import HomePageView


urlpatterns = [
	# Built-in -----------------------------------------------------------------
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/', auth_views.login, name='auth_login'),
    url(r'^accounts/logout/',
        auth_views.logout,
        {'next_page': '/'},
        name='auth_logout'),
    url(r'^password/change/$',
        auth_views.password_change,
        {'post_change_redirect': 'users:home'},
        name='password_change'),
    url(r'^password/reset/$',
        auth_views.password_reset,
        {'post_reset_redirect': 'users:home'},
        name='password_reset'),

    # This makes the set language URL available.
    url(r'^i18n/', include('django.conf.urls.i18n')),

    # Third-party --------------------------------------------------------------
    url(r'^comments/', include('django_comments.urls')),
    url(r'^autocomplete/', include('autocomplete_light.urls')),

    # TWLight apps -------------------------------------------------------------
    url(r'^users/', include(users_urls, namespace="users")),
    url(r'^applications/', include(applications_urls, namespace="applications")),
    url(r'^partners/', include(partners_urls, namespace="partners")),
    url(r'^csv/', include(csv_urls, namespace="csv")),

    # Other TWLight views
    url(r'^oauth/login/$',
        auth.OAuthInitializeView.as_view(),
        name='oauth_login'),
    url(r'^oauth/callback/$',
        auth.OAuthCallbackView.as_view(),
        name='oauth_callback'),

    url(r'^dashboard/$', DashboardView.as_view(), name='dashboard'),
    url(r'^terms/$', TermsView.as_view(), name='terms'),
    url(r'^$', HomePageView.as_view(), name='homepage'),
    url(r'^about/$',
        TemplateView.as_view(template_name='about.html'),
        name='about'),
]
