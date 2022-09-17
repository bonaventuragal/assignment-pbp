from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_watchlist_html(req):
    watchlist = MyWatchList.objects.all()
    context = {
        "nama": "Bonaventura Galang Kristabel Angipanglipur Hatmasasmita",
        "npm": "2106630025",
        "watchlist": watchlist
    }
    return render(req, "watchlist.html", context)

def show_watchlist_xml(req):
    watchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", watchlist), content_type="application/xml")

def show_watchlist_json(req):
    watchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", watchlist), content_type="application/json")