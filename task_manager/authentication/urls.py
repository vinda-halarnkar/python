from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout,  name='logout'),
    # path('list/create/', views.create_list),
    # path('list/<int:list_id>/item/add/', views.add_item),
    # path('item/<int:item_id>/complete/', views.mark_item_complete),
    # path('item/<int:item_id>/delete/', views.delete_item),
    # path('list/<int:list_id>/delete/', views.delete_list),
    # path('list/sort/<str:order>/', views.sort_lists),
    # path('list/<int:list_id>/items/', views.get_items),
]