import cv2 as cv  # OpenCV para procesamiento de imágenes
import numpy as np  # NumPy para trabajar con matrices

# Carga la imagen en color (3 canales: B, G, R en OpenCV)
img = cv.imread("C:/Users/emili/Downloads/fondo.jpg", 1)

# Verifica que se haya cargado correctamente
if img is None:
    raise FileNotFoundError("No se encontró la imagen en la ruta especificada")

# Crea una imagen vacía (matriz de ceros) con el mismo alto y ancho que la original
# dtype=np.uint8 porque las imágenes son de 8 bits por canal
img2 = np.zeros(img.shape[:2], dtype=np.uint8)

# Muestra las dimensiones de la imagen (alto, ancho, canales)
print("Dimensiones:", img.shape)

# Separa los 3 canales (OpenCV usa BGR en vez de RGB)
b, g, r = cv.split(img)

# Crea imágenes que muestran solo un canal, poniendo los otros dos en negro
r2 = cv.merge([img2, img2, r])  # Solo rojo
g2 = cv.merge([img2, g, img2])  # Solo verde
b2 = cv.merge([b, img2, img2])  # Solo azul

# Reconstruye la imagen cambiando el orden de los canales (B, R, G en vez de B, G, R)
img3 = cv.merge([b, r, g])

# === Visualización de resultados ===
cv.imshow("Original", img)
cv.imshow("Rojo (r2)", r2)
cv.imshow("Verde (g2)", g2)
cv.imshow("Azul (b2)", b2)
cv.imshow("Canales reordenados (BRG)", img3)

cv.waitKey(0)
cv.destroyAllWindows()
