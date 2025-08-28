import cv2

# Lee la imagen (asegúrate de que el archivo exista en esa ruta)
img = cv2.imread("0c235241ecd73e4f94631b9a9d9d1b46.jpg")

# Muestra la imagen en una ventana
cv2.imshow("Ventana", img)

# Espera hasta que presiones una tecla
cv2.waitKey(0)

# Cierra todas las ventanas abiertas de OpenCV
cv2.destroyAllWindows()
