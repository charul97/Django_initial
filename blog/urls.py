from django.conf.urls import include,url
from django.contrib import admin
from blog import views


from blog.views import (
    blog_list,
    blog_create,
    blog_detail,
    blog_update,
    blog_delete,
    )

#router.register(r'Post',views.PostSet)

urlpatterns = [
#    url(r'^admin/', admin.site.urls),
#    url(r'^charul/', views.blog_home),
    url(r'^create/', blog_create),
    url(r'^(?P<id>\d+)/$', blog_detail, name='detail'),
    url(r'^$', blog_list, name='list'),
    url(r'^(?P<id>\d+)/edit/$', blog_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', blog_delete),
#    url(r'^template/', views.blog_template),
#    url(r'^db/',include(router.urls)),
]