from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.views import View
from .models import Company
import json
# Create your views here.
#vista basada en una clase
class CompanyView(View):
    '''
    El método dispatch, se ejecuta cada vez se realiza una petición. 
    Mediante un decorador , nos saltamos el csrf_exempt( la protección contr csrf) ya que las peticiones 
    que haremos en este ejemplo no serán desde ningún cliente. Serán hechas mediante thunder client para pruebas.
    '''
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    #lista todas las compañías através del ORM(Object Relational Mapping)
    def get(self, request,id=0):
        if(id>0):
            companies=list(Company.objects.filter(id=id).values())
            if len(companies)>0:
                company=companies[0]
                datos={'message': "Success", 'company':company}
        else:
          companies=list(Company.objects.values())
         #Es necesario convertirlo a list, para que sea un objeto conocido por python y por tanto , serializable a json
          if len(companies)>0:
            datos={'message':"Success", 'companies':companies}
          else:
           datos={'message':"Companies not found..."}
        return JsonResponse(datos)
        
    def post(self, request):
        #print(request.body)
        jd=json.loads(request.body)#diccionario en el que se convierten los datos de json enviados
        Company.objects.create(name=jd['name'],website=jd['website'],foundation=jd['foundation'])
        datos={'message':"Success"}
        return JsonResponse(datos)
        
    def put(self,request,id):
        jd=json.loads(request.body)
        companies=list(Company.objects.filter(id=id).values())
        if len(companies) > 0:
            #Aquí tenemos la certeza de que la compañía a actualizar, existe
            company=Company.objects.get(id=id)
            company.name=jd['name']
            company.website=jd['website']
            company.foundation=jd['foundation']
            company.save()
            datos={'message':"Success"}
        else:
            datos={'message':"Company not found..."}
        return JsonResponse(datos)
    def delete(self,request,id):
        #Aquí no trabajamos con datos json
        companies=list(Company.objects.filter(id=id).values())
        if len(companies) > 0:
            #El método delete está integrado en el ORM
            Company.objects.filter(id=id).delete()
            datos={'message':"Success"}
        else:
            datos={'message':"Company not found..."}
        return JsonResponse(datos)