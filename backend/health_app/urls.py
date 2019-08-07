from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[

    url('^$',views.welcome,name='welcome'),
    url(r'^new/profile/$', views.new_profile, name='new-profile'),    
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^scan/$',views.scan,name='scan'),
    url(r'^del/(\d+)$',views.delete_item,name='delete'),
    url(r'stats/$',views.stats,name='stats'),
    # * urls for the api
    url(r'^api/profile/$',views.ProfileList.as_view()),
    url(r'^api/original/$',views.OriginalList.as_view()),
    url(r'^api/extracts/$',views.ExtractedList.as_view()),
    url(r'^api/users/$',views.UserList.as_view()),
    url(r'api/prof/prof-id/(?P<pk>[0-9]+)/$',views.ProfileDescr.as_view()),
    url(r'api/ori/ori-id/(?P<pk>[0-9]+)/$',views.OriginalDescr.as_view()),
    url(r'api/extract/extract-id/(?P<pk>[0-9]+)/$',views.ExtractDescr.as_view()),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
