from django.urls import path
from contact import views

app_name = 'contact' # criado namespace para a aplicação contact. sempre que chamar a view index tem que chamar contact:index

urlpatterns = [
    path('', views.index, name='index'),
]
