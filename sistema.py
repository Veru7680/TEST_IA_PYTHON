def carrera_orientacion():
    # Preguntas y sus respectivas carreras
    preguntas = [
        ("¿Te interesa resolver problemas complejos con programación y sistemas?", ['Informática']),
        ("¿Te gustaría trabajar en el diseño de software y aplicaciones?", ['Informática']),
        ("¿Te interesa desarrollar algoritmos y estructuras de datos?", ['Informática']),
        ("¿Disfrutas trabajar con equipos de computadoras y redes?", ['Informática']),
        ("¿Te gustaría crear proyectos tecnológicos innovadores?", ['Informática']),
        ("¿Te atrae la idea de trabajar en la agricultura, cuidando el entorno natural?", ['Agronómica']),
        ("¿Te gustaría trabajar en la optimización de cultivos y la producción agrícola?", ['Agronómica']),
        ("¿Te interesa el estudio de suelos, plagas y la mejora de la productividad agrícola?", ['Agronómica']),
        ("¿Te gustaría trabajar con animales y la producción ganadera?", ['Agronómica']),
        ("¿Te atrae la idea de trabajar en proyectos de desarrollo rural?", ['Agronómica']),
        ("¿Te gustaría resolver problemas relacionados con la gestión de recursos naturales?", ['Ambiental']),
        ("¿Te interesa el estudio de la contaminación y la sostenibilidad?", ['Ambiental']),
        ("¿Te gustaría trabajar en proyectos de conservación del medio ambiente?", ['Ambiental']),
        ("¿Te interesa desarrollar políticas públicas para el cuidado del agua y la biodiversidad?", ['Ambiental']),
        ("¿Te gustaría trabajar con energía renovable y energías limpias?", ['Ambiental']),
        ("¿Te atrae el diseño de infraestructuras relacionadas con el manejo del agua?", ['Hídricos']),
        ("¿Te gustaría gestionar proyectos relacionados con la distribución y almacenamiento de agua?", ['Hídricos']),
        ("¿Te interesa el estudio de la hidráulica y la ingeniería de recursos hídricos?", ['Hídricos']),
        ("¿Te gustaría trabajar en la construcción de presas, canales o plantas de tratamiento de agua?", ['Hídricos']),
        ("¿Te interesa trabajar en la gestión de aguas subterráneas y fuentes de agua?", ['Hídricos']),
        ("¿Te interesa la programación de sistemas para automatizar procesos?", ['Informática']),
        ("¿Te gustaría desarrollar aplicaciones móviles para mejorar la vida de las personas?", ['Informática']),
        ("¿Disfrutas aprender sobre redes de comunicación y ciberseguridad?", ['Informática']),
        ("¿Te gustaría trabajar en la creación de sistemas de información geográfica (SIG)?", ['Agronómica']),
        ("¿Te interesa la biotecnología aplicada al campo agrícola?", ['Agronómica']),
        ("¿Te gustaría desarrollar soluciones para el manejo de residuos sólidos?", ['Ambiental']),
        ("¿Te interesa la ingeniería de paisajes y la restauración ecológica?", ['Ambiental']),
        ("¿Te gustaría trabajar en el monitoreo y control de la calidad del agua?", ['Hídricos']),
        ("¿Te atrae el análisis de flujos hídricos y la modelización de cuencas hidrográficas?", ['Hídricos']),
        ("¿Te gustaría colaborar en proyectos de recuperación de ecosistemas acuáticos?", ['Hídricos']),
    ]

    # Inicialización de puntajes para cada carrera
    puntajes = {
        'Informática': 0,
        'Agronómica': 0,
        'Ambiental': 0,
        'Hídricos': 0
    }

    # Recorrer cada pregunta
    for pregunta, carreras in preguntas:
        respuesta = input(f"{pregunta} (S/N): ").strip().upper()
        
        # Validar respuesta
        if respuesta == 'S':
            for carrera in carreras:
                puntajes[carrera] += 1

    # Mostrar resultados
    print("\nResultados finales:")
    for carrera, puntaje in puntajes.items():
        print(f"{carrera}: {puntaje} puntos")

    # Determinar las dos carreras con mayor puntaje
    carreras_ordenadas = sorted(puntajes.items(), key=lambda x: x[1], reverse=True)
    print("\nLas dos carreras con mayor puntuación son:")
    print(f"1. {carreras_ordenadas[0][0]} con {carreras_ordenadas[0][1]} puntos")
    print(f"2. {carreras_ordenadas[1][0]} con {carreras_ordenadas[1][1]} puntos")

# Ejecutar la función
carrera_orientacion()
