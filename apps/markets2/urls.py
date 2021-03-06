from django.conf.urls import url
from . import views

app_name = 'markets2'

urlpatterns = [
    url(r'^$', views.HomepageView.as_view(), name='home2'),
    url(r'^regions/$', views.RegionChoiceView.as_view(), name='region-choice'),
    url(r'^markets/$', views.MarketListView.as_view(), name='list'),
]
