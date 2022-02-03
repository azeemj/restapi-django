from django.conf.urls import url
from django.urls import include, path
from . import views

urlpatterns = [
    url('inventory-list', views.inventory),
    path('details/<int:para>', views.detail)

]
