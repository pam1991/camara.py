import cv2
import time

# Creamos el objeto de captura de video
cap = cv2.VideoCapture(0)

# Verificar si la cámara se abrió correctamente
if not cap.isOpened():
    print("Error al abrir la cámara")
    exit()

# Obtener la resolución de la cámara
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("Resolución de la cámara:", width, "x", height)

# Definir el número de fotogramas por segundo (FPS)
fps = 30  # Puedes ajustar este valor según sea necesario
print("Número de fotogramas por segundo (FPS):", fps)

# Calcular el tiempo de retardo (delay time) en milisegundos
delay_time = int(1000 / fps)

# Inicializar variables para el conteo de fotogramas y el tiempo inicial
num_frames = 0
start_time = time.time()

# Bucle para capturar y mostrar los fotogramas
while True:
    # Leer un fotograma de la cámara
    ret, frame = cap.read()

    # Verificar si la lectura fue exitosa
    if not ret:
        print("Error al leer el fotograma")
        break

    # Incrementar el contador de fotogramas
    num_frames += 1

    # Calcular el tiempo transcurrido desde el inicio de la captura
    elapsed_time = time.time() - start_time

    # Calcular el número de fotogramas por segundo (FPS)
    if elapsed_time > 0:
        fps = num_frames / elapsed_time
    else:
        fps = 0

    # Mostrar los detalles de los fotogramas
    print("Dimensiones del fotograma:", frame.shape)
    print("Tipo de datos de píxeles:", frame.dtype)
    print("Número de fotogramas por segundo (FPS):", round(fps, 2))
    print("Tiempo transcurrido desde el inicio de la captura:", round(elapsed_time, 2), "segundos")

    # Mostrar el fotograma
    cv2.imshow("Video capture", frame)

    # Esperar un tiempo antes de procesar el siguiente fotograma
    time.sleep(1 / fps)

    # Detectar la entrada del teclado y salir del bucle si se presiona la tecla "Espacio"
    key = cv2.waitKey(delay_time)
    if key == 32:
        break

# Liberar la captura de video
cap.release()

# Cerrar todas las ventanas
cv2.destroyAllWindows()
