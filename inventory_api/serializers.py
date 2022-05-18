from builtins import object

class ProductSerializer(object):
    def get_all(self, products):
        serialized_products = {"products": []}
        for products in products:
            serialized_products["products"].append(self.get(products))
        return serialized_products


    def get(self, product):
        serialize_product = {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "quantity": product.quantity,
            "warehouses": []
        }
        warehouse_serializer = WarehouseSerializer()
        for warehouse in product.warehouse.all():
            serialize_product["warehouses"].append(warehouse_serializer.get(warehouse, False))
        return serialize_product
        
class WarehouseSerializer(object):
    def get_all(self, warehouses):
        serialized_warehouses = {"warehouses": []}
        for warehouse in warehouses:
            serialized_warehouses["warehouses"].append(self.get(warehouse))
        return serialized_warehouses

    def get(self, warehouse, handle_products= True):
        serialized_warehouse = {
            "id": warehouse.id, 
            "name": warehouse.name,
            "location": warehouse.location,
            "phone": warehouse.phone,
        }
        if handle_products:
            serialized_warehouse = {"products": []}
            product_serializer = ProductSerializer()
            for product in warehouse.products.all():
                serialized_warehouse["products"].append(product_serializer.get(product))
        return serialized_warehouse
