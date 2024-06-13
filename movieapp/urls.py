from django.urls import path

from movieapp import views

urlpatterns = [
    # admin page urls
    path('addmovie',views.addmovie_fun,name='addmovie'),
    path('showtime',views.showtime_fun,name='showtime'),
    path('displaymovie',views.displaymovie_fun,name='displaymovie'),
    path('bookingdetails',views.bookingdetails_fun,name='bookingdetails'),
    path('updatestatus/<int:id>',views.updatestatus,name='updatestatus'),

    path('reg',views.reg_fun,name='reg'),
    path('log',views.log_fun,name='log'),

    # customer page urls
    path('home',views.home_fun,name='home'),
    path('showdata',views.showdata_fun,name='showdata'),
    path('bookshow/<int:showid>',views.bookshow_fun,name='bookshow'),
    path('cencelbooking/<int:id>',views.cancel_booking,name='cancelbooking')


]