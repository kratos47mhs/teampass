from django.shortcuts import render, redirect
from django import forms
from .forms import FolderForm
from django import View
from .models import Folder

def home(request):
    return render(request, "home.html")

def folder_list(request):
    folders = Folder.objects.all()
    return render(request, "folder_list.html", {"folders": folders})

def folder_new(request):
    if request.method == "POST":
        form = FolderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("folder_list")
    else:
        form = FolderForm()
    return render(request, "folder_new.html", {"form": form})

def folder_detail(request, pk):
    folder = Folder.objects.get(pk=pk)
    return render(request, "folder_detail.html", {"folder": folder})

def item_list(request):
    # TO DO: implement item list view
    pass

class FolderCreateView(forms.ModelFormMixin, View):
    form_class = forms.ModelForm
    template_name = "folder_new.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs

    def form_valid(self, form):
        folder = form.save(commit=False)
        # TO DO: add any necessary validation or processing
        folder.save()
        return redirect("folder_list")

class FolderUpdateView(forms.ModelFormMixin, View):
    model_form_class = forms.ModelForm
    template_name = "folder_update.html"

    def get_object(self, queryset=None):
        pk_var = self.kwargs["pk"]
        slug_var = self.kwargs["slug"]
        # TO DO: implement object retrieval logic
        pass

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

class UserRegisterView(View):
    template_name = "register.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        # TO DO: implement registration logic
        pass