from django.http import JsonResponse, HttpResponseBadRequest
from django.views import View
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render 
from .models import Cliente

# Create your views here.
class ClienteView (View):
    @method_decorator(csrf_exempt, name="dispatch")
    def get(self, request):
        Clientes = Cliente.objects.all().values()
        return JsonResponse(list(Clientes), safe=False)
    
    def post(self, request):
        try:
            data = json.load(request.body)
            cliente = cliente.objects.create(
                id = data["id"],
                nombre = data["nombre"],
                fecha_nacimiento = data["fecha de nacimiento"],
            )
            return JsonResponse({"mensaje": "Cliente creado", "id":cliente.nombre})
        except:
            return HttpResponseBadRequest({"error": "Formato invalido"})


    """def get (self, request):
        data = {"respuesta": "Hola mundo"
                }
        return JsonResponse(data)
def post(self, request):
    try:
        body = json.loads(request.body)
    except: 
        return HttpResponseBadRequest("formato invalido")
    
    data = {
        "status": "ok"
    }
    
    return JsonResponse(data) 
    """      

class PaginitaView(View):
    def get (self, request):
        return render(request, "mi app/index.html")
    