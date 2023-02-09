from django.urls import path

from webapp.views.base import index_view, cat_stats

urlpatterns = [
    path("", index_view, name='index'),
    path("cat_stats", cat_stats, name="cat_stats")
]
