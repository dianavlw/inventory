from ast import excepthandler
import json
from django.shortcuts import render
from inventory_api.serializers import ProductSerializer, WarehouseSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from inventory_api.models import Product, Warehouse
from inventory_api.forms import ProductForm, WarehouseForm


#product
def product_list(request):
    return object_list(request, Product, ProductSerializer)
    

def product_detail(request, product_id):
    return object_detail(request, Product, ProductSerializer, product_id)

@csrf_exempt    
def product_new(request):
    return process_object_form(request, ProductForm, ProductSerializer)


@csrf_exempt 
def product_update(request, product_id):
    return process_object_form(request, Product, ProductForm, ProductSerializer, product_id)


@csrf_exempt 
def product_delete(request, product_id):
    return object_delete(request, Product, product_id)



## warehouse

def warehouse_list(request):
    return object_list(request, Warehouse, WarehouseSerializer)

def warehouse_detail(request, warehouse_id):
    return object_detail(request, Warehouse, WarehouseSerializer, warehouse_id)

@csrf_exempt
def warehouse_new(request):
    return process_object_form(request, Warehouse, WarehouseForm, WarehouseSerializer)

@csrf_exempt
def warehouse_update(request, warehouse_id):
    return process_object_form(request, Warehouse, WarehouseForm, WarehouseSerializer, warehouse_id)

@csrf_exempt
def warehouse_delete(request, warehouse_id):
    return object_delete(request, Warehouse, warehouse_id)



# being able to remove products from warehouses, generic methods
def object_list(request, model, model_serializer):
    object = model.objects.all()
    serialized_object= model_serializer().get_all(object)
    return JsonResponse(data=serialized_object, status= 200)
    return render(request, 'base.html', {'object':object})


def object_detail(request, model, model_serializer,  object_id):
    try:
        object = model.objects.get(pk=object_id)
        serialized_object = model_serializer().get(object)
        return JsonResponse(data=serialized_object, status=200)
    except:
        return JsonResponse(data={"status:": "Item not found!"}, status=404)


def object_detail(request, model, model_serializer, object_id):
    try:
        object = model.objects.get(pk=object_id)
        serialized_object = model_serializer().get(object)
        return JsonResponse(data=serialized_object, status=200)
    except:
        return JsonResponse(data={"status:": "Item not found!"}, status=404)


def process_object_form(request, model, model_form, model_serializer, object_id=None):
    if request.method == "POST":
        try:
            data = json.load(request)
            object = None
            if object_id:
                object = model.objects.get(pk=object_id)
            form = model_form(data, instance=object)
            if form.is_valid():
                object = form.save()
                serialized_object = model_serializer().get(object)
                return JsonResponse(data=serialized_object, status=200)
            else:
                return JsonResponse(data={"status:": "Invalid fields!"}, status=404)
        except:
            return JsonResponse(data={"status:": "Bad request!"}, status=404)


def object_delete(request, model, object_id):  
    if request.method == "POST":
        try:
            object = model.objects.get(pk=object_id)
            object.delete()
            return JsonResponse(data={"status:": "Item been deleted!"}, status=200)
        except:
            return JsonResponse(data={"status:": "Item doesn't exist!"}, status=404)

