
from django.urls import path
from publisher import  views

urlpatterns = [
    path('padd',views.publisher_add,name='padd'),
    path('publisher',views.publish,name="publish"),
    path('publist',views.publist,name="publist"),
    path('pub_login',views.pub_login,name='pub_login'),
    path('pub_reg',views.pub_reg,name='pub_reg'),

]