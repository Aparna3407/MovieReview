from django.urls import path
from . import views
app_name='movieapp'
urlpatterns = [
    path('/add_movie',views.add_movie, name='add_movie'),
    path('rate/<int:id>/',views.rate,name="rate"),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
]
