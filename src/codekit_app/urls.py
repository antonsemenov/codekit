from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from app import views

admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.home),
    # url(r'^codekit_app/', include('codekit_app.foo.urls')),
    url(r'^task/(\w+)/(\d+)/$', views.task_view, {'GET': views.task_view_get, 'POST': views.task_view_post}),
    #url(r'^task/python/1/', views.task_view, {'GET': views.task_view_get, 'POST': views.task_view_post}),
    # url(r'^codekit_app/', include('codekit_app.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('', (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
