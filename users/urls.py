from django.conf.urls import url
from users import views

urlpatterns = [
    url(r'^app/user$', views.users_create),
    url(r'^app/user/auth$', views.users_login),
    url(r'^app/sites/list/(?P<user>\[0-9]+)$', views.users_notes),
    # url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    # url(r'^api/tutorials/published$', views.tutorial_list_published)
]