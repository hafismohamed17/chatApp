from django.shortcuts import render,redirect
from . import models
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse

def home_page(request):
    return render(request, "index.html")

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm = request.POST.get("confirm_password")

        if password != confirm:
            messages.error(request, "Passwords do not match!")
            return redirect("register")

        # Check if username/email exists
        if models.User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect("register")
        if models.User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect("register")

        hashed_password = make_password(password)
        models.User.objects.create(username=username, email=email, password=hashed_password)
        messages.success(request, "Registration successful! Please log in.")
        return redirect("login")

    # For GET request, render the registration page
    return render(request, "register.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = models.User.objects.get(username=username)
            if check_password(password, user.password):
                # Set session
                request.session["user_id"] = user.id
                request.session["username"] = user.username
                return redirect("home")  # Redirect to chat
            else:
                messages.error(request, "Invalid password")
        except models.User.DoesNotExist:
            messages.error(request, "User not found")

        return redirect("login")

    return render(request, "login.html")

def logout_view(request):
    request.session.flush()
    return redirect("login")


def home(request):
    user_id = request.session.get("user_id")  # get logged-in user from session
    if not user_id:
        return redirect("login")  # redirect if not logged in

    user = models.User.objects.get(id=user_id)

    if request.method == "POST":
        msg = request.POST.get("message")
        if msg:
            models.Message.objects.create(user=user, text=msg)
        return redirect("home")

    messages = models.Message.objects.order_by("-created_at")
    return render(request, "chat.html", {"messages": messages, "user": user})

def get_messages_json(request):
    msgs = models.Message.objects.order_by("-created_at")
    data = []

    for m in msgs:
        data.append({
            "user": m.user.username if m.user else "Unknown",
            "text": m.text,
            "time": m.created_at.strftime("%H:%M %d %b")
        })

    return JsonResponse({"messages": data})
