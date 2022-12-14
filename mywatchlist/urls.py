from django.urls import path
from mywatchlist.views import show_watchlist_html, show_watchlist_xml, show_watchlist_json, wathclist_links

app_name = 'mywatchlist'

urlpatterns = [
    path('', wathclist_links, name='watchlist'),
    path('html/', show_watchlist_html, name='watchlist_html'),
    path('xml/', show_watchlist_xml, name='watchlist_xml'),
    path('json/', show_watchlist_json, name='watchlist_json'),
]