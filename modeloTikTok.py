# 1. NUESTROS DATOS (Comentarios en una publicación)
comentarios_nuevos = [
    "¡Qué buen video! Sigue así crack",
    "Eres un tonto, tu contenido es horrible y feo",
    "Me encantó la edición del segundo 15",
    "Qué feo te ves, dedícate a otra cosa, tonto"
]

# 2. NUESTRO MODELO (Palabras prohibidas por la comunidad)
palabras_toxicas = ["tonto", "horrible", "feo", "basura", "odioso"]

def modelo_ia_moderador(comentario):
    comentario_minuscula = comentario.lower()
    
    # El modelo busca si hay lenguaje ofensivo
    for palabra in list(palabras_toxicas):
        if palabra in comentario_minuscula:
            return "BLOQUEADO (Tóxico)" # Predicción 1
            
    return "APROBADO (Seguro)" # Predicción 2

# 3. EVALUACIÓN Y PREDICCIÓN
print("--- MODERADOR DE REDES SOCIALES ---")
for i, comentario in enumerate(comentarios_nuevos, 1):
    prediccion = modelo_ia_moderador(comentario)
    print(f"Comentario {i}: '{comentario}' -> ESTADO: {prediccion}")
