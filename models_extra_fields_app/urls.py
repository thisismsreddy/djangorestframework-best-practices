from django.conf.urls import include, url
from .views import PersonView,PersonDetailView

urlpatterns = [

    url(r'^$', PersonView.as_view(), name='person'),
    url(r'^person_details/(?P<pk>[0-9]+)/$', views.PersonDetailView.as_view(),name='person_details'),

]
