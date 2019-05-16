from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item, List

def home_page(request):
    return render(request, 'home.html')

def view_list(request, list_id):
    items = Item.objects.filter(list=list_id)
    return render(request, 'list.html', {'items': items, 'list_id': list_id})

def new_list(request):
    new_list = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=new_list)
    return redirect(f'/lists/{new_list.id}/')

def add_item(request, list_id):
    existing_list = List.objects.get(pk=list_id)
    Item.objects.create(text=request.POST['item_text'], list=existing_list)
    return redirect(f'/lists/{existing_list.id}/')