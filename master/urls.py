from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^mainpage' , views.main_page,name='main_page'),
    url(r'^result_page' , views.result_page,name='result_page'),
    url(r'^userpage', views.user_page, name='user_page'),
    url(r'^certificate',views.certificate_page,name='certificate_page'),
    url(r'^teacher_page',views.teacher_page,name='teacher_page'),
    url(r'^users', views.user,name='users'),

]