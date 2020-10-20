from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index,name="first_page"),
    path('<int:item_id>/',views.detail,name="details"),
    path('select_food',views.veg,name="home"),
    path('non_veg',views.non_veg),
    path('add',views.create,name="add"),
    path('update/<int:id>',views.update,name="update")
    
    
    
]
