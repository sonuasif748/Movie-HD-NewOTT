from django.urls import path
from dashboard import views

urlpatterns = [
    path('dash',views.dash,name='dash'),
    path('list',views.movies_list,name='list'),
    path('addmovie',views.addmovie,name='addmovie'),
    path('user',views.users,name='user'),
    path('comnt',views.comment,name='comnt'),
    path('payments_history',views.payments,name='payments'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('admin_reg',views.admin_reg,name='admin_reg'),
    path('update_status/<int:status>/<int:id>', views.update_status, name='update_status'),
    path('logout_user',views.logout_user,name='logout_user'),
    # path('update',views.update,name='update'),
    path('pub_update_movie-<int:id>/',views.pub_update_movie, name='pub_update_movie'),
    path('pub_delete_movie-<int:id>/',views.pub_delete_movie, name='pub_delete_movie'),
    path('searchbar/',views.search,name='search'),

    path('deleteuser-<int:id>/',views.delete_user,name='delete_user'),
    path('updateuser<int:id>/',views.update_user,name='update_user'),
    path('test/',views.test1,name='test'),

]