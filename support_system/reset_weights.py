# reset_weights.py

import os
import django
from django.conf import settings
from yourapp.models import Worker

def reset_daily_weights():
    try:
        # Configurar el entorno de Django
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
        django.setup()

        # Reiniciar todos los pesos acumulados a 0
        workers = Worker.objects.all()
        for worker in workers:
            worker.work_weight_accumulated = 0
            worker.save()

        print('Weights reset successfully')
    except Exception as e:
        print(f'ERROR: {str(e)}')

if __name__ == '__main__':
    reset_daily_weights()
