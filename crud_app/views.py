from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

# List all items
def item_list(request):
    items = Item.objects.all()
    return render(request, 'crud_app/item_list.html', {'items': items})

# Create a new item
def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'crud_app/item_form.html', {'form': form})

# Update an item
def item_update(request, id):
    item = get_object_or_404(Item, id=id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'crud_app/item_form.html', {'form': form})

# Delete an item
def item_delete(request, id):
    item = get_object_or_404(Item, id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'crud_app/item_confirm_delete.html', {'item': item})