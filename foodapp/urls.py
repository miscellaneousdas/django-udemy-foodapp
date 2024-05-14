from . import views
from django.urls import path

#namespace
app_name = 'foodapp'

urlpatterns = [
    #/foodapp/
    path('', views.index, name='index'),
    #/foodapp/1/
    path('<int:item_id>/', views.detail, name='detail'),
    path('item/', views.item, name='item'),
    
]
