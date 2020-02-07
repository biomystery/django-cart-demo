from django.conf.urls import url
from core import views
app_name = 'core'

urlpatterns = [

    url(r'^$', views.ProductListView.as_view(), name='list'),
    url(r'^register/$', views.register, name='register'),
    url(r'^(?P<pk>\d+)/$', views.ProductDetailView.as_view(), name='detail'),
    url(r'^create/$', views.ProductCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/$', views.ProductUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', views.ProductDeleteView.as_view(), name='delete'),
    url(r'^category_list$', views.CategoryListView.as_view(), name='category_list'),
    url(r'^(?P<pk>\d+)/$', views.CategoryDetailView.as_view(), name='detail'),
    url(r'^create/$', views.CategoryCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/$', views.CategoryUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', views.CategoryDeleteView.as_view(), name='delete'),
    url(r'^$', views.UserProfileListView.as_view(), name='profile_list'),
    url(r'^(?P<pk>\d+)/$', views.UserProfileDetailView.as_view(), name='profile_detail'),
    url(r'^create/$', views.UserProfileCreateView.as_view(), name='profile_create'),
    url(r'^update/(?P<pk>\d+)/$', views.UserProfileUpdateView.as_view(), name='profile_update'),
    url(r'^delete/(?P<pk>\d+)/$', views.UserProfileDeleteView.as_view(), name='profile_delete'),

]
