import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import random

def analizar_datos_comunidad():
    """
    Analiza todos los datos registrados en la comunidad y retorna un diagnóstico inteligente
    """
    diagnostico = {
        'problemas_prioritarios': [],
        'fortalezas_comunitarias': [],
        'poblaciones_vulnerables': [],
        'recursos_disponibles': [],
        'oportunidades_intervencion': []
    }

    # Analizar familias registradas
    if hasattr(st.session_state, 'familias') and st.session_state.familias:
        familias = st.session_state.familias

        # Problemas más frecuentes
        problemas = {
            'diabetes': 0,
            'hipertension': 0,
            'obesidad': 0,
            'hacinamiento': 0,
            'violencia_intrafamiliar': 0,
            'consumo_drogas': 0,
            'embarazo_adolescente': 0,
            'desempleo': 0,
            'baja_escolaridad': 0,
            'acceso_salud': 0
        }

        for familia in familias:
            try:
                # Enfermedades crónicas
                salud = familia.get('salud', {})
                if isinstance(salud, dict):
                    if salud.get('diabetes', False):
                        problemas['diabetes'] += 1
                    if salud.get('hipertension', False):
                        problemas['hipertension'] += 1
                    if salud.get('obesidad', False):
                        problemas['obesidad'] += 1
                    if salud.get('violencia_intrafamiliar', False):
                        problemas['violencia_intrafamiliar'] += 1
                    if salud.get('consumo_drogas', False):
                        problemas['consumo_drogas'] += 1
                    if salud.get('embarazo_adolescente', False):
                        problemas['embarazo_adolescente'] += 1

                # Condiciones sociales
                vivienda = familia.get('vivienda', {})
                if isinstance(vivienda, dict) and vivienda.get('hacinamiento') == 'Alto':
                    problemas['hacinamiento'] += 1

                # Condiciones económicas
                economia = familia.get('economia', {})
                if isinstance(economia, dict) and economia.get('desempleo', False):
                    problemas['desempleo'] += 1
                
                educacion = familia.get('educacion', {})
                if isinstance(educacion, dict) and educacion.get('baja_escolaridad', False):
                    problemas['baja_escolaridad'] += 1
                
                acceso_aps = familia.get('acceso_aps', {})
                if isinstance(acceso_aps, dict) and not acceso_aps.get('acceso_facil', True):
                    problemas['acceso_salud'] += 1
                    
            except Exception as e:
                # Si hay algún error con una familia específica, continuamos con la siguiente
                continue

        # Identificar problemas prioritarios (más del 30% de las familias)
        total_familias = len(familias)
        if total_familias > 0:
            for problema, cantidad in problemas.items():
                porcentaje = (cantidad / total_familias) * 100
                if porcentaje >= 30:
                    diagnostico['problemas_prioritarios'].append({
                        'problema': problema,
                        'cantidad': cantidad,
                        'porcentaje': porcentaje
                    })

    # Analizar sectores
    if hasattr(st.session_state, 'sectores') and st.session_state.sectores:
        sectores = st.session_state.sectores

        for sector in sectores:
            if sector.get('vulnerabilidad') == 'Alta':
                diagnostico['poblaciones_vulnerables'].append(f"Sector {sector.get('nombre', 'Desconocido')}")

            # Identificar fortalezas
            if sector.get('caracteristicas'):
                diagnostico['fortalezas_comunitarias'].extend(sector['caracteristicas'])

    # Analizar red de trabajo
    if hasattr(st.session_state, 'red_intersectoral') and st.session_state.red_intersectoral:
        instituciones = st.session_state.red_intersectoral

        for institucion in instituciones:
            if institucion.get('tipo') in ['Educación', 'Deportes', 'Cultura']:
                diagnostico['recursos_disponibles'].append(institucion.get('nombre', 'Institución'))

    return diagnostico

def generar_sugerencias_intervenciones(diagnostico):
    """
    Genera sugerencias automáticas de intervenciones basadas en el diagnóstico
    """
    sugerencias = []
    
    # Base de datos de intervenciones por problema
    intervenciones_por_problema = {
        'diabetes': [
            {
                'nombre': 'Programa de Educación Diabetológica',
                'tipo': 'Preventiva',
                'objetivo': 'Mejorar el control de la diabetes y prevenir complicaciones',
                'poblacion': 'Personas con diabetes y sus familias',
                'actividades': [
                    'Talleres de educación en diabetes',
                    'Grupos de apoyo para diabéticos',
                    'Control de glicemia domiciliario',
                    'Educación nutricional específica'
                ],
                'duracion': '6 meses',
                'frecuencia': 'Semanal',
                'recursos': 'Educador en diabetes, nutricionista, glucómetros',
                'indicadores': 'Control glicémico, adherencia al tratamiento, complicaciones'
            },
            {
                'nombre': 'Talleres de Cocina Saludable',
                'tipo': 'Promocional',
                'objetivo': 'Enseñar preparación de alimentos saludables para diabéticos',
                'poblacion': 'Familias con miembros diabéticos',
                'actividades': [
                    'Clases de cocina práctica',
                    'Recetarios saludables',
                    'Planificación de menús semanales'
                ],
                'duracion': '3 meses',
                'frecuencia': 'Quincenal',
                'recursos': 'Cocina equipada, nutricionista, ingredientes',
                'indicadores': 'Cambios en hábitos alimentarios, control de peso'
            }
        ],
        'hipertension': [
            {
                'nombre': 'Programa de Control de Hipertensión',
                'tipo': 'Preventiva',
                'objetivo': 'Controlar la presión arterial y prevenir complicaciones cardiovasculares',
                'poblacion': 'Personas con hipertensión arterial',
                'actividades': [
                    'Control de presión arterial regular',
                    'Educación sobre medicamentos',
                    'Talleres de reducción de sodio',
                    'Actividad física adaptada'
                ],
                'duracion': '12 meses',
                'frecuencia': 'Mensual',
                'recursos': 'Tensiómetros, educador en salud, monitor de actividad física',
                'indicadores': 'Control de presión arterial, adherencia al tratamiento'
            }
        ],
        'obesidad': [
            {
                'nombre': 'Programa de Actividad Física Comunitaria',
                'tipo': 'Promocional',
                'objetivo': 'Promover hábitos de vida saludable y control de peso',
                'poblacion': 'Personas con sobrepeso y obesidad',
                'actividades': [
                    'Clases de ejercicio grupal',
                    'Caminatas comunitarias',
                    'Talleres de nutrición',
                    'Seguimiento de peso y medidas'
                ],
                'duracion': '6 meses',
                'frecuencia': 'Semanal',
                'recursos': 'Instructor de actividad física, nutricionista, balanzas',
                'indicadores': 'Pérdida de peso, mejora en condición física, adherencia'
            }
        ],
        'hacinamiento': [
            {
                'nombre': 'Programa de Mejora Habitacional',
                'tipo': 'Comunitaria',
                'objetivo': 'Mejorar las condiciones de vivienda y hacinamiento',
                'poblacion': 'Familias en situación de hacinamiento',
                'actividades': [
                    'Asesoría en mejoras habitacionales',
                    'Gestión de subsidios habitacionales',
                    'Talleres de organización del espacio',
                    'Apoyo en trámites municipales'
                ],
                'duracion': '12 meses',
                'frecuencia': 'Mensual',
                'recursos': 'Asistente social, arquitecto, gestor municipal',
                'indicadores': 'Reducción del hacinamiento, mejoras habitacionales'
            }
        ],
        'violencia_intrafamiliar': [
            {
                'nombre': 'Programa de Prevención de Violencia Intrafamiliar',
                'tipo': 'Preventiva',
                'objetivo': 'Prevenir y detectar casos de violencia intrafamiliar',
                'poblacion': 'Familias en riesgo de violencia',
                'actividades': [
                    'Talleres de resolución pacífica de conflictos',
                    'Educación en derechos humanos',
                    'Detección temprana de violencia',
                    'Derivación a servicios especializados'
                ],
                'duracion': '6 meses',
                'frecuencia': 'Quincenal',
                'recursos': 'Psicólogo, trabajador social, abogado',
                'indicadores': 'Reducción de casos de violencia, derivaciones exitosas'
            }
        ],
        'consumo_drogas': [
            {
                'nombre': 'Programa de Prevención de Consumo de Drogas',
                'tipo': 'Preventiva',
                'objetivo': 'Prevenir el consumo de drogas y apoyar la rehabilitación',
                'poblacion': 'Adolescentes y jóvenes en riesgo',
                'actividades': [
                    'Talleres de prevención en colegios',
                    'Actividades deportivas y recreativas',
                    'Apoyo a familias afectadas',
                    'Derivación a centros de rehabilitación'
                ],
                'duracion': '12 meses',
                'frecuencia': 'Semanal',
                'recursos': 'Psicólogo, monitor deportivo, educador',
                'indicadores': 'Reducción del consumo, participación en actividades'
            }
        ],
        'embarazo_adolescente': [
            {
                'nombre': 'Programa de Salud Sexual y Reproductiva',
                'tipo': 'Preventiva',
                'objetivo': 'Prevenir embarazos adolescentes y promover salud sexual',
                'poblacion': 'Adolescentes y jóvenes',
                'actividades': [
                    'Educación sexual integral',
                    'Talleres de proyecto de vida',
                    'Acceso a métodos anticonceptivos',
                    'Apoyo a madres adolescentes'
                ],
                'duracion': '12 meses',
                'frecuencia': 'Mensual',
                'recursos': 'Matrona, psicólogo, educador en salud',
                'indicadores': 'Reducción de embarazos adolescentes, uso de anticonceptivos'
            }
        ],
        'desempleo': [
            {
                'nombre': 'Programa de Inserción Laboral',
                'tipo': 'Comunitaria',
                'objetivo': 'Mejorar las oportunidades laborales de la comunidad',
                'poblacion': 'Personas desempleadas',
                'actividades': [
                    'Capacitación laboral',
                    'Talleres de emprendimiento',
                    'Gestión de empleos',
                    'Apoyo en currículum vitae'
                ],
                'duracion': '6 meses',
                'frecuencia': 'Semanal',
                'recursos': 'Orientador laboral, capacitador, gestor de empleos',
                'indicadores': 'Inserción laboral, creación de emprendimientos'
            }
        ],
        'baja_escolaridad': [
            {
                'nombre': 'Programa de Alfabetización y Educación',
                'tipo': 'Promocional',
                'objetivo': 'Mejorar los niveles de educación de la comunidad',
                'poblacion': 'Personas con baja escolaridad',
                'actividades': [
                    'Clases de alfabetización',
                    'Apoyo escolar para niños',
                    'Talleres de computación',
                    'Preparación para exámenes libres'
                ],
                'duracion': '12 meses',
                'frecuencia': 'Semanal',
                'recursos': 'Profesor, computadores, material educativo',
                'indicadores': 'Mejora en niveles de lectura, aprobación de exámenes'
            }
        ],
        'acceso_salud': [
            {
                'nombre': 'Programa de Acceso a Servicios de Salud',
                'tipo': 'Comunitaria',
                'objetivo': 'Mejorar el acceso a servicios de salud de la comunidad',
                'poblacion': 'Personas con dificultades de acceso',
                'actividades': [
                    'Transporte comunitario a centros de salud',
                    'Atención domiciliaria',
                    'Gestión de horas médicas',
                    'Educación en derechos de salud'
                ],
                'duracion': '12 meses',
                'frecuencia': 'Mensual',
                'recursos': 'Movilización, personal de salud, gestor',
                'indicadores': 'Mejora en acceso, satisfacción usuaria'
            }
        ]
    }
    
    # Generar sugerencias basadas en problemas identificados
    for problema in diagnostico['problemas_prioritarios']:
        if problema['problema'] in intervenciones_por_problema:
            sugerencias.extend(intervenciones_por_problema[problema['problema']])
    
    # Agregar sugerencias generales basadas en fortalezas y recursos
    if diagnostico['fortalezas_comunitarias']:
        sugerencias.append({
            'nombre': 'Programa de Fortalecimiento Comunitario',
            'tipo': 'Promocional',
            'objetivo': 'Potenciar las fortalezas identificadas en la comunidad',
            'poblacion': 'Toda la comunidad',
            'actividades': [
                'Talleres de liderazgo comunitario',
                'Organización de eventos comunitarios',
                'Fortalecimiento de redes sociales',
                'Desarrollo de proyectos comunitarios'
            ],
            'duracion': '6 meses',
            'frecuencia': 'Mensual',
            'recursos': 'Facilitador comunitario, espacio de reunión',
            'indicadores': 'Participación comunitaria, desarrollo de proyectos'
        })
    
    return sugerencias

def generar_cronograma_inteligente(sugerencias):
    """
    Genera un cronograma inteligente para las intervenciones sugeridas
    """
    cronograma = []
    fecha_actual = datetime.now()
    
    # Priorizar intervenciones
    prioridades = {
        'Preventiva': 1,
        'Curativa': 2,
        'Promocional': 3,
        'Rehabilitadora': 4,
        'Comunitaria': 5
    }
    
    # Ordenar sugerencias por prioridad
    sugerencias_ordenadas = sorted(sugerencias, key=lambda x: prioridades.get(x['tipo'], 6))
    
    for i, sugerencia in enumerate(sugerencias_ordenadas):
        # Calcular fechas basadas en prioridad y duración
        if i == 0:
            fecha_inicio = fecha_actual + timedelta(days=30)  # Comenzar en 1 mes
        else:
            fecha_inicio = fecha_actual + timedelta(days=30 + (i * 60))  # Espaciado de 2 meses
        
        # Calcular fecha fin basada en duración
        duracion_meses = int(sugerencia['duracion'].split()[0])
        fecha_fin = fecha_inicio + timedelta(days=duracion_meses * 30)
        
        # Asignar prioridad
        if sugerencia['tipo'] == 'Preventiva':
            prioridad = 'Alta'
        elif sugerencia['tipo'] in ['Curativa', 'Promocional']:
            prioridad = 'Media'
        else:
            prioridad = 'Baja'
        
        cronograma.append({
            'nombre': sugerencia['nombre'],
            'tipo': sugerencia['tipo'],
            'objetivo': sugerencia['objetivo'],
            'poblacion': sugerencia['poblacion'],
            'prioridad': prioridad,
            'fecha_inicio': fecha_inicio.strftime('%Y-%m-%d'),
            'fecha_fin': fecha_fin.strftime('%Y-%m-%d'),
            'frecuencia': sugerencia['frecuencia'],
            'responsable': 'Equipo de Salud Familiar',
            'equipo': 'Médico, TENS, Matrona, Psicólogo',
            'recursos': sugerencia['recursos'],
            'presupuesto': random.randint(500000, 2000000),  # Presupuesto estimado
            'indicadores': sugerencia['indicadores'],
            'actividades': sugerencia['actividades']
        })
    
    return cronograma

def generar_recomendaciones_personalizadas():
    """
    Genera recomendaciones personalizadas basadas en el análisis de datos
    """
    diagnostico = analizar_datos_comunidad()
    sugerencias = generar_sugerencias_intervenciones(diagnostico)
    cronograma = generar_cronograma_inteligente(sugerencias)
    
    return {
        'diagnostico': diagnostico,
        'sugerencias': sugerencias,
        'cronograma': cronograma
    } 