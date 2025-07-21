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
            'observaciones': 'Aumento estacional esperado, casos leves en su mayoría'
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