"""django_bookmarks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from bookmarks.views import *
from django.views.generic import TemplateView

urlpatterns = [
    # Browsing
    url(r'^$', main_page, name='main_page'),
    url(r'^user/(\w+)/$', user_page, name='user_page'),    
    url(r'^admin/', admin.site.urls),
    url(r'^tag/([^\s]+)/$', tag_page, name='tag_page'),
    url(r'^tag/$', tag_cloud_page, name='tag_cloud_page'),
    url(r'^search/$', search_page, name='search_page'),

    # Session management
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', logout_page, name='logout_page'),    
    url(r'^register/$', register_page, name='register_page'),
    url(r'^register/success/$', TemplateView.as_view(template_name="registration/register_success.djhtml")),

    # Account management
    url(r'^save/$', bookmark_save_page, name='bookmark_save_page'),
]
