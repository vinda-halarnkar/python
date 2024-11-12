from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_view, name='list_view'),
    path('add_list/', views.add_list, name='add_list'),
    path('add_item/', views.add_item, name='add_item'),
    path('mark_item_complete/<int:item_id>/', views.mark_item_complete, name='mark_item_complete'),
    path('delete_list/<int:list_id>/', views.delete_list, name='delete_list'),
    path('list_detail/<int:list_id>/<str:sort_order>/', views.list_detail, name='list_detail'),
    path('delete_item/<int:item_id>/', views.delete_item, name='delete_item'),
    path('delete_item/<int:item_id>/', views.delete_item, name='delete_item'),

    #api paths
    path('get-lists/', views.get_list, name="get_lists"),
    path('get-lists/', views.get_list, name='get_list'),
    # path('<int:list_id>/item/add/', views.add_item),
    # path('<int:list_id>/delete/', views.delete_list),
    # path('sort/<str:order>/', views.sort_lists),
    # path('<int:list_id>/items/', views.get_items),
]