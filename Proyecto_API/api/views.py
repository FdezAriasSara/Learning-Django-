from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.views import View
from .models import Company
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
    def get(self, request):
        companies=list(Company.objects.values())
        #Es necesario convertirlo a list, para que sea un objeto conocido por python y por tanto , serializable a json
        if len(companies)>0:
           datos={'message':"Success", 'companies':companies}
        else:
           datos={'message':"Companies not found..."}
        return JsonResponse(datos)
        
    def post(self, request):
        print(request.body)
        datos={'message':"Success"}
        return JsonResponse(datos)
        
    def put(self,request):
        pass
    def delet(self,request):
        pass