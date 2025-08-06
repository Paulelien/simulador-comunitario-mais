import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json

def mostrar_gestion_clinica_aps():
    """
    Módulo de Gestión Clínica en APS adaptado para profesionales TENS
    Enfoque en control de pacientes crónicos, educación en salud y coordinación
    """
    
    st.title("🏥 Gestión Clínica en APS")
    st.markdown("### Control de Pacientes Crónicos y Educación en Salud - Enfoque TENS")
    
    # Inicializar session state
    if 'gestion_clinica_aps' not in st.session_state:
        st.session_state.gestion_clinica_aps = {
            'pacientes_cronicos': [],
            'controles_realizados': [],
            'educacion_salud': [],
            'seguimientos_tratamiento': [],
            'derivaciones': [],
            'indicadores_clinicos': []
        }
    
    # Pestañas principales
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "👥 Pacientes Crónicos", 
        "📋 Controles Clínicos",
        "📚 Educación en Salud", 
        "💊 Seguimiento Tratamientos",
        "🔄 Derivaciones",
        "📊 Indicadores"
    ])
    
    with tab1:
        mostrar_pacientes_cronicos()
    
    with tab2:
        mostrar_controles_clinicos()
    
    with tab3:
        mostrar_educacion_salud()
    
    with tab4:
        mostrar_seguimiento_tratamientos()
    
    with tab5:
        mostrar_derivaciones()
    
    with tab6:
        mostrar_indicadores_clinicos()

def mostrar_pacientes_cronicos():
    """Registro y seguimiento de pacientes crónicos"""
    
    st.header("👥 Registro de Pacientes Crónicos")
    st.markdown("**Control de pacientes con enfermedades crónicas**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📋 Información del Paciente")
        
        rut_paciente = st.text_input("RUT del Paciente:", key="gc_rut")
        nombre_paciente = st.text_input("Nombre Completo:", key="gc_nombre")
        fecha_nacimiento = st.date_input("Fecha de Nacimiento:", key="gc_fecha_nac")
        
        sexo = st.selectbox(
            "Sexo:",
            ["Masculino", "Femenino"],
            key="gc_sexo"
        )
        
        telefono = st.text_input("Teléfono:", key="gc_telefono")
        direccion = st.text_input("Dirección:", key="gc_direccion")
        
    with col2:
        st.subheader("🏥 Información Clínica")
        
        enfermedades_cronicas = st.multiselect(
            "Enfermedades Crónicas:",
            [
                "Hipertensión Arterial", "Diabetes Mellitus", "Obesidad",
                "Dislipidemia", "EPOC", "Asma", "Artritis",
                "Depresión", "Ansiedad", "Insuficiencia Cardíaca",
                "Enfermedad Renal Crónica", "Cáncer", "Otra"
            ],
            key="gc_enfermedades"
        )
        
        nivel_riesgo = st.selectbox(
            "Nivel de Riesgo:",
            ["Bajo", "Medio", "Alto", "Muy Alto"],
            key="gc_nivel_riesgo"
        )
        
        estado_funcional = st.selectbox(
            "Estado Funcional:",
            ["Independiente", "Dependencia Leve", "Dependencia Moderada", "Dependencia Severa"],
            key="gc_estado_funcional"
        )
        
        cuidador_principal = st.text_input("Cuidador Principal:", key="gc_cuidador")
    
    st.subheader("📝 Información Adicional")
    
    col1, col2 = st.columns(2)
    
    with col1:
        medicamentos_actuales = st.text_area(
            "Medicamentos Actuales:",
            placeholder="Lista de medicamentos que toma regularmente...",
            key="gc_medicamentos"
        )
        
        alergias = st.text_area(
            "Alergias Conocidas:",
            placeholder="Medicamentos, alimentos, otros...",
            key="gc_alergias"
        )
    
    with col2:
        antecedentes_familiares = st.text_area(
            "Antecedentes Familiares Relevantes:",
            placeholder="Enfermedades crónicas en familiares...",
            key="gc_antecedentes"
        )
        
        observaciones = st.text_area(
            "Observaciones Importantes:",
            placeholder="Información adicional relevante...",
            key="gc_observaciones"
        )
    
    if st.button("💾 Registrar Paciente Crónico", key="gc_guardar_paciente"):
        if rut_paciente and nombre_paciente and enfermedades_cronicas:
            paciente = {
                'id': len(st.session_state.gestion_clinica_aps['pacientes_cronicos']) + 1,
                'rut': rut_paciente,
                'nombre': nombre_paciente,
                'fecha_nacimiento': str(fecha_nacimiento),
                'sexo': sexo,
                'telefono': telefono,
                'direccion': direccion,
                'enfermedades': enfermedades_cronicas,
                'nivel_riesgo': nivel_riesgo,
                'estado_funcional': estado_funcional,
                'cuidador': cuidador_principal,
                'medicamentos': medicamentos_actuales,
                'alergias': alergias,
                'antecedentes': antecedentes_familiares,
                'observaciones': observaciones,
                'fecha_registro': str(datetime.now().date())
            }
            
            st.session_state.gestion_clinica_aps['pacientes_cronicos'].append(paciente)
            st.success("✅ Paciente crónico registrado exitosamente")
            st.rerun()
        else:
            st.error("❌ Complete los campos obligatorios")

def mostrar_controles_clinicos():
    """Control clínico de pacientes"""
    
    st.header("📋 Control Clínico")
    st.markdown("**Seguimiento de controles clínicos**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📋 Información del Control")
        
        rut_control = st.text_input("RUT del Paciente:", key="gc_rut_control")
        fecha_control = st.date_input("Fecha del Control:", key="gc_fecha_control")
        
        tipo_control = st.selectbox(
            "Tipo de Control:",
            [
                "Control Hipertensión", "Control Diabetes", "Control Obesidad",
                "Control Respiratorio", "Control Salud Mental", "Control General",
                "Control Domiciliario", "Otro"
            ],
            key="gc_tipo_control"
        )
        
        profesional_control = st.text_input("Profesional Responsable:", key="gc_profesional_control")
        
    with col2:
        st.subheader("📊 Signos Vitales")
        
        presion_sistolica = st.number_input("Presión Sistólica (mmHg):", min_value=0, key="gc_presion_sistolica")
        presion_diastolica = st.number_input("Presión Diastólica (mmHg):", min_value=0, key="gc_presion_diastolica")
        frecuencia_cardiaca = st.number_input("Frecuencia Cardíaca (lpm):", min_value=0, key="gc_frecuencia_cardiaca")
        temperatura = st.number_input("Temperatura (°C):", min_value=30.0, max_value=45.0, step=0.1, key="gc_temperatura")
        peso = st.number_input("Peso (kg):", min_value=0.0, key="gc_peso")
        talla = st.number_input("Talla (cm):", min_value=0, key="gc_talla")
    
    st.subheader("🔍 Evaluación Clínica")
    
    col1, col2 = st.columns(2)
    
    with col1:
        sintomas = st.multiselect(
            "Síntomas Presentes:",
            [
                "Dolor de cabeza", "Fatiga", "Dificultad para respirar",
                "Dolor en el pecho", "Mareos", "Náuseas",
                "Vómitos", "Diarrea", "Fiebre", "Tos",
                "Dolor articular", "Hinchazón", "Otro"
            ],
            key="gc_sintomas"
        )
        
        estado_general = st.selectbox(
            "Estado General:",
            ["Excelente", "Bueno", "Regular", "Malo", "Muy Malo"],
            key="gc_estado_general"
        )
        
        cumplimiento_tratamiento = st.selectbox(
            "Cumplimiento del Tratamiento:",
            ["Excelente", "Bueno", "Regular", "Malo", "Sin tratamiento"],
            key="gc_cumplimiento"
        )
    
    with col2:
        complicaciones = st.text_area(
            "Complicaciones Identificadas:",
            placeholder="Complicaciones o problemas detectados...",
            key="gc_complicaciones"
        )
        
        plan_accion = st.text_area(
            "Plan de Acción:",
            placeholder="Acciones a realizar, cambios en tratamiento...",
            key="gc_plan_accion"
        )
    
    proximo_control = st.date_input("Próximo Control:", key="gc_proximo_control")
    
    observaciones_control = st.text_area(
        "Observaciones del Control:",
        key="gc_obs_control"
    )
    
    if st.button("💾 Guardar Control Clínico", key="gc_guardar_control"):
        if rut_control and fecha_control:
            control = {
                'id': len(st.session_state.gestion_clinica_aps['controles_realizados']) + 1,
                'rut_paciente': rut_control,
                'fecha': str(fecha_control),
                'tipo': tipo_control,
                'profesional': profesional_control,
                'signos_vitales': {
                    'presion_sistolica': presion_sistolica,
                    'presion_diastolica': presion_diastolica,
                    'frecuencia_cardiaca': frecuencia_cardiaca,
                    'temperatura': temperatura,
                    'peso': peso,
                    'talla': talla
                },
                'sintomas': sintomas,
                'estado_general': estado_general,
                'cumplimiento': cumplimiento_tratamiento,
                'complicaciones': complicaciones,
                'plan_accion': plan_accion,
                'proximo_control': str(proximo_control),
                'observaciones': observaciones_control
            }
            
            st.session_state.gestion_clinica_aps['controles_realizados'].append(control)
            st.success("✅ Control clínico guardado exitosamente")
            st.rerun()
        else:
            st.error("❌ Complete los campos obligatorios")

def mostrar_educacion_salud():
    """Educación en salud para pacientes"""
    
    st.header("📚 Educación en Salud")
    st.markdown("**Sesiones educativas para pacientes y familias**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📋 Información de la Sesión")
        
        nombre_sesion = st.text_input("Nombre de la Sesión:", key="gc_nombre_sesion")
        fecha_sesion = st.date_input("Fecha de la Sesión:", key="gc_fecha_sesion")
        
        tipo_educacion = st.selectbox(
            "Tipo de Educación:",
            [
                "Manejo de Hipertensión", "Control de Diabetes", "Alimentación Saludable",
                "Actividad Física", "Manejo del Estrés", "Prevención de Caídas",
                "Cuidado de Medicamentos", "Signos de Alarma", "Otro"
            ],
            key="gc_tipo_educacion"
        )
        
        modalidad = st.selectbox(
            "Modalidad:",
            ["Individual", "Grupal", "Familiar", "Comunitario"],
            key="gc_modalidad"
        )
        
    with col2:
        st.subheader("👥 Participantes")
        
        participantes = st.multiselect(
            "Participantes:",
            [
                "Paciente", "Familiar", "Cuidador", "Vecino",
                "Otro paciente", "Líder comunitario", "Otro"
            ],
            key="gc_participantes"
        )
        
        numero_participantes = st.number_input("Número de Participantes:", min_value=1, key="gc_num_participantes")
        
        duracion_sesion = st.number_input("Duración (minutos):", min_value=15, key="gc_duracion")
        
        lugar_sesion = st.text_input("Lugar de Realización:", key="gc_lugar_sesion")
    
    st.subheader("📝 Contenido de la Sesión")
    
    objetivos = st.text_area(
        "Objetivos de la Sesión:",
        placeholder="Qué se busca lograr con esta sesión...",
        key="gc_objetivos_sesion"
    )
    
    contenido = st.text_area(
        "Contenido Desarrollado:",
        placeholder="Temas tratados, actividades realizadas...",
        key="gc_contenido"
    )
    
    materiales_utilizados = st.text_area(
        "Materiales Utilizados:",
        placeholder="Folletos, videos, presentaciones...",
        key="gc_materiales"
    )
    
    st.subheader("📊 Evaluación")
    
    col1, col2 = st.columns(2)
    
    with col1:
        comprension = st.slider("Nivel de Comprensión (1-10):", 1, 10, 5, key="gc_comprension")
        participacion = st.slider("Nivel de Participación (1-10):", 1, 10, 5, key="gc_participacion_sesion")
    
    with col2:
        satisfaccion = st.slider("Satisfacción (1-10):", 1, 10, 5, key="gc_satisfaccion_sesion")
        aplicabilidad = st.slider("Aplicabilidad Práctica (1-10):", 1, 10, 5, key="gc_aplicabilidad")
    
    observaciones_educacion = st.text_area(
        "Observaciones y Recomendaciones:",
        key="gc_obs_educacion"
    )
    
    if st.button("💾 Guardar Sesión Educativa", key="gc_guardar_educacion"):
        if nombre_sesion and fecha_sesion:
            educacion = {
                'id': len(st.session_state.gestion_clinica_aps['educacion_salud']) + 1,
                'nombre': nombre_sesion,
                'fecha': str(fecha_sesion),
                'tipo': tipo_educacion,
                'modalidad': modalidad,
                'participantes': participantes,
                'numero_participantes': numero_participantes,
                'duracion': duracion_sesion,
                'lugar': lugar_sesion,
                'objetivos': objetivos,
                'contenido': contenido,
                'materiales': materiales_utilizados,
                'comprension': comprension,
                'participacion': participacion,
                'satisfaccion': satisfaccion,
                'aplicabilidad': aplicabilidad,
                'observaciones': observaciones_educacion
            }
            
            st.session_state.gestion_clinica_aps['educacion_salud'].append(educacion)
            st.success("✅ Sesión educativa guardada exitosamente")
            st.rerun()
        else:
            st.error("❌ Complete los campos obligatorios")

def mostrar_seguimiento_tratamientos():
    """Seguimiento de tratamientos farmacológicos y no farmacológicos"""
    
    st.header("💊 Seguimiento de Tratamientos")
    st.markdown("**Control de adherencia y efectividad de tratamientos**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📋 Información del Seguimiento")
        
        rut_seguimiento = st.text_input("RUT del Paciente:", key="gc_rut_seg")
        fecha_seguimiento = st.date_input("Fecha de Seguimiento:", key="gc_fecha_seg")
        
        tipo_tratamiento = st.selectbox(
            "Tipo de Tratamiento:",
            [
                "Farmacológico", "No Farmacológico", "Mixto",
                "Cambio de Dosis", "Suspensión", "Nuevo Tratamiento"
            ],
            key="gc_tipo_tratamiento"
        )
        
        profesional_seguimiento = st.text_input("Profesional Responsable:", key="gc_prof_seg")
        
    with col2:
        st.subheader("💊 Información del Tratamiento")
        
        medicamentos = st.text_area(
            "Medicamentos:",
            placeholder="Lista de medicamentos actuales...",
            key="gc_medicamentos_seg"
        )
        
        dosis = st.text_input("Dosis:", key="gc_dosis")
        frecuencia = st.text_input("Frecuencia:", key="gc_frecuencia")
    
    st.subheader("📊 Evaluación del Tratamiento")
    
    col1, col2 = st.columns(2)
    
    with col1:
        adherencia = st.selectbox(
            "Adherencia al Tratamiento:",
            ["Excelente (>90%)", "Buena (70-90%)", "Regular (50-70%)", "Mala (<50%)"],
            key="gc_adherencia"
        )
        
        efectividad = st.selectbox(
            "Efectividad:",
            ["Excelente", "Buena", "Regular", "Mala", "Sin efecto"],
            key="gc_efectividad"
        )
        
        efectos_secundarios = st.multiselect(
            "Efectos Secundarios:",
            [
                "Náuseas", "Vómitos", "Dolor de cabeza", "Mareos",
                "Fatiga", "Diarrea", "Estreñimiento", "Alergias",
                "Cambios en el apetito", "Problemas de sueño", "Otro"
            ],
            key="gc_efectos_secundarios"
        )
    
    with col2:
        barreras_cumplimiento = st.multiselect(
            "Barreras para el Cumplimiento:",
            [
                "Olvido", "Efectos secundarios", "Costo", "Complejidad",
                "Falta de comprensión", "Horarios", "Disponibilidad",
                "Estigma", "Otro"
            ],
            key="gc_barreras"
        )
        
        estrategias_mejora = st.text_area(
            "Estrategias de Mejora:",
            placeholder="Estrategias para mejorar la adherencia...",
            key="gc_estrategias"
        )
    
    st.subheader("📝 Plan de Acción")
    
    cambios_tratamiento = st.text_area(
        "Cambios en el Tratamiento:",
        placeholder="Modificaciones, ajustes, nuevas indicaciones...",
        key="gc_cambios"
    )
    
    proximo_seguimiento = st.date_input("Próximo Seguimiento:", key="gc_proximo_seg")
    
    observaciones_tratamiento = st.text_area(
        "Observaciones:",
        key="gc_obs_tratamiento"
    )
    
    if st.button("💾 Guardar Seguimiento de Tratamiento", key="gc_guardar_seg_tratamiento"):
        if rut_seguimiento and fecha_seguimiento:
            seguimiento = {
                'id': len(st.session_state.gestion_clinica_aps['seguimientos_tratamiento']) + 1,
                'rut_paciente': rut_seguimiento,
                'fecha': str(fecha_seguimiento),
                'tipo_tratamiento': tipo_tratamiento,
                'profesional': profesional_seguimiento,
                'medicamentos': medicamentos,
                'dosis': dosis,
                'frecuencia': frecuencia,
                'adherencia': adherencia,
                'efectividad': efectividad,
                'efectos_secundarios': efectos_secundarios,
                'barreras': barreras_cumplimiento,
                'estrategias': estrategias_mejora,
                'cambios': cambios_tratamiento,
                'proximo_seguimiento': str(proximo_seguimiento),
                'observaciones': observaciones_tratamiento
            }
            
            st.session_state.gestion_clinica_aps['seguimientos_tratamiento'].append(seguimiento)
            st.success("✅ Seguimiento de tratamiento guardado exitosamente")
            st.rerun()
        else:
            st.error("❌ Complete los campos obligatorios")

def mostrar_derivaciones():
    """Sistema de derivaciones"""
    
    st.header("🔄 Sistema de Derivaciones")
    st.markdown("**Coordinación con otros niveles de atención**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📋 Información de la Derivación")
        
        rut_derivacion = st.text_input("RUT del Paciente:", key="gc_rut_der")
        fecha_derivacion = st.date_input("Fecha de Derivación:", key="gc_fecha_der")
        
        tipo_derivacion = st.selectbox(
            "Tipo de Derivación:",
            [
                "Especialista", "Hospital", "Centro de Salud",
                "Salud Mental", "Rehabilitación", "Laboratorio",
                "Imagenología", "Otro"
            ],
            key="gc_tipo_derivacion"
        )
        
        especialidad = st.selectbox(
            "Especialidad:",
            [
                "Cardiología", "Endocrinología", "Neurología",
                "Psiquiatría", "Oftalmología", "Ortopedia",
                "Dermatología", "Ginecología", "Pediatría",
                "Geriatría", "Otro"
            ],
            key="gc_especialidad"
        )
        
    with col2:
        st.subheader("🏥 Destino")
        
        establecimiento = st.text_input("Establecimiento Destino:", key="gc_establecimiento")
        profesional_destino = st.text_input("Profesional Destino:", key="gc_prof_destino")
        
        urgencia = st.selectbox(
            "Nivel de Urgencia:",
            ["Rutinaria", "Preferente", "Urgente", "Emergencia"],
            key="gc_urgencia"
        )
        
        motivo_derivacion = st.text_area(
            "Motivo de la Derivación:",
            placeholder="Razón específica de la derivación...",
            key="gc_motivo"
        )
    
    st.subheader("📝 Información Clínica")
    
    col1, col2 = st.columns(2)
    
    with col1:
        diagnostico_presuntivo = st.text_area(
            "Diagnóstico Presuntivo:",
            placeholder="Diagnóstico que motiva la derivación...",
            key="gc_diagnostico_presuntivo"
        )
        
        examenes_realizados = st.text_area(
            "Exámenes Realizados:",
            placeholder="Exámenes previos, resultados...",
            key="gc_examenes"
        )
    
    with col2:
        tratamiento_actual = st.text_area(
            "Tratamiento Actual:",
            placeholder="Medicamentos y tratamientos en curso...",
            key="gc_tratamiento_actual"
        )
        
        observaciones_derivacion = st.text_area(
            "Observaciones Importantes:",
            placeholder="Información adicional relevante...",
            key="gc_obs_derivacion"
        )
    
    fecha_control = st.date_input("Fecha de Control Post-Derivación:", key="gc_fecha_control_post")
    
    if st.button("💾 Guardar Derivación", key="gc_guardar_derivacion"):
        if rut_derivacion and establecimiento and motivo_derivacion:
            derivacion = {
                'id': len(st.session_state.gestion_clinica_aps['derivaciones']) + 1,
                'rut_paciente': rut_derivacion,
                'fecha': str(fecha_derivacion),
                'tipo': tipo_derivacion,
                'especialidad': especialidad,
                'establecimiento': establecimiento,
                'profesional_destino': profesional_destino,
                'urgencia': urgencia,
                'motivo': motivo_derivacion,
                'diagnostico_presuntivo': diagnostico_presuntivo,
                'examenes': examenes_realizados,
                'tratamiento_actual': tratamiento_actual,
                'observaciones': observaciones_derivacion,
                'fecha_control': str(fecha_control)
            }
            
            st.session_state.gestion_clinica_aps['derivaciones'].append(derivacion)
            st.success("✅ Derivación guardada exitosamente")
            st.rerun()
        else:
            st.error("❌ Complete los campos obligatorios")

def mostrar_indicadores_clinicos():
    """Indicadores clínicos de gestión"""
    
    st.header("📊 Indicadores Clínicos de Gestión")
    st.markdown("**Métricas de calidad y efectividad**")
    
    # Métricas generales
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_pacientes = len(st.session_state.gestion_clinica_aps['pacientes_cronicos'])
        st.metric("Pacientes Crónicos", total_pacientes)
    
    with col2:
        total_controles = len(st.session_state.gestion_clinica_aps['controles_realizados'])
        st.metric("Controles Realizados", total_controles)
    
    with col3:
        total_educacion = len(st.session_state.gestion_clinica_aps['educacion_salud'])
        st.metric("Sesiones Educativas", total_educacion)
    
    with col4:
        total_derivaciones = len(st.session_state.gestion_clinica_aps['derivaciones'])
        st.metric("Derivaciones", total_derivaciones)
    
    # Gráficos
    col1, col2 = st.columns(2)
    
    with col1:
        if st.session_state.gestion_clinica_aps['pacientes_cronicos']:
            st.subheader("📊 Enfermedades Crónicas")
            
            # Contar enfermedades
            enfermedades_count = {}
            for paciente in st.session_state.gestion_clinica_aps['pacientes_cronicos']:
                for enfermedad in paciente['enfermedades']:
                    enfermedades_count[enfermedad] = enfermedades_count.get(enfermedad, 0) + 1
            
            if enfermedades_count:
                df_enfermedades = pd.DataFrame([
                    {'Enfermedad': k, 'Pacientes': v}
                    for k, v in enfermedades_count.items()
                ])
                
                fig_enfermedades = px.bar(
                    df_enfermedades,
                    x='Enfermedad',
                    y='Pacientes',
                    title="Distribución de Enfermedades Crónicas"
                )
                st.plotly_chart(fig_enfermedades, use_container_width=True)
    
    with col2:
        if st.session_state.gestion_clinica_aps['controles_realizados']:
            st.subheader("📈 Tipos de Control")
            
            df_controles = pd.DataFrame([
                {
                    'Tipo': c['tipo'],
                    'Fecha': c['fecha']
                }
                for c in st.session_state.gestion_clinica_aps['controles_realizados']
            ])
            
            if not df_controles.empty:
                fig_controles = px.pie(
                    df_controles.groupby('Tipo').size().reset_index(name='Cantidad'),
                    values='Cantidad',
                    names='Tipo',
                    title="Distribución de Tipos de Control"
                )
                st.plotly_chart(fig_controles, use_container_width=True)
    
    # Tabla de pacientes
    if st.session_state.gestion_clinica_aps['pacientes_cronicos']:
        st.subheader("📋 Lista de Pacientes Crónicos")
        
        df_pacientes = pd.DataFrame([
            {
                'RUT': p['rut'],
                'Nombre': p['nombre'],
                'Enfermedades': ', '.join(p['enfermedades']),
                'Nivel Riesgo': p['nivel_riesgo'],
                'Estado Funcional': p['estado_funcional'],
                'Fecha Registro': p['fecha_registro']
            }
            for p in st.session_state.gestion_clinica_aps['pacientes_cronicos']
        ])
        
        st.dataframe(df_pacientes, use_container_width=True)
    
    # Exportar datos
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📊 Exportar Datos a CSV", key="gc_exportar_csv"):
            if st.session_state.gestion_clinica_aps['pacientes_cronicos']:
                df_export = pd.DataFrame(st.session_state.gestion_clinica_aps['pacientes_cronicos'])
                csv = df_export.to_csv(index=False)
                st.download_button(
                    label="⬇️ Descargar CSV",
                    data=csv,
                    file_name="gestion_clinica_aps.csv",
                    mime="text/csv"
                )
    
    with col2:
        if st.button("📄 Generar Reporte Completo", key="gc_generar_reporte"):
            st.info("📋 Reporte generado en la consola")
            st.json(st.session_state.gestion_clinica_aps) 