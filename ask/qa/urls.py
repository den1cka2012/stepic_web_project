"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from qa.views import test, login_add, signup_add, question, ask_add, answer_add, popular, new, qa_list_all, qa_popular_all

urlpatterns = [
    url(r'^$', qa_list_all, name='main'),
    url(r'^\?page=(?P<page>\d+)', qa_list_all, name='main'),
    url(r'^test/', test, name='test'),
    url(r'^login/', login_add, name='login'),
    url(r'^signup/', signup_add, name='signup'),
    url(r'^question/(?P<id>\d+)/', question, name='question'),
    url(r'^ask/', ask_add, name='ask'),
    url(r'^answer/', answer_add, name='answer'),
    url(r'^popular/', qa_popular_all, name='popular'),
    url(r'^popular/\?page=(?P<page>\d+)', qa_popular_all, name='popular'),
    url(r'^new/', new, name='new'),
]

