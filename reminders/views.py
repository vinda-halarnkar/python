from datetime import datetime
from celery import shared_task


# Create your views here.
@shared_task
def send_task_reminder():
    try:
        print(f"Ran operation at {datetime.now()}")
    except Exception as e:
        print("Task does not exist.")
