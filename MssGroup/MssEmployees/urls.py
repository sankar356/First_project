
from django.urls import path
from MssEmployees import views as v1
urlpatterns = [
    # path('index/', v1.index),
    # path('adm/', v1.newAdmin),
    # path('user', v1.user),
    # path('master', v1.master),
    path('login/', v1.login, name='register'),
    path('register/', v1.Register),
    path('', v1.homePage),

]
