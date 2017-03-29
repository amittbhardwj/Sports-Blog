from django.conf.urls import patterns, include, url
from blog.views import *
from django.contrib.auth.views import login, logout
from django.contrib import admin
from score.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = patterns('',url(r'^home/$',show),url(r'^register/$',register),(r'^getoptional/$',getoptional),(r'^check/(?P<status>.*)/$',check),
	url(r'^write/',writepost),(r'^saveinfo/$',saveoptional),url(r'^ajax/hit/$',show,name='hitcount_update_ajax'),
	url(r'^registration/$',registration),url(r'^logout/',logout),url(r'^follow/(?P<name>.*)/(?P<status>.*)/$',follow),
	url(r'^changed/$',changepassword),url(r'changepassword/',change),url(r'^boom/',boom),url(r'^lol/',lol),
	(r'^profile/(?P<name>.*)/(?P<title>.*)/$', displaypost),url(r'^dashboard/',dashboard),url(r'^success/(?P<value>.*)/',createpost),
	(r'^admin/', include('django.contrib.auth.urls')),(r'^comments/',include('django.contrib.comments.urls')),
	(r'^profile/$', login),(r'^login/$', login_page),(r'^profile/(?P<name>.*)/$', publicprofile),
	 url(r'^saveimage/',saveimage), 
    # Examples:
    # url(r'^$', 'score.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)