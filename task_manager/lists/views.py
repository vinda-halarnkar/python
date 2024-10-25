from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# from .models import List, Item
import json


# Create your views here.
# @login_required
def list_view(request):
    return render(request, 'list/view_list.html')


# Create List
# @login_required
# def list_create(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         name = data.get('name')
#         if not name:
#             return JsonResponse({"error": "List name is required."}, status=400)
#         new_list = List.objects.create(name=name, user=request.user)
#         return JsonResponse({"message": "List created successfully.", "list_id": new_list.id})
#     return render(request, 'lists/list_create.html')
#
# # List Detail with Items
# @login_required
# def list_detail(request, list_id):
#     list_obj = get_object_or_404(List, id=list_id, user=request.user)
#     if request.method == 'POST':
#         item_name = request.POST.get('name')
#         if item_name:
#             Item.objects.create(name=item_name, list=list_obj)
#             return redirect('list_detail', list_id=list_obj.id)
#     return render(request, 'lists/list_detail.html', {'list': list_obj, 'items': list_obj.items.all()})
#
# # Mark Item as Completed
# @login_required
# def mark_item_complete(request, item_id):
#     item = get_object_or_404(Item, id=item_id, list__user=request.user)
#     item.completed = True
#     item.save()
#     return redirect('list_detail', list_id=item.list.id)
#
# # Delete List
# @login_required
# def delete_list(request, list_id):
#     list_obj = get_object_or_404(List, id=list_id, user=request.user)
#     list_obj.delete()
#     return redirect('list_index')
#
# # List Index with Sorting
# @login_required
# def list_index(request):
#     order = request.GET.get('order', 'asc')
#     lists = List.objects.filter(user=request.user).order_by('name' if order == 'asc' else '-name')
#     return render(request, 'lists/list_index.html', {'lists': lists, 'order': order})


# @login_required
# @csrf_exempt
# def create_list(request):
#     data = json.loads(request.body)
#     list_name = data.get('name')
#     new_list = List.objects.create(user=request.user, name=list_name)
#     return JsonResponse({"message": "List created", "list_id": new_list.id})
#
# @login_required
# @csrf_exempt
# def add_item(request, list_id):
#     data = json.loads(request.body)
#     item_name = data.get('name')
#     list_obj = List.objects.get(id=list_id, user=request.user)
#     Item.objects.create(list=list_obj, name=item_name)
#     return JsonResponse({"message": "Item added to list"})
#
# @login_required
# @csrf_exempt
# def mark_item_complete(request, item_id):
#     item = Item.objects.get(id=item_id, list__user=request.user)
#     item.completed = True
#     item.save()
#     return JsonResponse({"message": "Item marked as completed"})
#
# @login_required
# @csrf_exempt
# def delete_item(request, item_id):
#     item = Item.objects.get(id=item_id, list__user=request.user)
#     item.delete()
#     return JsonResponse({"message": "Item deleted"})
#
# @login_required
# @csrf_exempt
# def delete_list(request, list_id):
#     list_obj = List.objects.get(id=list_id, user=request.user)
#     list_obj.delete()
#     return JsonResponse({"message": "List deleted"})
#
# @login_required
# def sort_lists(request, order):
#     lists = List.objects.filter(user=request.user).order_by('name' if order == 'asc' else '-name')
#     return JsonResponse({"lists": [list.name for list in lists]})
#
# @login_required
# def get_items(request, list_id):
#     list_obj = List.objects.get(id=list_id, user=request.user)
#     items = list_obj.items.all()
#     return JsonResponse({"items": [{"name": item.name, "completed": item.completed} for item in items]})