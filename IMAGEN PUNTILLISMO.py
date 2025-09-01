import numpy as np
import cv2 as cv
import random


def crear_lienzo(ancho, alto, color_fondo=(220, 230, 240)):
    """
    Crea un lienzo vacío con un color de fondo específico

    Args:
        ancho: Ancho del lienzo en píxeles
        alto: Alto del lienzo en píxeles
        color_fondo: Color de fondo en formato BGR (azul, verde, rojo)

    Returns:
        Imagen numpy array con 3 canales de color
    """
    # Crea una imagen de 3 canales (BGR) llena con el color de fondo
    lienzo = np.full((alto, ancho, 3), color_fondo, dtype=np.uint8)
    return lienzo


def dibujar_punto_puntillismo(imagen, x, y, color, tamaño_min=2, tamaño_max=6):
    """
    Dibuja un punto con estilo puntillista (círculo con tamaño variable)

    Args:
        imagen: La imagen donde dibujar
        x, y: Coordenadas del punto
        color: Color del punto en formato BGR
        tamaño_min, tamaño_max: Rango de tamaños para los puntos
    """
    # Genera un tamaño aleatorio para el punto
    radio = random.randint(tamaño_min, tamaño_max)

    # Dibuja un círculo relleno en las coordenadas especificadas
    cv.circle(imagen, (x, y), radio, color, -1)


def dibujar_cielo(imagen, ancho, alto):
    """
    Dibuja el cielo usando puntos de diferentes tonos azules

    Args:
        imagen: El lienzo donde dibujar
        ancho: Ancho de la imagen
        alto: Alto de la imagen
    """
    print("Dibujando el cielo...")

    # Define la región del cielo (tercio superior de la imagen)
    limite_cielo = alto // 3

    # Paleta de colores para el cielo (diferentes tonos de azul)
    colores_cielo = [
        (255, 200, 100),  # Azul claro
        (240, 180, 80),  # Azul medio
        (220, 160, 60),  # Azul más oscuro
        (200, 140, 40),  # Azul profundo
    ]

    # Dibuja puntos aleatorios en la región del cielo
    for _ in range(3000):  # Número de puntos para el cielo
        x = random.randint(0, ancho - 1)
        y = random.randint(0, limite_cielo)
        color = random.choice(colores_cielo)
        dibujar_punto_puntillismo(imagen, x, y, color, 3, 7)


def dibujar_montañas(imagen, ancho, alto):
    """
    Dibuja montañas en el horizonte usando tonos grises y marrones

    Args:
        imagen: El lienzo donde dibujar
        ancho: Ancho de la imagen
        alto: Alto de la imagen
    """
    print("Dibujando las montañas...")

    # Define la región de las montañas
    inicio_montañas = alto // 3
    fin_montañas = alto // 2

    # Paleta de colores para las montañas
    colores_montañas = [
        (100, 100, 120),  # Gris azulado
        (80, 90, 110),  # Gris oscuro
        (60, 80, 100),  # Gris muy oscuro
        (90, 110, 130),  # Gris claro
    ]

    # Crea una forma de montaña usando una función sinusoidal
    for x in range(0, ancho, 2):  # Cada 2 píxeles para optimizar
        # Calcula la altura de la montaña usando senos para crear picos
        altura_montaña = int(inicio_montañas + 30 * np.sin(x * 0.01) + 20 * np.sin(x * 0.03))

        # Dibuja puntos desde la línea de la montaña hasta el límite inferior
        for y in range(altura_montaña, fin_montañas):
            if random.random() < 0.7:  # 70% de probabilidad de dibujar un punto
                color = random.choice(colores_montañas)
                dibujar_punto_puntillismo(imagen, x, y, color, 2, 5)


def dibujar_campo(imagen, ancho, alto):
    """
    Dibuja un campo verde con diferentes tonalidades

    Args:
        imagen: El lienzo donde dibujar
        ancho: Ancho de la imagen
        alto: Alto de la imagen
    """
    print("Dibujando el campo...")

    # Define la región del campo (mitad inferior)
    inicio_campo = alto // 2

    # Paleta de colores para el campo (diferentes verdes)
    colores_campo = [
        (50, 150, 50),  # Verde medio
        (40, 130, 40),  # Verde más oscuro
        (60, 170, 60),  # Verde claro
        (30, 110, 30),  # Verde muy oscuro
        (70, 180, 70),  # Verde muy claro
    ]

    # Dibuja el campo con puntos aleatorios
    for _ in range(5000):  # Muchos puntos para dar textura al campo
        x = random.randint(0, ancho - 1)
        y = random.randint(inicio_campo, alto - 1)
        color = random.choice(colores_campo)
        dibujar_punto_puntillismo(imagen, x, y, color, 2, 6)


def dibujar_flores(imagen, ancho, alto):
    """
    Añade flores pequeñas dispersas por el campo

    Args:
        imagen: El lienzo donde dibujar
        ancho: Ancho de la imagen
        alto: Alto de la imagen
    """
    print("Añadiendo flores...")

    # Colores para las flores
    colores_flores = [
        (0, 0, 200),  # Rojo
        (0, 150, 255),  # Amarillo
        (200, 100, 150),  # Rosa
        (255, 255, 255),  # Blanco
    ]

    # Dibuja flores aleatorias en el campo
    inicio_campo = alto // 2
    for _ in range(200):  # Número de flores
        x = random.randint(0, ancho - 1)
        y = random.randint(inicio_campo + 50, alto - 20)
        color = random.choice(colores_flores)
        # Las flores son puntos un poco más grandes
        dibujar_punto_puntillismo(imagen, x, y, color, 4, 8)


def dibujar_sol(imagen, x_sol, y_sol):
    """
    Dibuja el sol como un conjunto de puntos amarillos

    Args:
        imagen: El lienzo donde dibujar
        x_sol, y_sol: Coordenadas del centro del sol
    """
    print("Dibujando el sol...")

    # Colores para el sol (amarillos y naranjas)
    colores_sol = [
        (0, 200, 255),  # Amarillo brillante
        (0, 180, 240),  # Amarillo medio
        (0, 150, 255),  # Amarillo intenso
        (0, 160, 200),  # Naranja claro
    ]

    # Dibuja el sol como puntos en forma circular
    radio_sol = 40
    for _ in range(300):  # Número de puntos para el sol
        # Genera coordenadas aleatorias dentro de un círculo
        angulo = random.uniform(0, 2 * np.pi)
        distancia = random.uniform(0, radio_sol)

        x = int(x_sol + distancia * np.cos(angulo))
        y = int(y_sol + distancia * np.sin(angulo))

        color = random.choice(colores_sol)
        dibujar_punto_puntillismo(imagen, x, y, color, 3, 8)


def crear_paisaje_puntillista():
    """
    Función principal que crea el paisaje completo
    """
    print("Iniciando creación del paisaje puntillista...")

    # Dimensiones de la imagen
    ancho, alto = 800, 600

    # Crear el lienzo
    paisaje = crear_lienzo(ancho, alto)

    # Dibujar cada elemento del paisaje en orden
    dibujar_cielo(paisaje, ancho, alto)
    dibujar_sol(paisaje, 650, 100)  # Sol en la esquina superior derecha
    dibujar_montañas(paisaje, ancho, alto)
    dibujar_campo(paisaje, ancho, alto)
    dibujar_flores(paisaje, ancho, alto)

    return paisaje


# ============= PROGRAMA PRINCIPAL =============
if __name__ == "__main__":
    print("=== Generador de Paisaje Puntillista ===")

    # Establecer semilla aleatoria para resultados reproducibles (opcional)
    random.seed(42)
    np.random.seed(42)

    # Crear el paisaje
    imagen_paisaje = crear_paisaje_puntillista()

    print("¡Paisaje completado!")

    # Mostrar la imagen
    cv.imshow('Paisaje Puntillista', imagen_paisaje)

    # Opcionalmente, guardar la imagen
    cv.imwrite('paisaje_puntillista.png', imagen_paisaje)
    print("Imagen guardada como 'paisaje_puntillista.png'")

    # Esperar a que el usuario presione una tecla
    print("Presiona cualquier tecla para cerrar...")
    cv.waitKey(0)
    cv.destroyAllWindows()