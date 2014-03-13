from django.conf.urls import patterns, url

from imgVerification import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^send_img$', views.send_img, name='send_img'),
    url(r'^submit$', views.submit, name='submit')
)
