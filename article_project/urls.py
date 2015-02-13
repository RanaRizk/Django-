from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'article_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^reg/$','article.views.reg'),
    url(r'^save/$','article.views.save'),
    url(r'^check/$','article.views.check'),
    url(r'^articles/all/$','article.views.articles'),
    url(r'^article/get/(?P<article_id>\d+)/$','article.views.article'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^checkfb/$','article.views.checkfb'),
    url(r'^home/$','article.views.home'),
    url(r'^savefb/$','article.views.savefb'),
    url(r'^savefblogin/$','article.views.savefblogin'),
    url(r'^login/$','article.views.login'),
    url(r'^logout/$','article.views.logout'),
    url(r'^like/(?P<article_id>\d+)/$','article.views.likeArticle'),
    url(r'^unlike/(?P<article_id>\d+)/$','article.views.unlikeArticle'),
    url(r'^comments/$','article.views.comments'),
    #url(r'^profile/$', 'article.views.profile'),
    #url(r'^changeSetting/$', 'article.views.changeSetting'),
]
