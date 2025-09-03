import cv2 as cv
import numpy as np

# Abre la cámara (0 = webcam por defecto)
cap = cv.VideoCapture(0)

if not cap.isOpened():
    raise RuntimeError("No se pudo abrir la cámara. Verifica permisos o índice de cámara.")

# Opcional: fija resolución
# cap.set(cv.CAP_PROP_FRAME_WIDTH,  640)
# cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = cap.read()
    if not ret:
        print("No se pudo leer frame de la cámara.")
        break

    # OpenCV trabaja en BGR
    b, g, r = cv.split(frame)

    # Zeros para anular canales
    zeros = np.zeros_like(b)

    # Versiones "solo canal" en color
    # (dejamos el canal correspondiente y los otros dos en negro)
    blue_only  = cv.merge([b, zeros, zeros])
    green_only = cv.merge([zeros, g, zeros])
    red_only   = cv.merge([zeros, zeros, r])

    # --- Mostrar en ventanas separadas ---
    cv.imshow("Original (BGR)", frame)
    cv.imshow("Canal Azul (B)", blue_only)
    cv.imshow("Canal Verde (G)", green_only)
    cv.imshow("Canal Rojo (R)", red_only)

    # --- Mosaico opcional en una sola ventana (2x2) ---
    # Redimensionamos para que todo quepa igual
    h, w = frame.shape[:2]
    target_w = 320
    target_h = int(h * (target_w / w))

    def rz(img):  # helper de resize
        return cv.resize(img, (target_w, target_h), interpolation=cv.INTER_AREA)

    grid = cv.vconcat([
        cv.hconcat([rz(frame), rz(blue_only)]),
        cv.hconcat([rz(green_only), rz(red_only)])
    ])
    cv.imshow("Mosaico: Original | B ; G | R", grid)

    # ESC para salir
    if (cv.waitKey(1) & 0xFF) == 27:
        break

cap.release()
cv.destroyAllWindows()
