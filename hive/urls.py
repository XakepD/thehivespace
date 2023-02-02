from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name ="home"),
    path('home', views.home, name ="nhome"),
    path('register', views.signup, name ="register"),
    path('login', views.signin, name ="login"),
    path('profile/', views.Profile.as_view(), name ="profile"),
    path('account/', views.Account.as_view(), name ="account"),
    path('category/<slug:val>', views.Category.as_view(), name ="category"),
    path('search/<slug:val>', views.Filter.as_view(), name ="search"),
    path('product-detail/<int:pk>', views.Productdetail.as_view(), name ="product-detail"),
]

