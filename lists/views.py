from pyexpat.errors import messages
from venv import logger

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ListSerializer

from reminders.views import send_task_reminder
from .forms import ListForm, ItemForm
from .models import List, Item
import csv

from .tasks import process_csv_task


# Create your views here.
@login_required
def list_view(request):
    try:
        lists = List.objects.filter(user=request.user)
        form = ListForm()
        return render(request, 'list/view_list.html',
                      {'lists': lists, 'form': form})
    except Exception as e:
        return JsonResponse({"error": "Unable to retrieve lists at this time. Please try again later."}, status=500)


# Api to get lists
# @api_view(['GET'])
def get_list(request):
    try:
        send_task_reminder.delay()
        return render(request, 'auth/login.html')

    except Exception as e:
        logger.error(e)
        return JsonResponse({"error": "Error Occurred"}, status=400)


# Create List
@login_required
def add_list(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        if not name:
            return JsonResponse({"error": "List name is required."}, status=400)
        try:
            new_list = List.objects.create(name=name, user=request.user)
            return JsonResponse({"message": "List created successfully.", "list_id": new_list.id})
        except Exception:
            return JsonResponse({'error': 'Unable to add lists at this time. Please try again later.'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)


@login_required
def add_item(request):
    data = request.POST
    item_id = data.get('item_id')
    if (item_id):
        item = get_object_or_404(Item, id=item_id)
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            try:
                form.save()
            except Exception as e:
                return JsonResponse({'error': 'Unable to update item at this time. Please try again later.'},
                                    status=404)
        return JsonResponse({"message": "Item Saved", "item_id": item_id})
    else:
        item_name = data.get('name')
        list_id = data.get('list_id')
        color = data.get('color')
        if not item_name:
            return JsonResponse({"error": "Item name is required."}, status=400)
        try:
            list_obj = List.objects.get(id=list_id, user=request.user)
            new_item = Item.objects.create(list=list_obj, name=item_name, color=color)
        except Exception as e:
            return JsonResponse({'error': 'Unable to add item at this time. Please try again later.'}, status=404)
        return JsonResponse({"message": "Item added to list", "item_id": new_item.id})


# List Detail with Items
@login_required
def list_detail(request, list_id, sort_order):
    try:
        # Fetch the list from the database
        list_data = get_object_or_404(List, id=int(list_id))
        item_data = Item.objects.filter(list_id=list_data, completed=False).order_by(sort_order)
        completed_items = Item.objects.filter(list_id=list_data, completed=True).order_by(sort_order)
        itemForm = ItemForm()
        return render(request, 'list/list_detail.html',
                      {'list_name': list_data, 'listItems': item_data, 'completed_items': completed_items,
                       'itemForm': itemForm})
    except Exception:
        return JsonResponse({'error': 'Unable to get list details at the moment. Please try again later.'}, status=404)


# Mark Item as Completed
@login_required
def mark_item_complete(request, item_id):
    if request.method == 'PUT':
        if not item_id:
            return JsonResponse({'error': 'Item Not Found'}, status=404)
        try:
            item = get_object_or_404(Item, id=item_id, list__user=request.user)
            item.completed = True
            item.save()
            return JsonResponse({'message': 'Item Marked as Completed'}, status=202)
        except Exception as e:
            return JsonResponse({'error': 'Unable to mark as complete, Try again later'}, status=404)
    return JsonResponse({"error": "Invalid request method."}, status=400)


# Delete List
@login_required
def delete_list(request, list_id):
    if request.method == 'DELETE':
        if not list_id:
            return JsonResponse({'error': 'List Not Found'}, status=404)
        try:
            list_obj = get_object_or_404(List, id=list_id, user=request.user)
            list_obj.delete()
            return JsonResponse({'message': 'List Deleted'}, status=202)
        except Exception as e:
            return JsonResponse({'error': 'Unable to delete list, Try again later'}, status=404)
    return JsonResponse({"error": "Invalid request method."}, status=400)


@login_required
def delete_item(request, item_id):
    if request.method == 'DELETE':
        if not item_id:
            return JsonResponse({'error': 'Item Not Found'}, status=404)
        try:
            item = get_object_or_404(Item, id=item_id)
            item.delete()
            return JsonResponse({"message": "Item deleted successfully."})
        except Exception as e:
            return JsonResponse({'error': 'Unable to delete item, Try again later'}, status=404)
    return JsonResponse({"error": "Invalid request method."}, status=400)

# Api to get lists
@api_view(['GET'])
def get_list(request):
    try:
        print('lists')
        app = List.objects.all()
        # Serialize the lists with their related items
        serializer = ListSerializer(app, many=True)
        return Response(serializer.data)
    except Exception as e:
        print(f"Error: {e}")
        return Response("Unable to retrieve lists at this time. Please try again later.")

@api_view(['POST'])
def postData(request):
    return Response(" test post request ")

def upload_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES['file']

        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'This is not a CSV file')
            return redirect('list_view')

        # Read file content and trigger Celery task
        file_data = csv_file.read().decode('utf-8')
        process_csv_task.delay(file_data, request.user.id)

        # Decode and read CSV file
        csv_file_data = csv_file.read().decode('utf-8').splitlines()
        reader = csv.reader(csv_file_data)

        # # Import each row into the List model
        # for row in reader:
        #     title = row[0]  # Assuming the title is in the first column
        #     List.objects.create(name=title, user= request.user)

        return redirect('list_view')
        # form = CSVUploadForm()

    # return render(request, 'upload_csv.html', {'form': form})
