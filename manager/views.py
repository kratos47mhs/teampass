from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from manager.models.models import Item, Folder, CustomUser
from .forms import ItemForm, FolderForm, CustomUserCreationForm


# Home view
def home(request):
    return render(request, "home.html")


# Item views
@login_required
def item_list(request):
    items = Item.objects.filter(user=request.user)
    folders = Folder.objects.filter(user=request.user)
    return render(request, "item_list.html", {"items": items})


@login_required
def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk, user=request.user)
    return render(request, "item_detail.html", {"item": item})


@login_required
def item_create(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect("item_detail", pk=item.pk)
    else:
        form = ItemForm()
    return render(request, "item_form.html", {"form": form})


@login_required
def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk, user=request.user)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("item_detail", pk=item.pk)
    else:
        form = ItemForm(instance=item)
    return render(request, "item_form.html", {"form": form})


@login_required
def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk, user=request.user)
    if request.method == "POST":
        item.delete()
        return redirect("item_list")
    return render(request, "item_confirm_delete.html", {"item": item})


# Folder views
@login_required
def folder_list(request):
    folders = Folder.objects.filter(user=request.user)
    return render(request, "folder_list.html", {"folders": folders})


@login_required
def folder_detail(request, pk):
    folder = get_object_or_404(Folder, pk=pk, user=request.user)
    return render(request, "folder_detail.html", {"folder": folder})


@login_required
def folder_create(request):
    if request.method == "POST":
        form = FolderForm(request.POST)
        if form.is_valid():
            folder = form.save(commit=False)
            folder.user = request.user
            folder.save()
            return redirect("folder_detail", pk=folder.pk)
    else:
        form = FolderForm()
    return render(request, "folder_form.html", {"form": form})


@login_required
def folder_update(request, pk):
    folder = get_object_or_404(Folder, pk=pk, user=request.user)
    if request.method == "POST":
        form = FolderForm(request.POST, instance=folder)
        if form.is_valid():
            form.save()
            return redirect("folder_detail", pk=folder.pk)
    else:
        form = FolderForm(instance=folder)
    return render(request, "folder_form.html", {"form": form})


@login_required
def folder_delete(request, pk):
    folder = get_object_or_404(Folder, pk=pk, user=request.user)
    if request.method == "POST":
        folder.delete()
        return redirect("folder_list")
    return render(request, "folder_confirm_delete.html", {"folder": folder})


# User views
@login_required
def user_list(request):
    users = CustomUser.objects.all()
    return render(request, "user_list.html", {"users": users})


@login_required
def user_detail(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    return render(request, "user_detail.html", {"user": user})


@login_required
def user_create(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("user_detail", pk=user.pk)
    else:
        form = CustomUserCreationForm()
    return render(request, "user_form.html", {"form": form})


@login_required
def user_update(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)  # Retrieve the user or return a 404 error
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_detail', pk=user.pk)
    else:
        form = CustomUserCreationForm(instance=user)
    return render(request, 'user_form.html', {'form': form})


@login_required
def user_delete(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method == "POST":
        user.delete()
        return redirect("user_list")
    return render(request, "user_confirm_delete.html", {"user": user})


# Authentication views
# def user_register(request):
#     if request.method == "POST":
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect("home")
#     else:
#         form = CustomUserCreationForm()
#     return render(request, "register.html", {"form": form})

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('home')  # Redirect to the home page after registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})



def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


@login_required
def user_logout(request):
    logout(request)
    return redirect("home")


@login_required
def user_profile(request):
    user = request.user
    return render(request, "profile.html", {"user": user})
