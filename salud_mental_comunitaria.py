import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json

def mostrar_salud_mental_comunitaria():
    """
    Módulo de Salud Mental Comunitaria adaptado para profesionales no médicos
    Enfoque en diagnóstico comunitario y trabajo territorial
    """
    
    st.title("🧠 Salud Mental Comunitaria")
    st.markdown("### Diagnóstico e Intervención Comunitaria - Enfoque No Médico")
    
    # Inicializar session state
    if 'salud_mental_comunitaria' not in st.session_state:
        st.session_state.salud_mental_comunitaria = {
            'diagnosticos_comunitarios': [],
            'intervenciones_grupales': [],
            'redes_apoyo': [],
            'indicadores_comunitarios': [],
            'seguimientos': []
        }
    
    # Pestañas principales
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "🔍 Diagnóstico Comunitario", 
        "👥 Intervenciones Grupales",
        "🤝 Redes de Apoyo", 
        "📊 Indicadores",
        "📋 Seguimiento",
        "📄 Reportes"
    ])
    
    with tab1:
        mostrar_diagnostico_comunitario()
    
    with tab2:
        mostrar_intervenciones_grupales()
    
    with tab3:
        mostrar_redes_apoyo()
    
    with tab4:
        mostrar_indicadores_comunitarios()
    
    with tab5:
        mostrar_seguimiento_comunitario()
    
    with tab6:
        mostrar_reportes_salud_mental()

def mostrar_diagnostico_comunitario():
    """Diagnóstico comunitario de salud mental"""
    
    st.header("🔍 Diagnóstico Comunitario de Salud Mental")
    st.markdown("**Enfoque para profesionales no médicos**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📋 Información del Diagnóstico")
        
        nombre_comunidad = st.text_input("Nombre de la Comunidad/Sector:", key="sm_nombre_comunidad")
        fecha_diagnostico = st.date_input("Fecha del Diagnóstico:", key="sm_fecha_diagnostico")
        
        tipo_diagnostico = st.selectbox(
            "Tipo de Diagnóstico:",
            ["Participativo", "Observacional", "Entrevistas Grupales", "Mapeo Comunitario"],
            key="sm_tipo_diagnostico"
        )
        
        profesional_responsable = st.text_input("Profesional Responsable:", key="sm_profesional")
        
    with col2:
        st.subheader("🎯 Factores de Riesgo Comunitario")
        
        factores_riesgo = st.multiselect(
            "Factores de Riesgo Identificados:",
            [
                "Aislamiento social", "Pobreza", "Violencia intrafamiliar",
                "Consumo de alcohol/drogas", "Desempleo", "Migración",
                "Discriminación", "Falta de acceso a servicios",
                "Estigma hacia salud mental", "Catástrofes naturales",
                "Conflictos comunitarios", "Falta de espacios recreativos"
            ],
            key="sm_factores_riesgo"
        )
        
        nivel_riesgo = st.selectbox(
            "Nivel de Riesgo Comunitario:",
            ["Bajo", "Medio", "Alto", "Crítico"],
            key="sm_nivel_riesgo"
        )
    
    st.subheader("📝 Hallazgos Principales")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Problemas Identificados:**")
        problemas = st.text_area(
            "Describa los principales problemas de salud mental identificados:",
            placeholder="Ej: Aislamiento en adultos mayores, estrés en cuidadores...",
            key="sm_problemas"
        )
        
        recursos_comunidad = st.text_area(
            "Recursos y Fortalezas de la Comunidad:",
            placeholder="Ej: Líderes comunitarios, espacios de reunión...",
            key="sm_recursos"
        )
    
    with col2:
        st.markdown("**Necesidades Identificadas:**")
        necesidades = st.text_area(
            "Principales necesidades de salud mental:",
            placeholder="Ej: Talleres de manejo del estrés, grupos de apoyo...",
            key="sm_necesidades"
        )
        
        barreras_acceso = st.text_area(
            "Barreras para el acceso a salud mental:",
            placeholder="Ej: Estigma, falta de transporte, horarios...",
            key="sm_barreras"
        )
    
    st.subheader("👥 Participación Comunitaria")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        participantes_hombres = st.number_input("Participantes Hombres:", min_value=0, key="sm_participantes_h")
        participantes_mujeres = st.number_input("Participantes Mujeres:", min_value=0, key="sm_participantes_m")
    
    with col2:
        participantes_ninos = st.number_input("Participantes Niños/Adolescentes:", min_value=0, key="sm_participantes_n")
        participantes_adultos_mayores = st.number_input("Participantes Adultos Mayores:", min_value=0, key="sm_participantes_am")
    
    with col3:
        lideres_comunitarios = st.number_input("Líderes Comunitarios Participantes:", min_value=0, key="sm_lideres")
        organizaciones_participantes = st.number_input("Organizaciones Participantes:", min_value=0, key="sm_organizaciones")
    
    if st.button("💾 Guardar Diagnóstico Comunitario", key="sm_guardar_diagnostico"):
        if nombre_comunidad and problemas:
            diagnostico = {
                'id': len(st.session_state.salud_mental_comunitaria['diagnosticos_comunitarios']) + 1,
                'nombre_comunidad': nombre_comunidad,
                'fecha': str(fecha_diagnostico),
                'tipo_diagnostico': tipo_diagnostico,
                'profesional': profesional_responsable,
                'factores_riesgo': factores_riesgo,
                'nivel_riesgo': nivel_riesgo,
                'problemas': problemas,
                'recursos': recursos_comunidad,
                'necesidades': necesidades,
                'barreras': barreras_acceso,
                'participantes': {
                    'hombres': participantes_hombres,
                    'mujeres': participantes_mujeres,
                    'ninos': participantes_ninos,
                    'adultos_mayores': participantes_adultos_mayores,
                    'lideres': lideres_comunitarios,
                    'organizaciones': organizaciones_participantes
                }
            }
            
            st.session_state.salud_mental_comunitaria['diagnosticos_comunitarios'].append(diagnostico)
            st.success("✅ Diagnóstico comunitario guardado exitosamente")
            st.rerun()
        else:
            st.error("❌ Complete los campos obligatorios")

def mostrar_intervenciones_grupales():
    """Intervenciones grupales de salud mental"""
    
    st.header("👥 Intervenciones Grupales de Salud Mental")
    st.markdown("**Actividades grupales para promoción y prevención**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📋 Información de la Intervención")
        
        nombre_intervencion = st.text_input("Nombre de la Intervención:", key="sm_nombre_intervencion")
        tipo_intervencion = st.selectbox(
            "Tipo de Intervención:",
            [
                "Taller de manejo del estrés", "Grupo de apoyo mutuo",
                "Actividades recreativas", "Educación en salud mental",
                "Arte terapia", "Musicoterapia", "Ejercicio físico",
                "Meditación/Mindfulness", "Habilidades sociales",
                "Prevención de violencia", "Otro"
            ],
            key="sm_tipo_intervencion"
        )
        
        fecha_inicio = st.date_input("Fecha de Inicio:", key="sm_fecha_inicio")
        fecha_fin = st.date_input("Fecha de Finalización:", key="sm_fecha_fin")
        
        frecuencia = st.selectbox(
            "Frecuencia:",
            ["Semanal", "Quincenal", "Mensual", "Única vez"],
            key="sm_frecuencia"
        )
        
        duracion_sesion = st.number_input("Duración por Sesión (minutos):", min_value=30, key="sm_duracion")
        
    with col2:
        st.subheader("👥 Participantes")
        
        grupo_objetivo = st.multiselect(
            "Grupo Objetivo:",
            [
                "Adultos mayores", "Mujeres", "Hombres", "Adolescentes",
                "Niños", "Cuidadores", "Migrantes", "Personas con discapacidad",
                "Familias", "Líderes comunitarios", "Otro"
            ],
            key="sm_grupo_objetivo"
        )
        
        participantes_esperados = st.number_input("Participantes Esperados:", min_value=1, key="sm_participantes_esperados")
        participantes_reales = st.number_input("Participantes Reales:", min_value=0, key="sm_participantes_reales")
        
        facilitadores = st.text_input("Facilitadores:", key="sm_facilitadores")
        
        lugar = st.text_input("Lugar de Realización:", key="sm_lugar")
    
    st.subheader("📝 Contenido y Metodología")
    
    objetivos = st.text_area(
        "Objetivos de la Intervención:",
        placeholder="Ej: Reducir el estrés, mejorar la cohesión social...",
        key="sm_objetivos"
    )
    
    metodologia = st.text_area(
        "Metodología Utilizada:",
        placeholder="Ej: Participativa, experiencial, teórico-práctica...",
        key="sm_metodologia"
    )
    
    materiales = st.text_area(
        "Materiales Utilizados:",
        placeholder="Ej: Papel, lápices, música, ejercicios...",
        key="sm_materiales"
    )
    
    st.subheader("📊 Evaluación")
    
    col1, col2 = st.columns(2)
    
    with col1:
        satisfaccion = st.slider("Nivel de Satisfacción (1-10):", 1, 10, 5, key="sm_satisfaccion")
        participacion = st.slider("Nivel de Participación (1-10):", 1, 10, 5, key="sm_participacion")
    
    with col2:
        cumplimiento_objetivos = st.slider("Cumplimiento de Objetivos (1-10):", 1, 10, 5, key="sm_cumplimiento")
        continuidad = st.checkbox("¿Se continuará la intervención?", key="sm_continuidad")
    
    observaciones = st.text_area(
        "Observaciones y Recomendaciones:",
        key="sm_observaciones"
    )
    
    if st.button("💾 Guardar Intervención Grupal", key="sm_guardar_intervencion"):
        if nombre_intervencion and objetivos:
            intervencion = {
                'id': len(st.session_state.salud_mental_comunitaria['intervenciones_grupales']) + 1,
                'nombre': nombre_intervencion,
                'tipo': tipo_intervencion,
                'fecha_inicio': str(fecha_inicio),
                'fecha_fin': str(fecha_fin),
                'frecuencia': frecuencia,
                'duracion': duracion_sesion,
                'grupo_objetivo': grupo_objetivo,
                'participantes_esperados': participantes_esperados,
                'participantes_reales': participantes_reales,
                'facilitadores': facilitadores,
                'lugar': lugar,
                'objetivos': objetivos,
                'metodologia': metodologia,
                'materiales': materiales,
                'satisfaccion': satisfaccion,
                'participacion': participacion,
                'cumplimiento': cumplimiento_objetivos,
                'continuidad': continuidad,
                'observaciones': observaciones
            }
            
            st.session_state.salud_mental_comunitaria['intervenciones_grupales'].append(intervencion)
            st.success("✅ Intervención grupal guardada exitosamente")
            st.rerun()
        else:
            st.error("❌ Complete los campos obligatorios")

def mostrar_redes_apoyo():
    """Redes de apoyo comunitario"""
    
    st.header("🤝 Redes de Apoyo Comunitario")
    st.markdown("**Mapeo y fortalecimiento de redes de apoyo**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏢 Organizaciones de Apoyo")
        
        nombre_organizacion = st.text_input("Nombre de la Organización:", key="sm_nombre_org")
        tipo_organizacion = st.selectbox(
            "Tipo de Organización:",
            [
                "Centro de salud", "Municipalidad", "ONG", "Iglesia",
                "Junta de vecinos", "Centro comunitario", "Escuela",
                "Centro de adultos mayores", "Organización deportiva",
                "Grupo de autoayuda", "Otro"
            ],
            key="sm_tipo_org"
        )
        
        contacto = st.text_input("Persona de Contacto:", key="sm_contacto")
        telefono = st.text_input("Teléfono:", key="sm_telefono")
        email = st.text_input("Email:", key="sm_email")
        
    with col2:
        st.subheader("📍 Ubicación y Servicios")
        
        direccion = st.text_input("Dirección:", key="sm_direccion")
        horarios = st.text_input("Horarios de Atención:", key="sm_horarios")
        
        servicios = st.multiselect(
            "Servicios Ofrecidos:",
            [
                "Atención psicológica", "Grupos de apoyo", "Actividades recreativas",
                "Educación", "Transporte", "Alimentación", "Vivienda",
                "Empleo", "Legal", "Otro"
            ],
            key="sm_servicios"
        )
        
        nivel_coordinacion = st.selectbox(
            "Nivel de Coordinación:",
            ["Excelente", "Bueno", "Regular", "Pobre", "Sin coordinación"],
            key="sm_coordinacion"
        )
    
    st.subheader("📝 Información Adicional")
    
    col1, col2 = st.columns(2)
    
    with col1:
        fortalezas = st.text_area(
            "Fortalezas de la Organización:",
            placeholder="Ej: Buena ubicación, personal comprometido...",
            key="sm_fortalezas"
        )
        
        necesidades_org = st.text_area(
            "Necesidades de la Organización:",
            placeholder="Ej: Capacitación, recursos, coordinación...",
            key="sm_necesidades_org"
        )
    
    with col2:
        actividades_conjuntas = st.text_area(
            "Actividades Conjuntas Realizadas:",
            placeholder="Ej: Talleres, campañas, eventos...",
            key="sm_actividades_conjuntas"
        )
        
        plan_futuro = st.text_area(
            "Plan de Trabajo Futuro:",
            placeholder="Ej: Proyectos, actividades planificadas...",
            key="sm_plan_futuro"
        )
    
    if st.button("💾 Guardar Red de Apoyo", key="sm_guardar_red"):
        if nombre_organizacion and tipo_organizacion:
            red_apoyo = {
                'id': len(st.session_state.salud_mental_comunitaria['redes_apoyo']) + 1,
                'nombre': nombre_organizacion,
                'tipo': tipo_organizacion,
                'contacto': contacto,
                'telefono': telefono,
                'email': email,
                'direccion': direccion,
                'horarios': horarios,
                'servicios': servicios,
                'coordinacion': nivel_coordinacion,
                'fortalezas': fortalezas,
                'necesidades': necesidades_org,
                'actividades_conjuntas': actividades_conjuntas,
                'plan_futuro': plan_futuro
            }
            
            st.session_state.salud_mental_comunitaria['redes_apoyo'].append(red_apoyo)
            st.success("✅ Red de apoyo guardada exitosamente")
            st.rerun()
        else:
            st.error("❌ Complete los campos obligatorios")

def mostrar_indicadores_comunitarios():
    """Indicadores comunitarios de salud mental"""
    
    st.header("📊 Indicadores Comunitarios de Salud Mental")
    st.markdown("**Seguimiento de indicadores poblacionales**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Indicadores de Proceso")
        
        fecha_indicador = st.date_input("Fecha de Medición:", key="sm_fecha_indicador")
        
        # Indicadores de participación
        st.markdown("**Participación Comunitaria:**")
        personas_contactadas = st.number_input("Personas Contactadas:", min_value=0, key="sm_contactadas")
        personas_participantes = st.number_input("Personas Participantes:", min_value=0, key="sm_participantes")
        
        # Indicadores de intervención
        st.markdown("**Intervenciones Realizadas:**")
        talleres_realizados = st.number_input("Talleres Realizados:", min_value=0, key="sm_talleres")
        sesiones_grupo = st.number_input("Sesiones de Grupo:", min_value=0, key="sm_sesiones")
        visitas_domicilio = st.number_input("Visitas Domiciliarias:", min_value=0, key="sm_visitas")
        
    with col2:
        st.subheader("🎯 Indicadores de Resultado")
        
        # Indicadores de satisfacción
        st.markdown("**Satisfacción:**")
        satisfaccion_general = st.slider("Satisfacción General (1-10):", 1, 10, 5, key="sm_satisfaccion_gen")
        recomendaria_servicio = st.slider("Recomendaría el Servicio (1-10):", 1, 10, 5, key="sm_recomendaria")
        
        # Indicadores de impacto
        st.markdown("**Impacto Percibido:**")
        mejora_bienestar = st.slider("Mejora en Bienestar (1-10):", 1, 10, 5, key="sm_bienestar")
        reduccion_estigma = st.slider("Reducción de Estigma (1-10):", 1, 10, 5, key="sm_estigma")
    
    st.subheader("📋 Indicadores Específicos")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Indicadores de Acceso:**")
        tiempo_espera = st.number_input("Tiempo de Espera Promedio (días):", min_value=0, key="sm_tiempo_espera")
        distancia_centro = st.number_input("Distancia al Centro (km):", min_value=0.0, key="sm_distancia")
        barreras_acceso = st.multiselect(
            "Barreras de Acceso Identificadas:",
            ["Transporte", "Horarios", "Estigma", "Costo", "Idioma", "Otro"],
            key="sm_barreras_indicador"
        )
    
    with col2:
        st.markdown("**Indicadores de Calidad:**")
        continuidad_atencion = st.slider("Continuidad de Atención (1-10):", 1, 10, 5, key="sm_continuidad_atencion")
        coordinacion_red = st.slider("Coordinación con Red (1-10):", 1, 10, 5, key="sm_coordinacion_red")
        resolucion_problemas = st.slider("Resolución de Problemas (1-10):", 1, 10, 5, key="sm_resolucion")
    
    observaciones_indicadores = st.text_area(
        "Observaciones sobre Indicadores:",
        key="sm_obs_indicadores"
    )
    
    if st.button("💾 Guardar Indicadores", key="sm_guardar_indicadores"):
        indicador = {
            'id': len(st.session_state.salud_mental_comunitaria['indicadores_comunitarios']) + 1,
            'fecha': str(fecha_indicador),
            'participacion': {
                'contactadas': personas_contactadas,
                'participantes': personas_participantes
            },
            'intervenciones': {
                'talleres': talleres_realizados,
                'sesiones': sesiones_grupo,
                'visitas': visitas_domicilio
            },
            'satisfaccion': {
                'general': satisfaccion_general,
                'recomendaria': recomendaria_servicio
            },
            'impacto': {
                'bienestar': mejora_bienestar,
                'estigma': reduccion_estigma
            },
            'acceso': {
                'tiempo_espera': tiempo_espera,
                'distancia': distancia_centro,
                'barreras': barreras_acceso
            },
            'calidad': {
                'continuidad': continuidad_atencion,
                'coordinacion': coordinacion_red,
                'resolucion': resolucion_problemas
            },
            'observaciones': observaciones_indicadores
        }
        
        st.session_state.salud_mental_comunitaria['indicadores_comunitarios'].append(indicador)
        st.success("✅ Indicadores guardados exitosamente")
        st.rerun()

def mostrar_seguimiento_comunitario():
    """Seguimiento comunitario de salud mental"""
    
    st.header("📋 Seguimiento Comunitario")
    st.markdown("**Seguimiento de casos y situaciones comunitarias**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📝 Información del Seguimiento")
        
        fecha_seguimiento = st.date_input("Fecha de Seguimiento:", key="sm_fecha_seg")
        tipo_seguimiento = st.selectbox(
            "Tipo de Seguimiento:",
            ["Individual", "Familiar", "Grupal", "Comunitario", "Institucional"],
            key="sm_tipo_seg"
        )
        
        profesional_seguimiento = st.text_input("Profesional Responsable:", key="sm_prof_seg")
        
        situacion = st.text_area(
            "Situación o Caso a Seguir:",
            placeholder="Ej: Grupo de adultos mayores con depresión...",
            key="sm_situacion"
        )
    
    with col2:
        st.subheader("📊 Estado Actual")
        
        estado_actual = st.selectbox(
            "Estado Actual:",
            ["Mejorado", "Estable", "Empeorado", "Sin cambios", "Nuevo"],
            key="sm_estado_actual"
        )
        
        nivel_urgencia = st.selectbox(
            "Nivel de Urgencia:",
            ["Bajo", "Medio", "Alto", "Crítico"],
            key="sm_urgencia"
        )
        
        intervenciones_realizadas = st.multiselect(
            "Intervenciones Realizadas:",
            [
                "Acompañamiento", "Derivación", "Coordinación con red",
                "Educación", "Apoyo emocional", "Activación de redes",
                "Gestión de recursos", "Otro"
            ],
            key="sm_intervenciones_seg"
        )
    
    st.subheader("📝 Evaluación del Seguimiento")
    
    col1, col2 = st.columns(2)
    
    with col1:
        progreso = st.slider("Progreso Observado (1-10):", 1, 10, 5, key="sm_progreso")
        adherencia = st.slider("Adherencia a Intervenciones (1-10):", 1, 10, 5, key="sm_adherencia")
        
        factores_facilitadores = st.text_area(
            "Factores Facilitadores:",
            placeholder="Ej: Apoyo familiar, recursos disponibles...",
            key="sm_facilitadores_seg"
        )
    
    with col2:
        barreras_seguimiento = st.text_area(
            "Barreras Identificadas:",
            placeholder="Ej: Falta de transporte, estigma...",
            key="sm_barreras_seg"
        )
        
        plan_accion = st.text_area(
            "Plan de Acción:",
            placeholder="Ej: Continuar acompañamiento, coordinar con...",
            key="sm_plan_accion"
        )
    
    proximo_seguimiento = st.date_input("Próximo Seguimiento:", key="sm_proximo_seg")
    
    observaciones_seguimiento = st.text_area(
        "Observaciones Generales:",
        key="sm_obs_seguimiento"
    )
    
    if st.button("💾 Guardar Seguimiento", key="sm_guardar_seguimiento"):
        if situacion and profesional_seguimiento:
            seguimiento = {
                'id': len(st.session_state.salud_mental_comunitaria['seguimientos']) + 1,
                'fecha': str(fecha_seguimiento),
                'tipo': tipo_seguimiento,
                'profesional': profesional_seguimiento,
                'situacion': situacion,
                'estado': estado_actual,
                'urgencia': nivel_urgencia,
                'intervenciones': intervenciones_realizadas,
                'progreso': progreso,
                'adherencia': adherencia,
                'facilitadores': factores_facilitadores,
                'barreras': barreras_seguimiento,
                'plan_accion': plan_accion,
                'proximo_seguimiento': str(proximo_seguimiento),
                'observaciones': observaciones_seguimiento
            }
            
            st.session_state.salud_mental_comunitaria['seguimientos'].append(seguimiento)
            st.success("✅ Seguimiento guardado exitosamente")
            st.rerun()
        else:
            st.error("❌ Complete los campos obligatorios")

def mostrar_reportes_salud_mental():
    """Reportes de salud mental comunitaria"""
    
    st.header("📄 Reportes de Salud Mental Comunitaria")
    
    # Métricas generales
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_diagnosticos = len(st.session_state.salud_mental_comunitaria['diagnosticos_comunitarios'])
        st.metric("Diagnósticos Comunitarios", total_diagnosticos)
    
    with col2:
        total_intervenciones = len(st.session_state.salud_mental_comunitaria['intervenciones_grupales'])
        st.metric("Intervenciones Grupales", total_intervenciones)
    
    with col3:
        total_redes = len(st.session_state.salud_mental_comunitaria['redes_apoyo'])
        st.metric("Redes de Apoyo", total_redes)
    
    with col4:
        total_seguimientos = len(st.session_state.salud_mental_comunitaria['seguimientos'])
        st.metric("Seguimientos", total_seguimientos)
    
    # Gráficos
    col1, col2 = st.columns(2)
    
    with col1:
        if st.session_state.salud_mental_comunitaria['diagnosticos_comunitarios']:
            st.subheader("📊 Niveles de Riesgo por Comunidad")
            
            df_riesgo = pd.DataFrame([
                {
                    'Comunidad': d['nombre_comunidad'],
                    'Nivel de Riesgo': d['nivel_riesgo']
                }
                for d in st.session_state.salud_mental_comunitaria['diagnosticos_comunitarios']
            ])
            
            fig_riesgo = px.bar(
                df_riesgo.groupby('Nivel de Riesgo').size().reset_index(name='Cantidad'),
                x='Nivel de Riesgo',
                y='Cantidad',
                title="Distribución de Niveles de Riesgo"
            )
            st.plotly_chart(fig_riesgo, use_container_width=True)
    
    with col2:
        if st.session_state.salud_mental_comunitaria['intervenciones_grupales']:
            st.subheader("👥 Tipos de Intervenciones")
            
            df_intervenciones = pd.DataFrame([
                {
                    'Tipo': i['tipo'],
                    'Participantes': i['participantes_reales']
                }
                for i in st.session_state.salud_mental_comunitaria['intervenciones_grupales']
            ])
            
            fig_intervenciones = px.pie(
                df_intervenciones.groupby('Tipo')['Participantes'].sum().reset_index(),
                values='Participantes',
                names='Tipo',
                title="Participantes por Tipo de Intervención"
            )
            st.plotly_chart(fig_intervenciones, use_container_width=True)
    
    # Tabla de datos
    if st.session_state.salud_mental_comunitaria['diagnosticos_comunitarios']:
        st.subheader("📋 Resumen de Diagnósticos Comunitarios")
        
        df_diagnosticos = pd.DataFrame([
            {
                'Comunidad': d['nombre_comunidad'],
                'Fecha': d['fecha'],
                'Tipo': d['tipo_diagnostico'],
                'Nivel Riesgo': d['nivel_riesgo'],
                'Profesional': d['profesional']
            }
            for d in st.session_state.salud_mental_comunitaria['diagnosticos_comunitarios']
        ])
        
        st.dataframe(df_diagnosticos, use_container_width=True)
    
    # Exportar datos
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📊 Exportar Datos a CSV", key="sm_exportar_csv"):
            if st.session_state.salud_mental_comunitaria['diagnosticos_comunitarios']:
                df_export = pd.DataFrame(st.session_state.salud_mental_comunitaria['diagnosticos_comunitarios'])
                csv = df_export.to_csv(index=False)
                st.download_button(
                    label="⬇️ Descargar CSV",
                    data=csv,
                    file_name="salud_mental_comunitaria.csv",
                    mime="text/csv"
                )
    
    with col2:
        if st.button("📄 Generar Reporte Completo", key="sm_generar_reporte"):
            st.info("📋 Reporte generado en la consola")
            # Aquí se podría generar un reporte más detallado
            st.json(st.session_state.salud_mental_comunitaria) 