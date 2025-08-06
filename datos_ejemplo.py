"""
Datos de ejemplo para el Simulador Comunitario
Este archivo contiene datos ficticios para demostrar la funcionalidad de la aplicación
"""

# Datos de ejemplo para sectores
SECTORES_EJEMPLO = [
    {
        "nombre": "Sector Norte",
        "poblacion_total": 1200,
        "num_familias": 300,
        "tipo_territorio": "Urbano",
        "nivel_socioeconomico": "Medio-Bajo",
        "vulnerabilidad": "Alta",
        "servicios": {
            "agua_potable": True,
            "electricidad": True,
            "alcantarillado": True,
            "transporte": True,
            "escuela": True,
            "cesfam": False,
            "organizaciones": True,
            "areas_verdes": False
        },
        "problemas": ["Hacinamiento", "Inseguridad", "Desempleo", "Obesidad"]
    },
    {
        "nombre": "Sector Centro",
        "poblacion_total": 800,
        "num_familias": 200,
        "tipo_territorio": "Urbano",
        "nivel_socioeconomico": "Medio",
        "vulnerabilidad": "Media",
        "servicios": {
            "agua_potable": True,
            "electricidad": True,
            "alcantarillado": True,
            "transporte": True,
            "escuela": True,
            "cesfam": True,
            "organizaciones": True,
            "areas_verdes": True
        },
        "problemas": ["Diabetes", "Hipertensión", "Adultos mayores"]
    },
    {
        "nombre": "Sector Sur",
        "poblacion_total": 1500,
        "num_familias": 375,
        "tipo_territorio": "Rural",
        "nivel_socioeconomico": "Bajo",
        "vulnerabilidad": "Crítica",
        "servicios": {
            "agua_potable": False,
            "electricidad": True,
            "alcantarillado": False,
            "transporte": False,
            "escuela": True,
            "cesfam": False,
            "organizaciones": False,
            "areas_verdes": True
        },
        "problemas": ["Falta de servicios básicos", "Embarazo adolescente", "Violencia intrafamiliar"]
    }
]

# Datos de ejemplo para equipos de cabecera
EQUIPOS_EJEMPLO = [
    {
        "sector": "Sector Norte",
        "composicion": {
            "medicos": 1,
            "enfermeras": 2,
            "tens": 4,
            "matronas": 1,
            "psicologos": 1,
            "otros": 0
        },
        "informacion": {
            "jefe_equipo": "Dra. María González",
            "telefono": "+56 9 1234 5678",
            "horario": "Lunes a Viernes 8:00-17:00",
            "modalidad": "Presencial",
            "experiencia": 8,
            "capacitacion_mais": True
        },
        "microareas": {
            "numero": 4,
            "familias_por_microarea": 75,
            "responsable": "TENS"
        }
    },
    {
        "sector": "Sector Centro",
        "composicion": {
            "medicos": 1,
            "enfermeras": 1,
            "tens": 2,
            "matronas": 1,
            "psicologos": 0,
            "otros": 0
        },
        "informacion": {
            "jefe_equipo": "Enf. Carlos Rodríguez",
            "telefono": "+56 9 2345 6789",
            "horario": "Lunes a Viernes 8:00-18:00",
            "modalidad": "Híbrido",
            "experiencia": 5,
            "capacitacion_mais": True
        },
        "microareas": {
            "numero": 3,
            "familias_por_microarea": 67,
            "responsable": "Enfermera"
        }
    },
    {
        "sector": "Sector Sur",
        "composicion": {
            "medicos": 1,
            "enfermeras": 2,
            "tens": 3,
            "matronas": 1,
            "psicologos": 1,
            "otros": 1
        },
        "informacion": {
            "jefe_equipo": "Dr. Juan Pérez",
            "telefono": "+56 9 3456 7890",
            "horario": "Lunes a Sábado 8:00-17:00",
            "modalidad": "Presencial",
            "experiencia": 12,
            "capacitacion_mais": True
        },
        "microareas": {
            "numero": 5,
            "familias_por_microarea": 75,
            "responsable": "Mixto"
        }
    }
]

# Datos de ejemplo para familias
FAMILIAS_EJEMPLO = [
    {
        "sector": "Sector Norte",
        "apellido": "González",
        "num_integrantes": 5,
        "jefe_hogar": {
            "nombre": "Roberto González",
            "edad": 45,
            "ocupacion": "Empleado"
        },
        "vivienda": {
            "tipo": "Casa",
            "hacinamiento": "Alto",
            "red_apoyo": "Débil",
            "participacion_social": "Baja",
            "acceso_aps": "Difícil"
        },
        "salud": {
            "enfermedades_cronicas": ["Diabetes", "Hipertensión"],
            "embarazo_adolescente": False,
            "violencia_intrafamiliar": True,
            "consumo_drogas": False,
            "desempleo": False,
            "discapacidad": False,
            "adulto_mayor": False
        },
        "riesgos": {
            "social": {"nivel": "Alto", "puntaje": 12},
            "sanitario": {"nivel": "Alto", "puntaje": 9}
        },
        "observaciones": "Familia en situación de vulnerabilidad, requiere intervención prioritaria",
        "fecha_registro": "2024-01-15",
        "responsable": "TENS Ana Martínez"
    },
    {
        "sector": "Sector Norte",
        "apellido": "Silva",
        "num_integrantes": 3,
        "jefe_hogar": {
            "nombre": "Carmen Silva",
            "edad": 38,
            "ocupacion": "Dueña de casa"
        },
        "vivienda": {
            "tipo": "Departamento",
            "hacinamiento": "Medio",
            "red_apoyo": "Regular",
            "participacion_social": "Alta",
            "acceso_aps": "Fácil"
        },
        "salud": {
            "enfermedades_cronicas": ["Obesidad"],
            "embarazo_adolescente": False,
            "violencia_intrafamiliar": False,
            "consumo_drogas": False,
            "desempleo": False,
            "discapacidad": False,
            "adulto_mayor": False
        },
        "riesgos": {
            "social": {"nivel": "Bajo", "puntaje": 4},
            "sanitario": {"nivel": "Medio", "puntaje": 5}
        },
        "observaciones": "Familia estable, requiere educación en hábitos saludables",
        "fecha_registro": "2024-01-15",
        "responsable": "TENS Ana Martínez"
    },
    {
        "sector": "Sector Centro",
        "apellido": "Rodríguez",
        "num_integrantes": 4,
        "jefe_hogar": {
            "nombre": "Luis Rodríguez",
            "edad": 52,
            "ocupacion": "Jubilado"
        },
        "vivienda": {
            "tipo": "Casa",
            "hacinamiento": "Bajo",
            "red_apoyo": "Fuerte",
            "participacion_social": "Alta",
            "acceso_aps": "Fácil"
        },
        "salud": {
            "enfermedades_cronicas": ["Hipertensión", "Artritis"],
            "embarazo_adolescente": False,
            "violencia_intrafamiliar": False,
            "consumo_drogas": False,
            "desempleo": False,
            "discapacidad": False,
            "adulto_mayor": True
        },
        "riesgos": {
            "social": {"nivel": "Bajo", "puntaje": 3},
            "sanitario": {"nivel": "Medio", "puntaje": 6}
        },
        "observaciones": "Adulto mayor con buen apoyo familiar",
        "fecha_registro": "2024-01-16",
        "responsable": "Enf. Carlos Rodríguez"
    },
    {
        "sector": "Sector Sur",
        "apellido": "Mendoza",
        "num_integrantes": 6,
        "jefe_hogar": {
            "nombre": "Patricia Mendoza",
            "edad": 35,
            "ocupacion": "Desempleado"
        },
        "vivienda": {
            "tipo": "Mediagua",
            "hacinamiento": "Alto",
            "red_apoyo": "Débil",
            "participacion_social": "Nula",
            "acceso_aps": "Difícil"
        },
        "salud": {
            "enfermedades_cronicas": [],
            "embarazo_adolescente": True,
            "violencia_intrafamiliar": True,
            "consumo_drogas": True,
            "desempleo": True,
            "discapacidad": False,
            "adulto_mayor": False
        },
        "riesgos": {
            "social": {"nivel": "Alto", "puntaje": 15},
            "sanitario": {"nivel": "Alto", "puntaje": 11}
        },
        "observaciones": "Familia en situación crítica, requiere intervención multisectorial",
        "fecha_registro": "2024-01-17",
        "responsable": "TENS Pedro López"
    },
    {
        "sector": "Sector Norte",
        "apellido": "Herrera",
        "num_integrantes": 4,
        "jefe_hogar": {
            "nombre": "Miguel Herrera",
            "edad": 41,
            "ocupacion": "Empleado"
        },
        "vivienda": {
            "tipo": "Casa",
            "hacinamiento": "Medio",
            "red_apoyo": "Regular",
            "participacion_social": "Media",
            "acceso_aps": "Fácil"
        },
        "salud": {
            "enfermedades_cronicas": ["Diabetes"],
            "embarazo_adolescente": False,
            "violencia_intrafamiliar": False,
            "consumo_drogas": False,
            "desempleo": False,
            "discapacidad": False,
            "adulto_mayor": False
        },
        "riesgos": {
            "social": {"nivel": "Medio", "puntaje": 7},
            "sanitario": {"nivel": "Medio", "puntaje": 6}
        },
        "observaciones": "Familia estable, requiere educación en diabetes",
        "fecha_registro": "2024-01-18",
        "responsable": "TENS Ana Martínez"
    },
    {
        "sector": "Sector Centro",
        "apellido": "Vargas",
        "num_integrantes": 3,
        "jefe_hogar": {
            "nombre": "Elena Vargas",
            "edad": 28,
            "ocupacion": "Empleada"
        },
        "vivienda": {
            "tipo": "Departamento",
            "hacinamiento": "Bajo",
            "red_apoyo": "Fuerte",
            "participacion_social": "Alta",
            "acceso_aps": "Fácil"
        },
        "salud": {
            "enfermedades_cronicas": [],
            "embarazo_adolescente": False,
            "violencia_intrafamiliar": False,
            "consumo_drogas": False,
            "desempleo": False,
            "discapacidad": False,
            "adulto_mayor": False
        },
        "riesgos": {
            "social": {"nivel": "Bajo", "puntaje": 2},
            "sanitario": {"nivel": "Bajo", "puntaje": 3}
        },
        "observaciones": "Familia saludable, sin factores de riesgo",
        "fecha_registro": "2024-01-18",
        "responsable": "Enf. Carlos Rodríguez"
    },
    {
        "sector": "Sector Sur",
        "apellido": "Rojas",
        "num_integrantes": 7,
        "jefe_hogar": {
            "nombre": "Francisco Rojas",
            "edad": 39,
            "ocupacion": "Desempleado"
        },
        "vivienda": {
            "tipo": "Mediagua",
            "hacinamiento": "Alto",
            "red_apoyo": "Débil",
            "participacion_social": "Baja",
            "acceso_aps": "Difícil"
        },
        "salud": {
            "enfermedades_cronicas": ["Hipertensión"],
            "embarazo_adolescente": False,
            "violencia_intrafamiliar": True,
            "consumo_drogas": True,
            "desempleo": True,
            "discapacidad": False,
            "adulto_mayor": False
        },
        "riesgos": {
            "social": {"nivel": "Alto", "puntaje": 14},
            "sanitario": {"nivel": "Alto", "puntaje": 10}
        },
        "observaciones": "Familia con múltiples factores de riesgo, requiere intervención integral",
        "fecha_registro": "2024-01-19",
        "responsable": "TENS Pedro López"
    },
    {
        "sector": "Sector Norte",
        "apellido": "Díaz",
        "num_integrantes": 2,
        "jefe_hogar": {
            "nombre": "Rosa Díaz",
            "edad": 67,
            "ocupacion": "Jubilada"
        },
        "vivienda": {
            "tipo": "Casa",
            "hacinamiento": "Bajo",
            "red_apoyo": "Fuerte",
            "participacion_social": "Alta",
            "acceso_aps": "Fácil"
        },
        "salud": {
            "enfermedades_cronicas": ["Artritis", "Hipertensión"],
            "embarazo_adolescente": False,
            "violencia_intrafamiliar": False,
            "consumo_drogas": False,
            "desempleo": False,
            "discapacidad": False,
            "adulto_mayor": True
        },
        "riesgos": {
            "social": {"nivel": "Bajo", "puntaje": 3},
            "sanitario": {"nivel": "Medio", "puntaje": 7}
        },
        "observaciones": "Adulto mayor con buen apoyo familiar y acceso a servicios",
        "fecha_registro": "2024-01-19",
        "responsable": "TENS Ana Martínez"
    },
    {
        "sector": "Sector Centro",
        "apellido": "Morales",
        "num_integrantes": 5,
        "jefe_hogar": {
            "nombre": "Carlos Morales",
            "edad": 44,
            "ocupacion": "Empleado"
        },
        "vivienda": {
            "tipo": "Casa",
            "hacinamiento": "Medio",
            "red_apoyo": "Regular",
            "participacion_social": "Media",
            "acceso_aps": "Fácil"
        },
        "salud": {
            "enfermedades_cronicas": ["Obesidad", "Diabetes"],
            "embarazo_adolescente": False,
            "violencia_intrafamiliar": False,
            "consumo_drogas": False,
            "desempleo": False,
            "discapacidad": False,
            "adulto_mayor": False
        },
        "riesgos": {
            "social": {"nivel": "Medio", "puntaje": 6},
            "sanitario": {"nivel": "Alto", "puntaje": 8}
        },
        "observaciones": "Familia con problemas de salud crónicos, requiere educación nutricional",
        "fecha_registro": "2024-01-20",
        "responsable": "Enf. Carlos Rodríguez"
    },
    {
        "sector": "Sector Sur",
        "apellido": "Torres",
        "num_integrantes": 4,
        "jefe_hogar": {
            "nombre": "Ana Torres",
            "edad": 31,
            "ocupacion": "Dueña de casa"
        },
        "vivienda": {
            "tipo": "Casa",
            "hacinamiento": "Medio",
            "red_apoyo": "Regular",
            "participacion_social": "Baja",
            "acceso_aps": "Difícil"
        },
        "salud": {
            "enfermedades_cronicas": [],
            "embarazo_adolescente": True,
            "violencia_intrafamiliar": False,
            "consumo_drogas": False,
            "desempleo": False,
            "discapacidad": False,
            "adulto_mayor": False
        },
        "riesgos": {
            "social": {"nivel": "Medio", "puntaje": 8},
            "sanitario": {"nivel": "Medio", "puntaje": 6}
        },
        "observaciones": "Embarazo adolescente, requiere apoyo psicosocial y educación sexual",
        "fecha_registro": "2024-01-20",
        "responsable": "TENS Pedro López"
    },
    {
        "sector": "Sector Norte",
        "apellido": "Castro",
        "num_integrantes": 6,
        "jefe_hogar": {
            "nombre": "Luis Castro",
            "edad": 48,
            "ocupacion": "Empleado"
        },
        "vivienda": {
            "tipo": "Casa",
            "hacinamiento": "Alto",
            "red_apoyo": "Débil",
            "participacion_social": "Baja",
            "acceso_aps": "Fácil"
        },
        "salud": {
            "enfermedades_cronicas": ["Hipertensión"],
            "embarazo_adolescente": False,
            "violencia_intrafamiliar": False,
            "consumo_drogas": False,
            "desempleo": False,
            "discapacidad": False,
            "adulto_mayor": False
        },
        "riesgos": {
            "social": {"nivel": "Medio", "puntaje": 9},
            "sanitario": {"nivel": "Medio", "puntaje": 6}
        },
        "observaciones": "Familia numerosa con hacinamiento, requiere apoyo habitacional",
        "fecha_registro": "2024-01-21",
        "responsable": "TENS Ana Martínez"
    },
    {
        "sector": "Sector Centro",
        "apellido": "Flores",
        "num_integrantes": 3,
        "jefe_hogar": {
            "nombre": "María Flores",
            "edad": 55,
            "ocupacion": "Jubilada"
        },
        "vivienda": {
            "tipo": "Departamento",
            "hacinamiento": "Bajo",
            "red_apoyo": "Fuerte",
            "participacion_social": "Alta",
            "acceso_aps": "Fácil"
        },
        "salud": {
            "enfermedades_cronicas": ["Diabetes", "Artritis"],
            "embarazo_adolescente": False,
            "violencia_intrafamiliar": False,
            "consumo_drogas": False,
            "desempleo": False,
            "discapacidad": False,
            "adulto_mayor": True
        },
        "riesgos": {
            "social": {"nivel": "Bajo", "puntaje": 2},
            "sanitario": {"nivel": "Medio", "puntaje": 7}
        },
        "observaciones": "Adulto mayor con enfermedades crónicas controladas",
        "fecha_registro": "2024-01-21",
        "responsable": "Enf. Carlos Rodríguez"
    },
    {
        "sector": "Sector Sur",
        "apellido": "Pérez",
        "num_integrantes": 6,
        "jefe_hogar": {
            "nombre": "Juan Pérez",
            "edad": 35,
            "ocupacion": "Obrero"
        },
        "vivienda": {
            "tipo": "Mediagua",
            "hacinamiento": "Crítico",
            "red_apoyo": "Débil",
            "participacion_social": "Baja",
            "acceso_aps": "Muy difícil"
        },
        "salud": {
            "enfermedades_cronicas": ["Tuberculosis"],
            "embarazo_adolescente": True,
            "violencia_intrafamiliar": True,
            "consumo_drogas": True,
            "desempleo": True,
            "discapacidad": False,
            "adulto_mayor": False
        },
        "riesgos": {
            "social": {"nivel": "Crítico", "puntaje": 18},
            "sanitario": {"nivel": "Crítico", "puntaje": 15}
        },
        "observaciones": "Familia en extrema vulnerabilidad, requiere intervención urgente y coordinada",
        "fecha_registro": "2024-01-16",
        "responsable": "TENS Carlos Ramírez"
    },
    {
        "sector": "Sector Norte",
        "apellido": "López",
        "num_integrantes": 4,
        "jefe_hogar": {
            "nombre": "Patricia López",
            "edad": 42,
            "ocupacion": "Trabajadora doméstica"
        },
        "vivienda": {
            "tipo": "Departamento",
            "hacinamiento": "Medio",
            "red_apoyo": "Regular",
            "participacion_social": "Media",
            "acceso_aps": "Fácil"
        },
        "salud": {
            "enfermedades_cronicas": ["Asma"],
            "embarazo_adolescente": False,
            "violencia_intrafamiliar": False,
            "consumo_drogas": False,
            "desempleo": False,
            "discapacidad": True,
            "adulto_mayor": False
        },
        "riesgos": {
            "social": {"nivel": "Medio", "puntaje": 7},
            "sanitario": {"nivel": "Medio", "puntaje": 6}
        },
        "observaciones": "Familia con hijo discapacitado, requiere apoyo en rehabilitación",
        "fecha_registro": "2024-01-16",
        "responsable": "TENS Ana Martínez"
    },
    {
        "sector": "Sector Centro",
        "apellido": "Martínez",
        "num_integrantes": 2,
        "jefe_hogar": {
            "nombre": "Elena Martínez",
            "edad": 68,
            "ocupacion": "Jubilada"
        },
        "vivienda": {
            "tipo": "Casa",
            "hacinamiento": "Bajo",
            "red_apoyo": "Fuerte",
            "participacion_social": "Alta",
            "acceso_aps": "Fácil"
        },
        "salud": {
            "enfermedades_cronicas": ["Diabetes", "Hipertensión", "Artritis"],
            "embarazo_adolescente": False,
            "violencia_intrafamiliar": False,
            "consumo_drogas": False,
            "desempleo": False,
            "discapacidad": False,
            "adulto_mayor": True
        },
        "riesgos": {
            "social": {"nivel": "Bajo", "puntaje": 2},
            "sanitario": {"nivel": "Alto", "puntaje": 8}
        },
        "observaciones": "Adulto mayor independiente, buen control de enfermedades crónicas",
        "fecha_registro": "2024-01-16",
        "responsable": "TENS María González"
    },
    {
        "sector": "Sector Sur",
        "apellido": "Soto",
        "num_integrantes": 7,
        "jefe_hogar": {
            "nombre": "Miguel Soto",
            "edad": 28,
            "ocupacion": "Desempleado"
        },
        "vivienda": {
            "tipo": "Casa",
            "hacinamiento": "Alto",
            "red_apoyo": "Débil",
            "participacion_social": "Baja",
            "acceso_aps": "Difícil"
        },
        "salud": {
            "enfermedades_cronicas": [],
            "embarazo_adolescente": True,
            "violencia_intrafamiliar": True,
            "consumo_drogas": True,
            "desempleo": True,
            "discapacidad": False,
            "adulto_mayor": False
        },
        "riesgos": {
            "social": {"nivel": "Alto", "puntaje": 14},
            "sanitario": {"nivel": "Alto", "puntaje": 9}
        },
        "observaciones": "Familia numerosa con múltiples factores de riesgo, requiere intervención integral",
        "fecha_registro": "2024-01-17",
        "responsable": "TENS Carlos Ramírez"
    },
    {
        "sector": "Sector Norte",
        "apellido": "Vega",
        "num_integrantes": 3,
        "jefe_hogar": {
            "nombre": "Ricardo Vega",
            "edad": 39,
            "ocupacion": "Técnico"
        },
        "vivienda": {
            "tipo": "Casa",
            "hacinamiento": "Bajo",
            "red_apoyo": "Fuerte",
            "participacion_social": "Alta",
            "acceso_aps": "Fácil"
        },
        "salud": {
            "enfermedades_cronicas": ["Hipertensión"],
            "embarazo_adolescente": False,
            "violencia_intrafamiliar": False,
            "consumo_drogas": False,
            "desempleo": False,
            "discapacidad": False,
            "adulto_mayor": False
        },
        "riesgos": {
            "social": {"nivel": "Bajo", "puntaje": 3},
            "sanitario": {"nivel": "Medio", "puntaje": 5}
        },
        "observaciones": "Familia estable, buen control de hipertensión",
        "fecha_registro": "2024-01-17",
        "responsable": "TENS Ana Martínez"
    },
    {
        "sector": "Sector Centro",
        "apellido": "Reyes",
        "num_integrantes": 5,
        "jefe_hogar": {
            "nombre": "Sofía Reyes",
            "edad": 44,
            "ocupacion": "Profesora"
        },
        "vivienda": {
            "tipo": "Departamento",
            "hacinamiento": "Medio",
            "red_apoyo": "Fuerte",
            "participacion_social": "Alta",
            "acceso_aps": "Fácil"
        },
        "salud": {
            "enfermedades_cronicas": ["Obesidad"],
            "embarazo_adolescente": False,
            "violencia_intrafamiliar": False,
            "consumo_drogas": False,
            "desempleo": False,
            "discapacidad": False,
            "adulto_mayor": False
        },
        "riesgos": {
            "social": {"nivel": "Bajo", "puntaje": 2},
            "sanitario": {"nivel": "Medio", "puntaje": 6}
        },
        "observaciones": "Familia funcional, requiere educación en hábitos saludables",
        "fecha_registro": "2024-01-17",
        "responsable": "TENS María González"
    },
    {
        "sector": "Sector Sur",
        "apellido": "Navarro",
        "num_integrantes": 4,
        "jefe_hogar": {
            "nombre": "Carlos Navarro",
            "edad": 31,
            "ocupacion": "Agricultor"
        },
        "vivienda": {
            "tipo": "Casa",
            "hacinamiento": "Medio",
            "red_apoyo": "Regular",
            "participacion_social": "Media",
            "acceso_aps": "Difícil"
        },
        "salud": {
            "enfermedades_cronicas": ["Diabetes"],
            "embarazo_adolescente": False,
            "violencia_intrafamiliar": False,
            "consumo_drogas": False,
            "desempleo": False,
            "discapacidad": False,
            "adulto_mayor": False
        },
        "riesgos": {
            "social": {"nivel": "Medio", "puntaje": 6},
            "sanitario": {"nivel": "Medio", "puntaje": 7}
        },
        "observaciones": "Familia rural, requiere apoyo en control de diabetes",
        "fecha_registro": "2024-01-18",
        "responsable": "TENS Carlos Ramírez"
    },
    {
        "sector": "Sector Norte",
        "apellido": "Jiménez",
        "num_integrantes": 6,
        "jefe_hogar": {
            "nombre": "Alejandra Jiménez",
            "edad": 36,
            "ocupacion": "Vendedora"
        },
        "vivienda": {
            "tipo": "Departamento",
            "hacinamiento": "Alto",
            "red_apoyo": "Regular",
            "participacion_social": "Media",
            "acceso_aps": "Fácil"
        },
        "salud": {
            "enfermedades_cronicas": ["Hipertensión"],
            "embarazo_adolescente": False,
            "violencia_intrafamiliar": False,
            "consumo_drogas": False,
            "desempleo": False,
            "discapacidad": False,
            "adulto_mayor": False
        },
        "riesgos": {
            "social": {"nivel": "Medio", "puntaje": 8},
            "sanitario": {"nivel": "Medio", "puntaje": 6}
        },
        "observaciones": "Familia numerosa, requiere apoyo en control de hipertensión y hacinamiento",
        "fecha_registro": "2024-01-18",
        "responsable": "TENS Ana Martínez"
    }
]

# Datos de ejemplo para instituciones
INSTITUCIONES_EJEMPLO = [
    {
        "nombre": "Escuela Básica San José",
        "tipo": "Educación",
        "sectores_cobertura": ["Sector Norte", "Sector Centro"],
        "contacto": {
            "nombre": "Prof. María Elena Torres",
            "telefono": "+56 9 4567 8901",
            "email": "director@escuelasanjose.cl"
        },
        "informacion": {
            "horario": "Lunes a Viernes 8:00-16:00",
            "modalidad": "Presencial",
            "nivel_coordinacion": "Excelente",
            "frecuencia_contacto": "Semanal"
        },
        "recursos": ["Espacios físicos", "Programas educativos", "Personal especializado"],
        "poblacion_objetivo": ["Niños y adolescentes", "Familias"],
        "programas_servicios": "Programa de alimentación escolar, talleres de salud, apoyo psicosocial",
        "fortalezas": "Personal capacitado, buena infraestructura, programas establecidos",
        "debilidades": "Horarios limitados, recursos tecnológicos limitados",
        "oportunidades_trabajo": "Talleres de prevención, educación en salud, detección temprana de problemas",
        "fecha_registro": "2024-01-10"
    },
    {
        "nombre": "Municipalidad de San Pedro",
        "tipo": "Municipalidad",
        "sectores_cobertura": ["Sector Norte", "Sector Centro", "Sector Sur"],
        "contacto": {
            "nombre": "Sra. Ana María Silva",
            "telefono": "+56 9 5678 9012",
            "email": "desarrollo.social@municipalidad.cl"
        },
        "informacion": {
            "horario": "Lunes a Viernes 8:30-17:30",
            "modalidad": "Presencial",
            "nivel_coordinacion": "Buena",
            "frecuencia_contacto": "Quincenal"
        },
        "recursos": ["Presupuesto", "Personal especializado", "Programas sociales"],
        "poblacion_objetivo": ["Población general", "Familias", "Adultos mayores"],
        "programas_servicios": "Programa de vivienda, apoyo social, actividades comunitarias",
        "fortalezas": "Recursos presupuestarios, programas establecidos, cobertura amplia",
        "debilidades": "Burocracia, tiempos de respuesta lentos",
        "oportunidades_trabajo": "Proyectos conjuntos, coordinación de recursos, trabajo comunitario",
        "fecha_registro": "2024-01-10"
    },
    {
        "nombre": "Centro de Salud Familiar (CESFAM)",
        "tipo": "Salud",
        "sectores_cobertura": ["Sector Centro"],
        "contacto": {
            "nombre": "Dr. Roberto Castro",
            "telefono": "+56 9 6789 0123",
            "email": "director@cesfam.cl"
        },
        "informacion": {
            "horario": "Lunes a Viernes 8:00-17:00",
            "modalidad": "Presencial",
            "nivel_coordinacion": "Excelente",
            "frecuencia_contacto": "Diario"
        },
        "recursos": ["Personal especializado", "Equipamiento", "Atención psicológica"],
        "poblacion_objetivo": ["Población general", "Familias", "Adultos mayores"],
        "programas_servicios": "Atención primaria, programas preventivos, salud mental",
        "fortalezas": "Personal capacitado, equipamiento adecuado, programas integrales",
        "debilidades": "Horarios limitados, alta demanda",
        "oportunidades_trabajo": "Coordinación de atención, derivaciones, programas conjuntos",
        "fecha_registro": "2024-01-10"
    },
    {
        "nombre": "Centro Comunitario Los Pinos",
        "tipo": "Comunitario",
        "sectores_cobertura": ["Sector Norte"],
        "contacto": {
            "nombre": "Sra. Carmen López",
            "telefono": "+56 9 7890 1234",
            "email": "director@centropinos.cl"
        },
        "informacion": {
            "horario": "Lunes a Sábado 9:00-21:00",
            "modalidad": "Presencial",
            "nivel_coordinacion": "Buena",
            "frecuencia_contacto": "Semanal"
        },
        "recursos": ["Espacios de reunión", "Sala de computación", "Talleres", "Área deportiva"],
        "poblacion_objetivo": ["Familias", "Jóvenes", "Adultos mayores"],
        "programas_servicios": "Talleres de manualidades, computación, deportes, actividades culturales",
        "fortalezas": "Espacios amplios, horarios flexibles, personal comprometido",
        "debilidades": "Recursos limitados, dependencia de financiamiento externo",
        "oportunidades_trabajo": "Talleres de salud, actividades preventivas, reuniones comunitarias",
        "fecha_registro": "2024-01-11"
    },
    {
        "nombre": "Junta de Vecinos Sector Sur",
        "tipo": "Organización Comunitaria",
        "sectores_cobertura": ["Sector Sur"],
        "contacto": {
            "nombre": "Sr. Manuel Rojas",
            "telefono": "+56 9 8901 2345",
            "email": "presidente@juntasursur.cl"
        },
        "informacion": {
            "horario": "Lunes a Viernes 18:00-20:00",
            "modalidad": "Presencial",
            "nivel_coordinacion": "Regular",
            "frecuencia_contacto": "Mensual"
        },
        "recursos": ["Sede social", "Líderes comunitarios", "Red de contactos"],
        "poblacion_objetivo": ["Vecinos del sector", "Familias"],
        "programas_servicios": "Organización de eventos comunitarios, gestión de mejoras barriales",
        "fortalezas": "Conocimiento del territorio, liderazgo local, participación activa",
        "debilidades": "Recursos limitados, dependencia de voluntarios",
        "oportunidades_trabajo": "Difusión de programas de salud, organización de actividades preventivas",
        "fecha_registro": "2024-01-11"
    },
    {
        "nombre": "Centro de Rehabilitación San Juan",
        "tipo": "Salud",
        "sectores_cobertura": ["Sector Norte", "Sector Centro", "Sector Sur"],
        "contacto": {
            "nombre": "Dra. Patricia Morales",
            "telefono": "+56 9 9012 3456",
            "email": "director@rehabilitacion.cl"
        },
        "informacion": {
            "horario": "Lunes a Viernes 8:00-18:00",
            "modalidad": "Presencial",
            "nivel_coordinacion": "Excelente",
            "frecuencia_contacto": "Semanal"
        },
        "recursos": ["Kinesiólogos", "Terapeutas ocupacionales", "Equipamiento especializado"],
        "poblacion_objetivo": ["Personas con discapacidad", "Adultos mayores", "Pacientes post-operatorios"],
        "programas_servicios": "Rehabilitación física, terapia ocupacional, apoyo psicosocial",
        "fortalezas": "Personal especializado, equipamiento moderno, programas integrales",
        "debilidades": "Cupos limitados, lista de espera",
        "oportunidades_trabajo": "Derivaciones, coordinación de tratamientos, educación en prevención",
        "fecha_registro": "2024-01-12"
    },
    {
        "nombre": "Liceo Técnico Profesional",
        "tipo": "Educación",
        "sectores_cobertura": ["Sector Norte", "Sector Centro"],
        "contacto": {
            "nombre": "Prof. Roberto Silva",
            "telefono": "+56 9 0123 4567",
            "email": "director@liceotecnico.cl"
        },
        "informacion": {
            "horario": "Lunes a Viernes 8:00-18:00",
            "modalidad": "Presencial",
            "nivel_coordinacion": "Buena",
            "frecuencia_contacto": "Quincenal"
        },
        "recursos": ["Aulas", "Laboratorios", "Talleres", "Personal docente"],
        "poblacion_objetivo": ["Adolescentes", "Jóvenes", "Familias"],
        "programas_servicios": "Educación media técnico-profesional, talleres de formación laboral",
        "fortalezas": "Infraestructura adecuada, programas técnicos, vinculación con empresas",
        "debilidades": "Recursos tecnológicos limitados, alta demanda",
        "oportunidades_trabajo": "Educación en salud sexual, prevención de drogas, orientación vocacional",
        "fecha_registro": "2024-01-12"
    },
    {
        "nombre": "Centro de la Mujer",
        "tipo": "Social",
        "sectores_cobertura": ["Sector Norte", "Sector Centro", "Sector Sur"],
        "contacto": {
            "nombre": "Sra. Ana María González",
            "telefono": "+56 9 1234 5678",
            "email": "directora@centromujer.cl"
        },
        "informacion": {
            "horario": "Lunes a Viernes 9:00-17:00",
            "modalidad": "Presencial",
            "nivel_coordinacion": "Excelente",
            "frecuencia_contacto": "Semanal"
        },
        "recursos": ["Psicólogas", "Trabajadoras sociales", "Abogadas", "Espacios de atención"],
        "poblacion_objetivo": ["Mujeres", "Familias afectadas por violencia"],
        "programas_servicios": "Atención psicológica, asesoría legal, apoyo a víctimas de violencia",
        "fortalezas": "Personal especializado, protocolos establecidos, trabajo en red",
        "debilidades": "Cupos limitados, alta demanda",
        "oportunidades_trabajo": "Derivaciones, coordinación de casos, talleres de prevención",
        "fecha_registro": "2024-01-13"
    }
]

# Datos de ejemplo para diagnóstico
DIAGNOSTICO_EJEMPLO = {
    "problema_principal": "Alta prevalencia de violencia intrafamiliar y factores de riesgo social en el Sector Norte y Sur",
    "factores_riesgo": ["Violencia intrafamiliar", "Hacinamiento", "Desempleo", "Falta de acceso a servicios"],
    "recursos_comunidad": "Organizaciones comunitarias activas, escuela con programas establecidos, CESFAM con personal capacitado",
    "grupo_prioritario": "Familias en alto riesgo",
    "justificacion_prioridad": "Las familias en alto riesgo presentan múltiples factores de vulnerabilidad que requieren intervención inmediata para prevenir consecuencias graves en la salud y bienestar familiar",
    "enfoque_intervencion": "Intersectorial",
    "estrategias_propuestas": ["Educación en salud", "Acompañamiento familiar", "Trabajo en red", "Prevención de violencia"],
    "indicadores_evaluacion": ["Reducción de factores de riesgo", "Mejora en acceso a servicios", "Reducción de violencia"],
    "tiempo_intervencion": "Mediano plazo (6-12 meses)",
    "fecha_diagnostico": "2024-01-20 14:30"
}

# Datos de ejemplo para plan de intervención
PLAN_INTERVENCION_EJEMPLO = [
    {
        "nombre": "Taller de Prevención de Violencia Intrafamiliar",
        "tipo": "Preventiva",
        "objetivo_general": "Prevenir la violencia intrafamiliar mediante educación y fortalecimiento de habilidades parentales",
        "sectores_objetivo": ["Sector Norte", "Sector Sur"],
        "poblacion_objetivo": ["Familias en alto riesgo", "Mujeres"],
        "objetivos_especificos": [
            "Identificar factores de riesgo de violencia intrafamiliar",
            "Desarrollar habilidades de comunicación familiar",
            "Establecer redes de apoyo comunitario"
        ],
        "actividades_especificas": [
            "Sesiones educativas grupales",
            "Acompañamiento individual a familias",
            "Coordinación con instituciones de apoyo"
        ],
        "responsables": ["TENS", "Psicólogo", "Trabajador Social"],
        "instituciones_participantes": ["Escuela Básica San José", "Municipalidad de San Pedro"],
        "recursos_necesarios": ["Material educativo", "Espacios físicos", "Personal especializado"],
        "presupuesto_estimado": 500000,
        "cronograma": {
            "fecha_inicio": "2024-02-01",
            "fecha_fin": "2024-05-31",
            "frecuencia": "Semanal"
        },
        "indicadores": [
            "Número de familias participantes",
            "Reducción de casos de violencia reportados",
            "Satisfacción de participantes"
        ],
        "metas": {
            "cuantitativa": "50 familias participarán en el taller",
            "cualitativa": "Mejorar el conocimiento sobre prevención de violencia"
        },
        "riesgos_contingencias": "Baja participación: realizar visitas domiciliarias y coordinación con líderes comunitarios",
        "fecha_creacion": "2024-01-20 15:00",
        "estado": "Planificada"
    },
    {
        "nombre": "Programa de Mejora de Condiciones Habitacionales",
        "tipo": "Asistencial",
        "objetivo_general": "Mejorar las condiciones de vivienda de familias con hacinamiento alto",
        "sectores_objetivo": ["Sector Norte", "Sector Sur"],
        "poblacion_objetivo": ["Familias en alto riesgo"],
        "objetivos_especificos": [
            "Identificar familias con hacinamiento crítico",
            "Coordinar con servicios de vivienda",
            "Proporcionar alternativas habitacionales"
        ],
        "actividades_especificas": [
            "Evaluación habitacional",
            "Coordinación con municipalidad",
            "Seguimiento de casos"
        ],
        "responsables": ["TENS", "Trabajador Social"],
        "instituciones_participantes": ["Municipalidad de San Pedro"],
        "recursos_necesarios": ["Presupuesto", "Personal especializado"],
        "presupuesto_estimado": 2000000,
        "cronograma": {
            "fecha_inicio": "2024-02-15",
            "fecha_fin": "2024-12-31",
            "frecuencia": "Mensual"
        },
        "indicadores": [
            "Número de familias beneficiadas",
            "Mejora en condiciones habitacionales",
            "Reducción de hacinamiento"
        ],
        "metas": {
            "cuantitativa": "20 familias mejorarán sus condiciones habitacionales",
            "cualitativa": "Reducir el hacinamiento crítico en un 50%"
        },
        "riesgos_contingencias": "Falta de recursos: buscar financiamiento alternativo y priorizar casos más críticos",
        "fecha_creacion": "2024-01-20 16:00",
        "estado": "Planificada"
    }
]

# Datos de ejemplo para participación comunitaria
PARTICIPACION_COMUNITARIA_EJEMPLO = {
    'encuestas': [
        {
            'id': 1,
            'tipo': 'Satisfacción de Usuarios',
            'fecha': '2024-01-15',
            'sector': 'Todos los Sectores',
            'num_encuestados': 85,
            'metodo': 'Presencial',
            'duracion': 12,
            'satisfaccion': 4,
            'participacion': 3,
            'necesidades': ['Salud Mental', 'Salud Cardiovascular', 'Salud Infantil'],
            'barreras': ['Horarios de Atención', 'Tiempo de Espera', 'Falta de Especialistas'],
            'observaciones': 'Los usuarios valoran positivamente la atención del personal, pero identifican barreras en horarios y tiempo de espera. Interés moderado en participación comunitaria.'
        },
        {
            'id': 2,
            'tipo': 'Necesidades de Salud',
            'fecha': '2024-01-18',
            'sector': 'Sector A',
            'num_encuestados': 45,
            'metodo': 'Telefónica',
            'duracion': 8,
            'satisfaccion': 3,
            'participacion': 4,
            'necesidades': ['Salud del Adulto Mayor', 'Prevención de Cáncer', 'Salud Sexual y Reproductiva'],
            'barreras': ['Distancia', 'Problemas de Transporte', 'Falta de Información'],
            'observaciones': 'Alto interés en programas preventivos, especialmente para adultos mayores. Barreras de acceso geográfico identificadas.'
        },
        {
            'id': 3,
            'tipo': 'Salud del Adulto Mayor',
            'fecha': '2024-01-22',
            'sector': 'Sector B',
            'num_encuestados': 32,
            'metodo': 'Presencial',
            'duracion': 15,
            'satisfaccion': 4,
            'participacion': 4,
            'necesidades': ['Control de Enfermedades Crónicas', 'Actividad Física', 'Socialización'],
            'barreras': ['Movilidad Reducida', 'Falta de Acompañamiento', 'Horarios Inadecuados'],
            'observaciones': 'Alta demanda de actividades grupales y control de enfermedades crónicas. Necesidad de transporte y acompañamiento.'
        },
        {
            'id': 4,
            'tipo': 'Salud Sexual y Reproductiva',
            'fecha': '2024-01-25',
            'sector': 'Sector C',
            'num_encuestados': 28,
            'metodo': 'Digital',
            'duracion': 10,
            'satisfaccion': 3,
            'participacion': 2,
            'necesidades': ['Educación Sexual', 'Acceso a Anticonceptivos', 'Prevención de ITS'],
            'barreras': ['Tabúes Culturales', 'Falta de Privacidad', 'Horarios Limitados'],
            'observaciones': 'Baja participación debido a tabúes culturales. Necesidad de abordaje sensible y confidencial.'
        },
        {
            'id': 5,
            'tipo': 'Prevención de Obesidad Infantil',
            'fecha': '2024-01-28',
            'sector': 'Todos los Sectores',
            'num_encuestados': 67,
            'metodo': 'Presencial',
            'duracion': 8,
            'satisfaccion': 4,
            'participacion': 4,
            'necesidades': ['Educación Nutricional', 'Actividad Física', 'Control de Peso'],
            'barreras': ['Falta de Tiempo', 'Recursos Económicos', 'Espacios Deportivos'],
            'observaciones': 'Alto interés en programas de prevención. Familias dispuestas a participar en talleres educativos.'
        }
    ],
    'grupos_focales': [
        {
            'id': 1,
            'tema': 'Necesidades de Salud Mental',
            'fecha': '2024-01-20',
            'participantes': 12,
            'perfil': 'Usuarios del CESFAM',
            'duracion': 2.0,
            'facilitador': 'Psicóloga María González',
            'preguntas': [
                '¿Qué problemas de salud mental son más frecuentes en la comunidad?',
                '¿Qué barreras identifican para acceder a atención en salud mental?',
                '¿Cómo les gustaría que se aborden estos problemas?',
                '¿Qué rol debería tener la comunidad en la promoción de salud mental?'
            ],
            'hallazgos_positivos': 'Alto interés en talleres de manejo del estrés y ansiedad. Reconocimiento de la importancia de la salud mental.',
            'hallazgos_negativos': 'Estigma hacia problemas de salud mental. Falta de especialistas en el CESFAM.',
            'recomendaciones': 'Implementar talleres grupales, capacitar al equipo en primeros auxilios psicológicos, coordinar con especialistas externos.',
            'participacion': 4,
            'satisfaccion': 5
        },
        {
            'id': 2,
            'tema': 'Prevención de Diabetes',
            'fecha': '2024-01-23',
            'participantes': 15,
            'perfil': 'Personas con prediabetes y familiares',
            'duracion': 1.5,
            'facilitador': 'Nutricionista Carmen Silva',
            'preguntas': [
                '¿Qué saben sobre la diabetes y sus factores de riesgo?',
                '¿Qué barreras identifican para mantener una alimentación saludable?',
                '¿Cómo les gustaría recibir educación sobre diabetes?',
                '¿Qué apoyo necesitan de la familia y la comunidad?'
            ],
            'hallazgos_positivos': 'Alto interés en aprender sobre alimentación saludable. Reconocimiento de la importancia del ejercicio.',
            'hallazgos_negativos': 'Falta de conocimiento sobre diabetes. Barreras económicas para alimentación saludable.',
            'recomendaciones': 'Talleres de cocina saludable, grupos de apoyo, educación familiar, coordinación con programas de alimentación.',
            'participacion': 5,
            'satisfaccion': 4
        },
        {
            'id': 3,
            'tema': 'Violencia Intrafamiliar',
            'fecha': '2024-01-26',
            'participantes': 8,
            'perfil': 'Mujeres víctimas de violencia',
            'duracion': 2.5,
            'facilitador': 'Trabajadora Social Patricia Rojas',
            'preguntas': [
                '¿Qué tipos de violencia han experimentado?',
                '¿Qué barreras identifican para denunciar?',
                '¿Qué apoyo necesitan para salir de la situación?',
                '¿Cómo puede la comunidad ayudar a prevenir la violencia?'
            ],
            'hallazgos_positivos': 'Valoración del apoyo profesional. Interés en grupos de apoyo.',
            'hallazgos_negativos': 'Miedo a denunciar, dependencia económica, falta de redes de apoyo.',
            'recomendaciones': 'Protocolos de derivación, grupos de apoyo, capacitación en detección temprana, coordinación con instituciones especializadas.',
            'participacion': 3,
            'satisfaccion': 4
        },
        {
            'id': 4,
            'tema': 'Actividad Física en Adultos Mayores',
            'fecha': '2024-01-29',
            'participantes': 20,
            'perfil': 'Adultos mayores activos',
            'duracion': 1.0,
            'facilitador': 'Kinesiólogo Roberto Díaz',
            'preguntas': [
                '¿Qué actividades físicas realizan actualmente?',
                '¿Qué barreras identifican para hacer ejercicio?',
                '¿Qué tipo de actividades les gustaría realizar?',
                '¿Cómo puede la comunidad facilitar la actividad física?'
            ],
            'hallazgos_positivos': 'Alto interés en actividades grupales. Reconocimiento de los beneficios del ejercicio.',
            'hallazgos_negativos': 'Falta de espacios adecuados, problemas de movilidad, horarios inadecuados.',
            'recomendaciones': 'Programas de ejercicio adaptado, espacios seguros, horarios flexibles, transporte comunitario.',
            'participacion': 5,
            'satisfaccion': 5
        }
    ],
    'analisis_foda': {
        'fortalezas': [
            {
                'id': 1,
                'elemento': 'Programa Cardiovascular Consolidado',
                'descripcion': 'Programa bien establecido con buenos resultados y alta participación de usuarios',
                'impacto': 'Alto',
                'prioridad': 'Alta',
                'sector': 'CESFAM'
            },
            {
                'id': 2,
                'elemento': 'Equipo Multidisciplinario',
                'descripcion': 'Personal capacitado y comprometido con el trabajo comunitario',
                'impacto': 'Alto',
                'prioridad': 'Alta',
                'sector': 'CESFAM'
            },
            {
                'id': 3,
                'elemento': 'Líderes Comunitarios Activos',
                'descripcion': 'Comunidad organizada con líderes comprometidos con la salud',
                'impacto': 'Medio',
                'prioridad': 'Media',
                'sector': 'Comunidad'
            }
        ],
        'oportunidades': [
            {
                'id': 1,
                'elemento': 'Fondo de Desarrollo Regional',
                'descripcion': 'Disponibilidad de recursos para proyectos de salud comunitaria',
                'impacto': 'Alto',
                'prioridad': 'Alta',
                'sector': 'Ambos'
            },
            {
                'id': 2,
                'elemento': 'Alianza con Universidad Local',
                'descripcion': 'Posibilidad de investigación y capacitación conjunta',
                'impacto': 'Medio',
                'prioridad': 'Media',
                'sector': 'CESFAM'
            }
        ],
        'debilidades': [
            {
                'id': 1,
                'elemento': 'Escasez de Horas de Especialistas',
                'descripcion': 'Limitada disponibilidad de especialistas para control de complicaciones',
                'impacto': 'Alto',
                'prioridad': 'Alta',
                'sector': 'CESFAM'
            },
            {
                'id': 2,
                'elemento': 'Infraestructura Limitada',
                'descripcion': 'Espacios insuficientes para actividades grupales y talleres',
                'impacto': 'Medio',
                'prioridad': 'Media',
                'sector': 'CESFAM'
            },
            {
                'id': 3,
                'elemento': 'Baja Participación de Hombres',
                'descripcion': 'Menor participación masculina en actividades preventivas',
                'impacto': 'Medio',
                'prioridad': 'Media',
                'sector': 'Comunidad'
            }
        ],
        'amenazas': [
            {
                'id': 1,
                'elemento': 'Recorte Presupuestario',
                'descripcion': 'Posible reducción de recursos para programas comunitarios',
                'impacto': 'Alto',
                'prioridad': 'Alta',
                'sector': 'CESFAM'
            },
            {
                'id': 2,
                'elemento': 'Cambio de Autoridades',
                'descripcion': 'Riesgo de cambio de prioridades con nueva gestión municipal',
                'impacto': 'Medio',
                'prioridad': 'Media',
                'sector': 'Ambos'
            }
        ]
    },
    'plan_anual': [
        {
            'id': 1,
            'nombre': 'Programa de Salud Mental Comunitaria',
            'tipo': 'Preventiva',
            'objetivo': 'Mejorar el acceso y la calidad de la atención en salud mental',
            'sector': 'Todos los Sectores',
            'poblacion': 'Toda la Comunidad',
            'prioridad': 'Alta',
            'fecha_inicio': '2024-03-01',
            'fecha_fin': '2024-12-31',
            'frecuencia': 'Semanal',
            'responsable': 'Psicóloga María González',
            'equipo': 'Equipo de Salud Mental, TENS, Líderes Comunitarios',
            'recursos': 'Sala de talleres, materiales educativos, presupuesto para especialistas',
            'presupuesto': 1500000,
            'indicadores': 'Número de talleres realizados, participantes, satisfacción, reducción de síntomas de ansiedad',
            'fortalezas': ['Equipo Multidisciplinario'],
            'debilidades': ['Escasez de Horas de Especialistas'],
            'oportunidades': ['Fondo de Desarrollo Regional'],
            'amenazas': ['Recorte Presupuestario']
        },
        {
            'id': 2,
            'nombre': 'Mejora de Infraestructura para Actividades Grupales',
            'tipo': 'Promocional',
            'objetivo': 'Ampliar espacios para actividades comunitarias y talleres',
            'sector': 'Todos los Sectores',
            'poblacion': 'Toda la Comunidad',
            'prioridad': 'Media',
            'fecha_inicio': '2024-04-01',
            'fecha_fin': '2024-08-31',
            'frecuencia': 'Una vez',
            'responsable': 'Administrador CESFAM',
            'equipo': 'Equipo Administrativo, Técnicos',
            'recursos': 'Presupuesto municipal, materiales de construcción',
            'presupuesto': 3000000,
            'indicadores': 'Espacios habilitados, capacidad de usuarios, satisfacción',
            'fortalezas': ['Programa Cardiovascular Consolidado'],
            'debilidades': ['Infraestructura Limitada'],
            'oportunidades': ['Fondo de Desarrollo Regional'],
            'amenazas': ['Recorte Presupuestario']
        }
    ]
}

# Datos de ejemplo para epidemiología
EPIDEMIOLOGIA_EJEMPLO = {
    'indicadores_basicos': [
        {
            'id': 1,
            'tipo': 'Morbilidad',
            'fecha': '2024-01-15',
            'sector': 'Todos los Sectores',
            'periodo': 'Último mes',
            'fuente': 'Fichas clínicas',
            'observaciones': 'Alta incidencia de infecciones respiratorias en invierno',
            'casos_nuevos': 45,
            'casos_existentes': 120,
            'poblacion_riesgo': 1000,
            'incidencia': 45.0,
            'prevalencia': 120.0
        },
        {
            'id': 2,
            'tipo': 'Mortalidad',
            'fecha': '2024-01-20',
            'sector': 'Todos los Sectores',
            'periodo': 'Último año',
            'fuente': 'Sistema de información',
            'observaciones': 'Mortalidad principalmente por enfermedades cardiovasculares',
            'defunciones': 8,
            'poblacion_total': 1000,
            'tasa_mortalidad': 8.0,
            'causas': ['Enfermedades cardiovasculares', 'Cáncer']
        },
        {
            'id': 3,
            'tipo': 'Demográfico',
            'fecha': '2024-01-25',
            'sector': 'Todos los Sectores',
            'periodo': 'Último año',
            'fuente': 'Censo comunal',
            'observaciones': 'Población envejecida con alto índice de dependencia',
            'poblacion_total': 1000,
            'menores_15': 180,
            'mayores_65': 220,
            'indice_dependencia': 40.0
        },
        {
            'id': 4,
            'tipo': 'Natalidad',
            'fecha': '2024-01-30',
            'sector': 'Todos los Sectores',
            'periodo': 'Último año',
            'fuente': 'Registro civil',
            'observaciones': 'Baja natalidad, algunos embarazos adolescentes',
            'nacimientos': 12,
            'poblacion_total': 1000,
            'tasa_natalidad': 12.0,
            'embarazos_adolescentes': 3
        },
        {
            'id': 5,
            'tipo': 'Vacunación',
            'fecha': '2024-02-01',
            'sector': 'Todos los Sectores',
            'periodo': 'Último mes',
            'fuente': 'Programa de inmunizaciones',
            'observaciones': 'Cobertura adecuada en niños, baja en adultos',
            'poblacion_objetivo': 200,
            'vacunados': 180,
            'cobertura': 90.0,
            'vacunas': ['Influenza', 'COVID-19', 'Neumococo']
        }
    ],
    'patologias_prioritarias': [
        {
            'id': 1,
            'patologia': 'Diabetes Mellitus',
            'fecha': '2024-01-15',
            'sector': 'Todos los Sectores',
            'prioridad': 'Alta',
            'tendencia': 'En aumento',
            'casos_activos': 45,
            'casos_nuevos': 8,
            'poblacion': 1000,
            'edad_promedio': 58,
            'prevalencia': 45.0,
            'incidencia_mensual': 8.0,
            'factores_asociados': ['Obesidad', 'Sedentarismo', 'Mala alimentación'],
            'intervenciones': ['Educación en salud', 'Control nutricional', 'Programa de ejercicio'],
            'observaciones': 'Alta prevalencia en adultos mayores, necesidad de intervenciones preventivas'
        },
        {
            'id': 2,
            'patologia': 'Hipertensión Arterial',
            'fecha': '2024-01-20',
            'sector': 'Todos los Sectores',
            'prioridad': 'Alta',
            'tendencia': 'Estable',
            'casos_activos': 65,
            'casos_nuevos': 5,
            'poblacion': 1000,
            'edad_promedio': 62,
            'prevalencia': 65.0,
            'incidencia_mensual': 5.0,
            'factores_asociados': ['Obesidad', 'Estrés', 'Mala alimentación'],
            'intervenciones': ['Control médico regular', 'Educación en salud', 'Apoyo psicológico'],
            'observaciones': 'Patología más frecuente en la población, buen control en la mayoría de casos'
        },
        {
            'id': 3,
            'patologia': 'Obesidad',
            'fecha': '2024-01-25',
            'sector': 'Todos los Sectores',
            'prioridad': 'Media',
            'tendencia': 'En aumento',
            'casos_activos': 85,
            'casos_nuevos': 12,
            'poblacion': 1000,
            'edad_promedio': 45,
            'prevalencia': 85.0,
            'incidencia_mensual': 12.0,
            'factores_asociados': ['Mala alimentación', 'Sedentarismo', 'Factores genéticos'],
            'intervenciones': ['Educación nutricional', 'Programas de ejercicio', 'Control de peso'],
            'observaciones': 'Alta prevalencia en adultos, necesidad de intervenciones preventivas desde la infancia'
        },
        {
            'id': 4,
            'patologia': 'Depresión',
            'fecha': '2024-01-28',
            'sector': 'Todos los Sectores',
            'prioridad': 'Alta',
            'tendencia': 'En aumento',
            'casos_activos': 25,
            'casos_nuevos': 6,
            'poblacion': 1000,
            'edad_promedio': 52,
            'prevalencia': 25.0,
            'incidencia_mensual': 6.0,
            'factores_asociados': ['Estrés', 'Aislamiento social', 'Problemas económicos'],
            'intervenciones': ['Atención psicológica', 'Grupos de apoyo', 'Actividades sociales'],
            'observaciones': 'Subdiagnosticada, necesidad de mejorar detección y acceso a tratamiento'
        },
        {
            'id': 5,
            'patologia': 'Violencia Intrafamiliar',
            'fecha': '2024-02-01',
            'sector': 'Todos los Sectores',
            'prioridad': 'Alta',
            'tendencia': 'Estable',
            'casos_activos': 15,
            'casos_nuevos': 3,
            'poblacion': 1000,
            'edad_promedio': 38,
            'prevalencia': 15.0,
            'incidencia_mensual': 3.0,
            'factores_asociados': ['Alcoholismo', 'Problemas económicos', 'Historia familiar'],
            'intervenciones': ['Detección temprana', 'Derivación especializada', 'Apoyo psicosocial'],
            'observaciones': 'Subregistrada, necesidad de protocolos de detección y derivación'
        }
    ],
    'vigilancia_epidemiologica': [
        {
            'id': 1,
            'evento': 'Infección Respiratoria',
            'fecha_inicio': '2024-01-01',
            'fecha_fin': '2024-01-31',
            'nivel_alerta': 'Atención',
            'sector': 'Todos los Sectores',
            'casos_sospechosos': 25,
            'casos_confirmados': 15,
            'casos_graves': 2,
            'defunciones': 0,
            'poblacion_expuesta': 1000,
            'tasa_ataque': 1.5,
            'grupo_edad': ['0-4 años', '5-14 años'],
            'sintomas': ['Fiebre', 'Tos', 'Dolor de cabeza'],
            'factores_riesgo': ['Hacinamiento', 'Contacto con enfermos'],
            'acciones': ['Educación comunitaria', 'Refuerzo de medidas preventivas'],
            'estado': 'Controlado'
        },
        {
            'id': 2,
            'evento': 'Gastroenteritis',
            'fecha_inicio': '2024-01-15',
            'fecha_fin': '2024-01-25',
            'nivel_alerta': 'Bajo',
            'sector': 'Sector Sur',
            'casos_sospechosos': 8,
            'casos_confirmados': 5,
            'casos_graves': 0,
            'defunciones': 0,
            'poblacion_expuesta': 300,
            'tasa_ataque': 1.7,
            'grupo_edad': ['0-4 años', 'Adultos'],
            'sintomas': ['Diarrea', 'Vómitos', 'Fiebre'],
            'factores_riesgo': ['Agua contaminada', 'Mala higiene'],
            'acciones': ['Educación en higiene', 'Cloración de agua'],
            'estado': 'Controlado'
        },
        {
            'id': 3,
            'evento': 'Dengue',
            'fecha_inicio': '2024-01-20',
            'fecha_fin': '2024-02-05',
            'nivel_alerta': 'Alto',
            'sector': 'Todos los Sectores',
            'casos_sospechosos': 12,
            'casos_confirmados': 8,
            'casos_graves': 1,
            'defunciones': 0,
            'poblacion_expuesta': 1000,
            'tasa_ataque': 0.8,
            'grupo_edad': ['Todas las edades'],
            'sintomas': ['Fiebre', 'Dolor de cabeza', 'Dolor muscular'],
            'factores_riesgo': ['Presencia de mosquitos', 'Agua estancada'],
            'acciones': ['Control vectorial', 'Educación comunitaria', 'Eliminación de criaderos'],
            'estado': 'En seguimiento'
        }
    ],
    'factores_riesgo': [
        {
            'id': 1,
            'factor': 'Obesidad',
            'fecha': '2024-01-15',
            'sector': 'Todos los Sectores',
            'nivel_riesgo': 'Alto',
            'tendencia': 'En aumento',
            'prevalencia': 35.0,
            'poblacion_expuesta': 350,
            'edad_promedio': 45,
            'genero': 'Ambos',
            'impacto_poblacional': 350,
            'patologias_asociadas': ['Diabetes', 'Hipertensión', 'Enfermedades cardiovasculares'],
            'intervenciones': ['Educación en salud', 'Programa de ejercicio', 'Apoyo nutricional'],
            'observaciones': 'Factor de riesgo más prevalente, requiere intervención multisectorial'
        },
        {
            'id': 2,
            'factor': 'Sedentarismo',
            'fecha': '2024-01-20',
            'sector': 'Todos los Sectores',
            'nivel_riesgo': 'Medio',
            'tendencia': 'Estable',
            'prevalencia': 60.0,
            'poblacion_expuesta': 600,
            'edad_promedio': 40,
            'genero': 'Hombres',
            'impacto_poblacional': 600,
            'patologias_asociadas': ['Obesidad', 'Enfermedades cardiovasculares'],
            'intervenciones': ['Programa de ejercicio', 'Educación en salud'],
            'observaciones': 'Alta prevalencia, especialmente en población económicamente activa'
        }
    ],
    'analisis_geografico': [
        {
            'id': 1,
            'evento': 'Diabetes',
            'fecha': '2024-01-25',
            'tipo_analisis': 'Prevalencia',
            'unidad_geografica': 'Sector',
            'periodo': 'Último año',
            'sector_a': {'casos': 18, 'poblacion': 300, 'tasa': 60.0},
            'sector_b': {'casos': 15, 'poblacion': 400, 'tasa': 37.5},
            'sector_c': {'casos': 12, 'poblacion': 300, 'tasa': 40.0},
            'cluster': 'Sí',
            'caracteristicas_cluster': 'Mayor prevalencia en Sector A, población más envejecida',
            'factores_cluster': ['Pobreza', 'Bajo nivel educacional'],
            'intervenciones': ['Focalización en sector específico', 'Educación comunitaria'],
            'observaciones': 'Cluster identificado en Sector A, requiere intervención focalizada'
        }
    ]
}

# Datos de ejemplo para autoevaluación
AUTOEVALUACION_EJEMPLO = {
    "comprension_conceptos": 4,
    "aplicacion_metodologia": 4,
    "analisis_datos": 3,
    "formulacion_diagnostico": 4,
    "planificacion_intervencion": 3,
    "trabajo_equipo": 5,
    "reflexion_personal": "Este proceso me ha permitido comprender mejor la complejidad del trabajo en salud familiar. Aprendí la importancia de la coordinación intersectorial y el trabajo en red. Lo más desafiante fue priorizar las intervenciones considerando los recursos disponibles.",
    "fortalezas": "Buen trabajo en equipo, capacidad de análisis, comunicación efectiva",
    "areas_mejora": "Análisis estadístico más profundo, planificación de recursos, evaluación de impacto",
    "fecha_evaluacion": "2024-01-20 17:00"
}

def cargar_datos_ejemplo():
    """
    Función para cargar datos de ejemplo en la aplicación
    """
    import streamlit as st
    
    if st.button("📋 Cargar Datos de Ejemplo", type="primary"):
        # Cargar sectores
        st.session_state.sectores = SECTORES_EJEMPLO.copy()
        
        # Cargar equipos
        st.session_state.equipos = EQUIPOS_EJEMPLO.copy()
        
        # Cargar familias
        st.session_state.familias = FAMILIAS_EJEMPLO.copy()
        
        # Cargar instituciones
        st.session_state.instituciones = INSTITUCIONES_EJEMPLO.copy()
        
        # Cargar diagnóstico
        st.session_state.diagnostico = DIAGNOSTICO_EJEMPLO.copy()
        
        # Cargar plan de intervención
        st.session_state.plan_intervencion = PLAN_INTERVENCION_EJEMPLO.copy()
        
        # Cargar participación comunitaria
        st.session_state.participacion_comunitaria = PARTICIPACION_COMUNITARIA_EJEMPLO.copy()
        
        # Cargar epidemiología
        st.session_state.epidemiologia = EPIDEMIOLOGIA_EJEMPLO.copy()
        
        # Cargar autoevaluación
        st.session_state.autoevaluacion = AUTOEVALUACION_EJEMPLO.copy()
        
        st.success("✅ Datos de ejemplo cargados exitosamente!")
        st.info("Ahora puedes explorar todas las secciones de la aplicación con datos de ejemplo.")
        st.rerun()

if __name__ == "__main__":
    print("Datos de ejemplo para el Simulador Comunitario")
    print("Este archivo contiene datos ficticios para demostrar la funcionalidad") 