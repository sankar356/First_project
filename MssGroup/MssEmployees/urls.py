
from django.urls import path
from MssEmployees import views as v1
urlpatterns = [
    # path('index/', v1.index),
    # path('adm/', v1.newAdmin),
    # path('user', v1.user),
    # path('master', v1.master),
    path('login/', v1.login, name='register'),
    path('register/', v1.Register),
    path('layout-default/', v1.layout_default),
    path('layout-top/', v1.layout_top),
    path('blank-pages/', v1.blank_pages),
    path('', v1.homePage, name="/index"),
    path('index', v1.homePage),

]
