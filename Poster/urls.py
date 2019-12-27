from django.urls import path

from . import views

app_name = 'poster'
urlpatterns = [
    path('<int:pk>/' ,views.Index.as_view() ,name="detail"),
    path('add_poster/' ,views.AddPost.as_view() ,name="add-poster"),    
]