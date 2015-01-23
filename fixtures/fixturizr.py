import json
import os
import random

products_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'products/')

products_txts = os.listdir(products_dir)

brands = dict()
products = list()
product_variants = list()


def get_brand_pk(brand_name):
    if brand_name in brands.keys():
        return brands[brand_name]['pk']

    new_pk = len(brands) + 1
    brands[brand_name] = {
        "fields": {
            "name": brand_name
        },
        "model": "webshop.brand",
        "pk": new_pk
    }
    return new_pk


for txt in products_txts:
    pk = int(txt.replace('.txt', ''))

    with open(os.path.join(products_dir, txt), 'r') as file:
        lines = file.readlines()
        price = int(lines[0].strip())

        products.append({
            "fields": {
                "brand": get_brand_pk(lines[3].strip()),
                "name": lines[1].strip(),
                "description": lines[2].strip()
            },
            "model": "webshop.product",
            "pk": pk
        })

        color = lines[4].strip()
        mi = int(lines[5].strip())
        ma = int(lines[6].strip())

        for size in range(mi, ma + 1):
            product_variants.append({
                "fields": {
                    "product": pk,
                    "color": color,
                    "price": price,
                    "size": float(size),
                    "image": "products/{}.jpg".format(pk),
                    "quantity": random.randint(1, 50)
                },
                "model": "webshop.productvariant",
                "pk": len(product_variants) + 1
            })


l = [b for b in brands.values()] + products + product_variants
print json.dumps(l, indent=2)