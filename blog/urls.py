from django.conf.urls import include, url
from django.contrib import admin
from app import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.BlogIndex.as_view(), name="index"),
    url(r'^entry/(?P<slug>\S+)$', views.BlogDetail.as_view(), name="entry_detail"),
    url('^markdown/', include( 'django_markdown.urls'))

]
