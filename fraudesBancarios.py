# 1. NUESTROS DATOS (Conceptos de transferencias recientes)
transferencias = [
    "Pago de la colegiatura del mes de mayo",
    "Compra de sustancias sospechosas y armas ilegales",
    "Transferencia a mi hermano por la cena de ayer",
    "Inversión en negocios prohibidos por la ley"
]

# 2. NUESTRO MODELO (Palabras de alerta del sistema financiero)
alertas_fraude = ["armas", "ilegal", "prohibidos", "sustancias", "clonación"]

def modelo_ia_banco(concepto):
    concepto_minuscula = concepto.lower()
    
    # El modelo analiza si la transacción es segura o de riesgo
    for palabra in list(alertas_fraude):
        if palabra in concepto_minuscula:
            return "ALERTA (Posible Fraude / Cuenta Congelada)" # Predicción 1
            
    return "CONTACTADO (Transacción Exitosa)" # Predicción 2

# 3. EVALUACIÓN Y PREDICCIÓN
print("--- DETECTOR DE FRAUDES BANCARIOS ---")
for i, concepto in enumerate(transferencias, 1):
    prediccion = modelo_ia_banco(concepto)
    print(f"Transacción {i}: '{concepto}' -> RESULTADO: {prediccion}")
