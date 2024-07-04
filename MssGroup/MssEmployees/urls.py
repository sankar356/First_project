
from django.urls import path
from MssEmployees import views as v1
urlpatterns = [
    path('hi/', v1.index),
    path('adm/', v1.newAdmin),
    path('user', v1.user),
    path('master', v1.master),
    path('user_register/', v1.user_register, name='register'),
    path('register/', v1.Register, name='data'),

]
