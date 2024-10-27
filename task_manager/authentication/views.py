from pyexpat.errors import messages

from django.db import IntegrityError
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
import re
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


#Register functionality
@csrf_exempt
def register(request):
    if request.method == 'POST':
        # data = json.loads(request.body)
        data = request.POST
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        # Validate username
        if not username or len(username) < 3:
            return JsonResponse({"error": "Username must be at least 3 characters long."}, status=400)

        # Validate email
        try:
            validate_email(email)
        except ValidationError:
            return JsonResponse({"error": "Invalid email format."}, status=400)

        # Validate password
        if not password or len(password) < 8:
            return JsonResponse({"error": "Password must be at least 8 characters long."}, status=400)

        # Check if the username or email already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'auth/register.html', {'error': "Username already exists. Please choose another."})
        elif User.objects.filter(email=email).exists():
            return render(request, 'auth/register.html', {'error': "Email is already registered. Try logging in."})

        # Create the user
        try:
            User.objects.create_user(username=username, email=email, password=password)
            return render(request, 'auth/register.html', {'success': True})
        except:
            return render(request, 'auth/register.html', {'error': "An error occurred. Please try again."})

    return render(request, 'auth/register.html')

#Login functionality
@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        # data = json.loads(request.body)
        data = request.POST
        username, password = data.get('username'), data.get('password')
        # Validate username and password presence
        if not username:
            return JsonResponse({"error": "Username is required."}, status=400)
        if not password:
            return JsonResponse({"error": "Password is required."}, status=400)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Log the user in
            return redirect('list_view')  # Redirect to the list view
        else:
            return render(request, 'auth/login.html',{'error': 'Invalid username or password.'})
            # return render(request, 'auth/register.html', {'success': True})
            # return JsonResponse({"error": "Invalid credentials."}, status=400)
    return render(request, 'auth/login.html')

#logout functionality
@login_required
def user_logout(request):
    logout(request)
    return JsonResponse({"message": "Logged out successfully."})