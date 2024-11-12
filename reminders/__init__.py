# __init__.py in your_project_name
from celery import app as celery_app  # Make sure it points to "celery.py"
__all__ = ('celery_app',)

