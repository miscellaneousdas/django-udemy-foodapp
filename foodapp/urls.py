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
    #Add item
    path('add/', views.create_item, name='create_item'),
    #Edit item
    path('update/<int:id>/', views.update_item, name='update_item'),
    #Delete item
    path('delete/<int:id>/', views.delete_item, name='delete_item')
]
