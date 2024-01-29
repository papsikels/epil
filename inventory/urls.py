from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="homepage"),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('EditProfile/', views.edit_profile, name='editprofile'),
    path("login/", views.Login, name="Login"),
    path("register/", views.register, name="register"),
    path("Child-Costume/", views.child, name="childpage"),
    path("Adult-Costume/", views.adult, name="adultpage"),
    path('toggle-bookmark/<int:costume_id>/', views.toggle_bookmark, name='toggle_bookmark'),
    path('bookmarked-costumes/', views.bookmarked_costumes, name='bookmarked'),
    path('product/<int:costume_id>/', views.product, name='product'),
    path('update-product/<int:pk>/', views.update_product, name='update_product'),
    path('delete-product/<int:pk>/', views.delete_product, name='delete_product'),

]

