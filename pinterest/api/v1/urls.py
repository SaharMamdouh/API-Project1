from django.urls import path
from .views import list_movie , create_movie , delete_movie , update_movie

appname='pinterest'
urlpatterns = [
    path('list/',list_movie,name='get-data'),
    path('create/',create_movie, name='post-data'),
    path('delete/<int:id>',delete_movie, name='delete-data'),
    path('update/<int:id>',update_movie, name='put-data'),
]
