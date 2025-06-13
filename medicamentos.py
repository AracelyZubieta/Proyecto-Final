medicamentos_db = {
    'Amoxicilina suspensión 500 mg/5 ml': {'forma_farmaceutica': 'Suspensión', 'dosis_mg_kg': 50, 'concentracion_mg_ml': 100},
    'Amoxicilina + ácido clavulánico suspensión 250 mg + 62.5 mg/5 ml': {'forma_farmaceutica': 'Suspensión', 'dosis_mg_kg': 50, 'concentracion_mg_ml': 50},
    'Cefixima suspensión 100 mg/5 ml': {'forma_farmaceutica': 'Suspensión', 'dosis_mg_kg': 8, 'concentracion_mg_ml': 20},
    'Cefradina suspensión 250 mg/5 ml': {'forma_farmaceutica': 'Suspensión', 'dosis_mg_kg': 50, 'concentracion_mg_ml': 50},
    'Cotrimoxazol suspensión 200 mg + 40 mg/5 ml': {'forma_farmaceutica': 'Suspensión', 'dosis_mg_kg': 8, 'concentracion_mg_ml': 48},
    'Albendazol suspensión 200 mg/5 ml': {'forma_farmaceutica': 'Suspensión', 'dosis_mg_kg': 10, 'concentracion_mg_ml': 40},
    'Mebendazol suspensión 100 mg/5 ml': {'forma_farmaceutica': 'Suspensión', 'dosis_mg_kg': 5, 'concentracion_mg_ml': 20},
    'Lamivudina jarabe 10 mg/ml': {'forma_farmaceutica': 'Jarabe', 'dosis_mg_kg': 4, 'concentracion_mg_ml': 10},
    'Ácido valproico solución oral 200 mg/5 ml': {'forma_farmaceutica': 'Solución oral', 'dosis_mg_kg': 20, 'concentracion_mg_ml': 40},
    'Ácido valproico solución oral 250 mg/5 ml': {'forma_farmaceutica': 'Solución oral', 'dosis_mg_kg': 20, 'concentracion_mg_ml': 50},
    'Fenobarbital gotas 20 mg/ml': {'forma_farmaceutica': 'Gotas', 'dosis_mg_kg': 5, 'concentracion_mg_ml': 20},
    'Clorfenamina jarabe 2 mg/5 ml': {'forma_farmaceutica': 'Jarabe', 'dosis_mg_kg': 0.1, 'concentracion_mg_ml': 0.4},
    'Cetirizina jarabe 5 mg/5 ml': {'forma_farmaceutica': 'Jarabe', 'dosis_mg_kg': 0.25, 'concentracion_mg_ml': 1},
    'Dextrometorfano jarabe 10 mg/5 ml': {'forma_farmaceutica': 'Jarabe', 'dosis_mg_kg': 1, 'concentracion_mg_ml': 2},
    'Complejo B inyectable (uso pediátrico)': {'forma_farmaceutica': 'Inyectable', 'dosis_mg_kg': 0.5},
    'Complejo de vitaminas y minerales (CMV) en polvo para solución oral': {'forma_farmaceutica': 'Polvo para solución oral', 'dosis_mg_kg': 1},
    'Vitamina D (colecalciferol) cápsula o comprimido blando': {'forma_farmaceutica': 'Cápsula o Comprimido blando', 'dosis_mg_kg': 0.05},
    'Ibuprofeno suspensión 100 mg/5 ml': {'forma_farmaceutica': 'Suspensión', 'dosis_mg_kg': 10, 'concentracion_mg_ml': 20},
    'Paracetamol': {'forma_farmaceutica': 'Comprimido', 'dosis_mg_kg': 15},
    'Lactulosa solución oral 65%': {'forma_farmaceutica': 'Solución oral', 'dosis_mg_kg': 0.5},
    'Metoclopramida comprimido o inyectable': {'forma_farmaceutica': 'Comprimido o Inyectable', 'dosis_mg_kg': 0.1},
    'Diclofenaco inyectable': {'forma_farmaceutica': 'Inyectable', 'dosis_mg_kg': 1.5},
    'Ibuprofeno inyectable': {'forma_farmaceutica': 'Inyectable', 'dosis_mg_kg': 10},
    'Omeprazol cápsulas': {'forma_farmaceutica': 'Cápsulas', 'dosis_mg_kg': 0.5},
    'Furosemida inyectable': {'forma_farmaceutica': 'Inyectable', 'dosis_mg_kg': 1},
}

def calcular_dosis_pediatrica(medicamento, peso):
    medicamento_data = medicamentos_db.get(medicamento)
    if medicamento_data:
        dosis_mg_kg = medicamento_data.get('dosis_mg_kg')
        if dosis_mg_kg is not None:
            dosis_total_mg = dosis_mg_kg * peso
            return dosis_total_mg
    return None