# Add the SKU data provided to the product catalog dictionary
product_catalog = {
    "SKU123": {
        "name": "Widget A",
        "price": 19.99,
        "quantity": 50
    },
    "SKU456": {
        "name": "Gadget B",
        "price": 34.95,
        "quantity": 25
    },
    "SKU789": {
        "name": "Gizmo C",
        "price": 9.99,
        "quantity": 100
    }
}

# Look up this SKU in your code.
sku_to_find = "SKU123"
print("Price of", product_catalog[sku_to_find]["name"], "is $", product_catalog[sku_to_find]["price"])