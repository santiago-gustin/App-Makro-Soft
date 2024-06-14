from django.shortcuts import render
from django.views.generic import View #Vista generica
from django.db.models import Min
from .models import Support, Worker
import random
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def form(request):

    if request.method == 'GET':
        return render(request, 'form.html')
    elif request.method == 'POST':
        print(f"Name: {request.POST['name']}, Description: {request.POST['description']}, Priority: {request.POST['priority']}, Weight: {request.POST['weight']}")  # Imprime los datos del formulario en la consola
        try:
            support = Support(name=request.POST['name'], description=request.POST['description'],
                priority=int(request.POST['priority']), work_weight=int(request.POST['weight']))
            support.save()

            # Lógica de asignación: encontrar el trabajador con el menor peso acumulado
            workers = Worker.objects.all()
            min_weight = max(worker.work_weight_accumulated for worker in workers)
            eligible_workers = [worker for worker in workers if worker.work_weight_accumulated == min_weight]
            assigned_worker = random.choice(eligible_workers)

            # Asignar el soporte al trabajador seleccionado y actualizar su peso acumulado
            support.assigned_to = assigned_worker
            assigned_worker.work_weight_accumulated += support.work_weight
            assigned_worker.save()
            support.save()

            return render(request, 'info_asignacion.html', {'assigned_worker': assigned_worker, 'support': support})
        except ValueError:
            return HttpResponse('ERROR: Invalid data type')
        except KeyError:
            return HttpResponse('ERROR: Missing required fields')
        except Exception as e:
            return HttpResponse(f'ERROR: {str(e)}')

def acumulado(request):
    workers = Worker.objects.all()
    return render(request, 'acumulado.html', {'workers': workers})

def reset_daily_weights(request):
    try:
        # Reiniciar todos los pesos acumulados a 0
        workers = Worker.objects.all()
        for worker in workers:
            worker.work_weight_accumulated = 0
            worker.save()
        
        return HttpResponse('Weights reset successfully')
    except Exception as e:
        return HttpResponse(f'ERROR: {str(e)}')
