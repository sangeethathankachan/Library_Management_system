from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.index,name='index'),
    #path('index',views.index,name='index'),
    path('adminindex',views.adminindex,name='adminindex'),
    path('mylibrary',views.mylibrary,name='mylibrary'),
    path('addcategory',views.addcategory,name='addcategory'),
    path('addbook',views.addbook,name='addbook'),
    path('showbooks',views.showbooks,name='showbooks'),
    path('editdetails/<int:pk>',views.editdetails,name='editdetails'),
    path('deletedetails/<int:pk>',views.deletedetails,name='deletedetails'),
    path('logout',views.logout,name='logout'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('signup',views.signup,name='signup'),
    path('login_user',views.login_user,name='login_user'),
    path('cartitem/<int:pk>/<int:k>/',views.cartitems,name='cartitem'),
    path('details/<int:pk>/<int:k>/',views.details,name='details'),
    path('profile/<int:pk>',views.profile,name='profile'),
    path('showuser',views.showuser,name='showuser'),
    path('edituser/<int:pk>',views.edituser,name='edituser'),
    path('items',views.items,name='items'),
    path('deleteuser/<int:pk>',views.deleteuser,name='deleteuser'),
    path('edituser/<int:pk>',views.edituser,name='edituser'),
    path('loadcartitems/<int:pk>',views.loadcartitems,name='loadcartitems'),
    path('deleteitem/<int:pk>',views.deleteitem,name='deleteitem'),
    path('issue',views.issue,name='issue'),
    path('viewissue/<int:pk>',views.viewissue,name='viewissue'),
    path('shcategory',views.shcategory,name='shcategory'),
    path('deletecat/<int:pk>',views.deletecat,name='deletecat'),
    path('viewadminis',views.viewadminis,name='viewadminis')
    
]