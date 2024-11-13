# myapp/tasks.py
import csv
from io import StringIO
from celery import shared_task
from django.contrib.auth import get_user_model
from .models import List

User = get_user_model()

@shared_task
def process_csv_task(file_data, user_id):
    user = User.objects.get(id=user_id)
    csv_file_data = StringIO(file_data)
    reader = csv.reader(csv_file_data)

    for row in reader:
        title = row[0]  # Assuming the title is in the first column
        List.objects.create(name=title, user=user)
