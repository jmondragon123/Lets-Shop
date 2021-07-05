from django.shortcuts import render
from django.http import HttpResponse
from .models import ShoppingList, Item

# Create your views here.
# Views are the webpages that we would be able to see
def index(response):
    return render(response,"shoppinglist/index.html",{})

def number(response, id):
    ls = ShoppingList.objects.get(id=id)
    ls_items = ls.item_set.all()
    return render(response,"shoppinglist/shoppinglistview.html",{"name":ls.shoppping_list_name,"slist":ls_items})
    # try:
    #     ls = ShoppingList.objects.get(id=id)
    #     ls_items = ls.item_set.get(id=1)
    # except:
    #     return HttpResponse(f"<h1>No List Found</h1>")
    # else:
    #     return HttpResponse(f"<h1>{id} : {ls.shoppping_list_name} {ls_items.item_name} </h1>")
