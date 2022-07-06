from django.urls import path 
from .views import CompanyView
urlpatterns=[path('companies/',CompanyView.as_view(),name='companies_list'),
             path('companies/<int:id>',CompanyView.as_view(),name='companies_process') 
             #El path con el parámetro sirve para varias cosas (insertar una compañia , leer una compañía , actualizar... ) por eso tiene un endpoint más genérico.
             #Su funcionalidad depende del método que se use en la petición.
             ]
