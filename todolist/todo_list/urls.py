from django.urls import path
from . import views

urlpatterns = [
path('',views.home_view,name='home'),
path('delete/<todolist_id>',views.delete,name='delete'),
path('complete/<todolist_id>',views.complete,name='complete'),
path('incomplete/<todolist_id>',views.incomplete,name='incomplete'),
path('edit/<todolist_id>',views.edit,name='edit'),

]
