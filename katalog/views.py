from django.shortcuts import render
from katalog.models import CatalogItem

def show_catalog(req):
    catalog_data = CatalogItem.objects.all()    
    context = {
        "nama": "Bonaventura Galang Kristabel Angipanglipur Hatmasasmita",
        "npm": "2106630025",
        "catalog_data": catalog_data
    }
    return render(req, "katalog/index.html", context)