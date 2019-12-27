from django.urls import path

from . import views

app_name = 'poster'
urlpatterns = [
    path('' ,views.ListPoster.as_view() ,name="list-poster"),
    path('<int:pk>/' ,views.Index.as_view() ,name="detail"),
    path('add/' ,views.AddPoster.as_view() ,name="add-poster"),    
    path('edit/<int:pk>' ,views.EditPoster.as_view() ,name="edit-poster"),
    path('request/<int:pk>' ,views.Request ,name='request'),
]