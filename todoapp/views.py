from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.http import HttpResponse

# -----------------------------
# HOME PAGE (after login)
# -----------------------------
@login_required
def home(request):
    return render(request, "index.html")


# -----------------------------
# REGISTER
# -----------------------------
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")   # redirect to login page
    else:
        form = RegisterForm()

    context = {"form": form}
    return render(request, "register.html", context)


# -----------------------------
# LOGIN
# -----------------------------
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "login.html", {"error": "Invalid username or password"})

    return render(request, "login.html")


# -----------------------------
# LOGOUT
# -----------------------------
@login_required
def logout_view(request):
    logout(request)
    return redirect("login")


# -----------------------------
# DELETE TASK (placeholder)
# -----------------------------
def delete_task(request, task_id):
    return HttpResponse(f"<h1>delete task: {task_id}</h1>")
