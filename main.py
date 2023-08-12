# import cv2
# import numpy as np
# import pyautogui
# from pywinauto import Desktop, Application
# import time

# time.sleep(5)

# # Cargar la imagen que deseas buscar
# imagen = cv2.imread('imagenes/logo.jpg')

# # Definir una bandera que indique si la imagen ha sido encontrada
# imagen_encontrada = False

# # Seleccionar el escritorio 2
# desktop = Desktop("Desktop 2")
# desktop.set_focus()

# # Ejecutar el programa en el escritorio 2
# while not imagen_encontrada:
#     # Capturar una captura de pantalla
#     pantalla = pyautogui.screenshot()

#     # Convertir la captura de pantalla a una imagen de OpenCV
#     imagen_pantalla = cv2.cvtColor(np.array(pantalla), cv2.COLOR_RGB2BGR)

#     # Buscar la imagen en la pantalla
#     resultado = cv2.matchTemplate(imagen_pantalla, imagen, cv2.TM_CCOEFF_NORMED)

#     # Encontrar las coordenadas de la imagen en la pantalla
#     _, max_val, _, max_loc = cv2.minMaxLoc(resultado)

#     # Si la imagen se encuentra en la pantalla, hacer clic en ella y establecer la bandera en True
#     if max_val > 0.9:
#         pyautogui.click(max_loc)
#         imagen_encontrada = True

# # Salir del bucle y detener el programa
# print("Imagen encontrada, programa detenido.")

from pywinauto import Desktop

desktops = Desktop().desktops()
for i, desktop in enumerate(desktops):
    print(f"Desktop {i + 1}: {desktop.name}")