from django.urls import path
from contact import views

app_name = 'contact' # criado namespace para a aplicação contact. sempre que chamar a view index tem que chamar contact:index

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    
    # contact CRUD
    path('contact/<int:contact_id>/detail/', views.contact, name='contact'),
    path('contact/create/', views.create, name='create'),
    
]
