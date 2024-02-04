from django.urls import path
from . import views
urlpatterns = [
  path('users/',views.index,name='index'),
  path('users/create',views.create,name='create'),
  path('users/<int:id>/update',views.update,name='update'),
  path('users/<int:id>',views.get,name='get'),
  path('users/<int:id>/delete',views.delete,name='delete'),
]