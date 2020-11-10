from django.urls import path
from . import views

urlpatterns = [
    path('signup',views.signup,name='GouSignup'),
    path('login',views.userlogin,name='GouLogin'),
    path('logout/',views.userlogout,name='GouLogout'),
    path('', views.home, name='GouHome'),
    path('about/', views.about, name='GouAbout'),
    path('contact/', views.contact, name='GouContact'),
    path('track/', views.track, name='GouTrack'),
    path('search/', views.search, name='search'),
    path('productview/<int:myid>', views.productview, name='Gouproductview'),
    path('checkout/', views.checkout, name='GouCheckout'),

]
