from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^api/profile/$',views.ProfileList.as_view()),
    url(r'^api/original/$',views.OriginalList.as_view()),
    url(r'^api/extracts/$',views.ExtractedList.as_view()),
    url(r'^api/users/$',views.UserList.as_view()),
    url(r'api/prof/prof-id/(?P<pk>[0-9]+)/$',views.ProfileDescr.as_view()),
    url(r'api/ori/ori-id/(?P<pk>[0-9]+)/$',views.OriginalDescr.as_view()),
    url(r'api/extract/extract-id/(?P<pk>[0-9]+)/$',views.ExtractDescr.as_view()),
]