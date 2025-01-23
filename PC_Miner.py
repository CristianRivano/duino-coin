from concurrent.futures import ThreadPoolExecutor
import numpy as np
import multiprocessing
import psutil
import threading
import time

# Detectar núcleos del CPU para configurar los hilos
threads = multiprocessing.cpu_count()

# Función para minería optimizada
def optimized_mine(job):
    """
    Simula minería optimizada usando NumPy.
    job: [job_id, dificultad, hashObjetivo]
    """
    result = np.power(int(job[0]) + int(job[1]), 2) + int(job[2])  # Operación matemática de ejemplo
    return result

# Límite dinámico de uso de CPU
def limit_cpu_usage():
    """
    Reduce el uso del CPU pausando brevemente si supera el 50%.
    """
    while True:
        if psutil.cpu_percent(interval=0.1) > 50:  # Intervalo para monitorear el uso
            time.sleep(0.1)

# Iniciar el limitador de CPU en un hilo separado
threading.Thread(target=limit_cpu_usage, daemon=True).start()

# Lista de trabajos de ejemplo
jobs = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15]
]

# Crear pool de hilos para procesar los trabajos
with ThreadPoolExecutor(max_workers=threads) as executor:
    print(f"Procesando trabajos con {threads} hilos...\n")
    
    # Enviar los trabajos al pool
    future_results = [executor.submit(optimized_mine, job) for job in jobs]
    
    # Imprimir resultados a medida que se completan
    for future in future_results:
        print(f"Resultado del trabajo: {future.result()}")