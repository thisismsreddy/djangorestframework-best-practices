from django.conf.urls import include, url
from .views import PersonView

urlpatterns = [

    url(r'^$', PersonView.as_view(), name='person')
]
