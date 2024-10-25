from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_view, name='list_view'),  # Ensure this is correct
    # path('create/', views.create_list),
    # path('<int:list_id>/item/add/', views.add_item),
    # path('<int:list_id>/delete/', views.delete_list),
    # path('sort/<str:order>/', views.sort_lists),
    # path('<int:list_id>/items/', views.get_items),
]