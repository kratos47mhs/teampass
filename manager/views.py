from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Items
from django.views.generic import ListView,UpdateView, DeleteView
from .forms import ItemForm
from .models import Folder
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.mail import send_mail
from django.core.serializers import serialize

def item_list(request):
    items = Items.objects.all()
    return render(request, 'manager/item_list.html', {'items': items})

class FolderUpdateView(UpdateView):
    model = Folder
    fields = ['name', 'parent']

class ItemListView(PermissionRequiredMixin, ListView):
    permission_required = 'app.view_item'


class ItemListView(ListView):
    model = Items
    queryset = Items.objects.filter(active=True)
class ItemUpdateView(UpdateView):
    model = Items
    fields = ['label', 'login', 'password', 'url', 'description']

class ItemDeleteView(DeleteView):
    model = Items
    success_url = reverse_lazy('item_list')

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'manager/add_item.html', {'form': form})

send_mail('Subject', 'Message', 'from@example.com', ['to@example.com'])

data = serialize('json', Items.objects.all())

queryset = Item.objects.select_related('folder').all()