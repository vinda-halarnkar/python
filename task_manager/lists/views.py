from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import ListForm, ItemForm
from .models import List, Item

# Create your views here.
@login_required
def list_view(request):
    lists = List.objects.filter(user=request.user)
    #get forms
    form = ListForm()
    return render(request, 'list/view_list.html',
                  {'lists': lists, 'form': form})
# Create List
@login_required
def add_list(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        if not name:
            return JsonResponse({"error": "List name is required."}, status=400)
        new_list = List.objects.create(name=name, user=request.user)
        return JsonResponse({"message": "List created successfully.", "list_id": new_list.id})

    return JsonResponse({'error': 'Invalid request'}, status=400)

@login_required
def add_item(request):
    data = request.POST
    item_name = data.get('name')
    list_id = data.get('list_id')
    list_obj = List.objects.get(id=list_id, user=request.user)
    if not item_name:
        return JsonResponse({"error": "Item name is required."}, status=400)
    new_item = Item.objects.create(list=list_obj, name=item_name)
    return JsonResponse({"message": "Item added to list" , "item_id": new_item.id})

# # List Detail with Items
@login_required
def list_detail(request, list_id):
    try:
        # Fetch the list from the database
        list_data = get_object_or_404(List, id=int(list_id))  # Use list_id, not 1

        item_data = Item.objects.filter(list_id=list_data, completed=False)
        completed_items = Item.objects.filter(list_id=list_data, completed=True)

        itemForm = ItemForm()
        return render(request, 'list/list_detail.html', {'list_name': list_data, 'listItems': item_data, 'completed_items': completed_items,
                                                         'itemForm': itemForm})

        # Render the template with the list data
    except Exception:
        return JsonResponse({'error': 'List not found'}, status=404)

# Mark Item as Completed
@login_required
def mark_item_complete(request, item_id):
    item_id = item_id
    if not item_id:
        return JsonResponse({'error': 'Item Not Found'}, status=404)
    item = get_object_or_404(Item, id=item_id, list__user=request.user)
    item.completed = True
    item.save()
    return JsonResponse({'message': 'Item Marked as Completed'}, status=202)

# Delete List
@login_required
def delete_list(request, list_id):
    if not list_id:
        return JsonResponse({'error': 'List Not Found'}, status=404)
    list_obj = get_object_or_404(List, id=list_id, user=request.user)
    list_obj.delete()
    return JsonResponse({'message': 'Item Deleted'}, status=202)

#sorting

