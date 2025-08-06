import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json

def mostrar_educacion_promocion_salud():
    """
    Módulo de Educación para la Salud y Promoción de la Salud
    Incluye: Objetivos SMART, Modelo de Creencias en Salud, Etapas del Ciclo de Vida
    """
    
    st.title("📚 Educación para la Salud y Promoción de la Salud")
    st.markdown("### Estrategias Educativas y Promocionales en APS - Enfoque TENS")
    
    # Inicializar session state
    if 'educacion_promocion_salud' not in st.session_state:
        st.session_state.educacion_promocion_salud = {
            'objetivos_smart': [],
            'intervenciones_educativas': [],
            'evaluacion_creencias': [],
            'programas_ciclo_vida': [],
            'indicadores_educacion': []
        }
    
    # Pestañas principales
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🎯 Objetivos SMART", 
        "📖 Intervenciones Educativas",
        "🧠 Modelo de Creencias en Salud", 
        "👶 Etapas del Ciclo de Vida",
        "📊 Indicadores"
    ])
    
    with tab1:
        mostrar_objetivos_smart()
    
    with tab2:
        mostrar_intervenciones_educativas()
    
    with tab3:
        mostrar_modelo_creencias()
    
    with tab4:
        mostrar_etapas_ciclo_vida()
    
    with tab5:
        mostrar_indicadores_educacion()

def mostrar_objetivos_smart():
    """Formulación de objetivos SMART para educación en salud"""
    
    st.header("🎯 Formulación de Objetivos SMART")
    st.markdown("**Específicos, Medibles, Alcanzables, Relevantes y con Tiempo definido**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📋 Nuevo Objetivo SMART")
        
        titulo = st.text_input("Título del Objetivo:", key="smart_titulo")
        
        # Componentes SMART
        st.markdown("#### Componentes SMART:")
        
        especifico = st.text_area("**S - Específico:** ¿Qué se quiere lograr exactamente?", key="smart_especifico")
        medible = st.text_area("**M - Medible:** ¿Cómo se medirá el progreso?", key="smart_medible")
        alcanzable = st.text_area("**A - Alcanzable:** ¿Es realista con los recursos disponibles?", key="smart_alcanzable")
        relevante = st.text_area("**R - Relevante:** ¿Por qué es importante este objetivo?", key="smart_relevante")
        tiempo = st.text_area("**T - Tiempo:** ¿Cuándo se logrará?", key="smart_tiempo")
        
        # Categoría del objetivo
        categoria = st.selectbox(
            "Categoría:",
            [
                "Prevención Primaria", "Prevención Secundaria", "Prevención Terciaria",
                "Promoción de la Salud", "Educación Sanitaria", "Empoderamiento Comunitario",
                "Cambio de Comportamiento", "Mejora de Acceso", "Calidad de Vida"
            ],
            key="smart_categoria"
        )
        
        # Población objetivo
        poblacion = st.multiselect(
            "Población Objetivo:",
            [
                "Niños (0-5 años)", "Escolares (6-12 años)", "Adolescentes (13-17 años)",
                "Adultos Jóvenes (18-29 años)", "Adultos (30-59 años)", "Adultos Mayores (60+)",
                "Mujeres Embarazadas", "Familias", "Comunidad General"
            ],
            key="smart_poblacion"
        )
        
        if st.button("💾 Guardar Objetivo SMART", key="guardar_smart"):
            if titulo and especifico and medible and alcanzable and relevante and tiempo:
                objetivo = {
                    'id': len(st.session_state.educacion_promocion_salud['objetivos_smart']) + 1,
                    'titulo': titulo,
                    'especifico': especifico,
                    'medible': medible,
                    'alcanzable': alcanzable,
                    'relevante': relevante,
                    'tiempo': tiempo,
                    'categoria': categoria,
                    'poblacion': poblacion,
                    'fecha_creacion': datetime.now().strftime("%Y-%m-%d %H:%M"),
                    'estado': 'En Progreso'
                }
                
                st.session_state.educacion_promocion_salud['objetivos_smart'].append(objetivo)
                st.success("✅ Objetivo SMART guardado exitosamente")
                
                # Limpiar campos
                st.rerun()
            else:
                st.error("❌ Por favor completa todos los campos obligatorios")
    
    with col2:
        st.subheader("📊 Objetivos SMART Registrados")
        
        if st.session_state.educacion_promocion_salud['objetivos_smart']:
            for objetivo in st.session_state.educacion_promocion_salud['objetivos_smart']:
                with st.expander(f"🎯 {objetivo['titulo']} - {objetivo['categoria']}", expanded=False):
                    st.write(f"**Específico:** {objetivo['especifico']}")
                    st.write(f"**Medible:** {objetivo['medible']}")
                    st.write(f"**Alcanzable:** {objetivo['alcanzable']}")
                    st.write(f"**Relevante:** {objetivo['relevante']}")
                    st.write(f"**Tiempo:** {objetivo['tiempo']}")
                    st.write(f"**Población:** {', '.join(objetivo['poblacion'])}")
                    st.write(f"**Estado:** {objetivo['estado']}")
                    st.write(f"**Fecha:** {objetivo['fecha_creacion']}")
                    
                    # Cambiar estado
                    nuevo_estado = st.selectbox(
                        "Cambiar estado:",
                        ["En Progreso", "Completado", "Pendiente", "Cancelado"],
                        index=["En Progreso", "Completado", "Pendiente", "Cancelado"].index(objetivo['estado']),
                        key=f"estado_{objetivo['id']}"
                    )
                    if nuevo_estado != objetivo['estado']:
                        objetivo['estado'] = nuevo_estado
                        st.success(f"Estado actualizado a: {nuevo_estado}")
        else:
            st.info("📝 No hay objetivos SMART registrados. Crea el primero en el panel izquierdo.")

def mostrar_intervenciones_educativas():
    """Diseño e implementación de intervenciones educativas"""
    
    st.header("📖 Intervenciones Educativas")
    st.markdown("**Diseño, implementación y evaluación de estrategias educativas**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎨 Nueva Intervención Educativa")
        
        nombre = st.text_input("Nombre de la Intervención:", key="interv_nombre")
        
        # Tipo de intervención
        tipo_intervencion = st.selectbox(
            "Tipo de Intervención:",
            [
                "Educación Individual", "Educación Grupal", "Talleres Comunitarios",
                "Material Educativo", "Campañas de Comunicación", "Tecnologías Digitales",
                "Intervención Familiar", "Educación en Escuelas", "Capacitación de Líderes"
            ],
            key="interv_tipo"
        )
        
        # Metodología educativa
        metodologia = st.multiselect(
            "Metodología Educativa:",
            [
                "Exposición Magistral", "Discusión Grupal", "Role Playing",
                "Casos Clínicos", "Demostración Práctica", "Aprendizaje Basado en Problemas",
                "Educación Entre Pares", "Tecnologías Interactivas", "Material Audiovisual"
            ],
            key="interv_metodologia"
        )
        
        # Contenido educativo
        contenido = st.text_area("Contenido Educativo:", key="interv_contenido")
        
        # Objetivos de aprendizaje
        objetivos = st.text_area("Objetivos de Aprendizaje:", key="interv_objetivos")
        
        # Duración y frecuencia
        duracion = st.text_input("Duración:", placeholder="Ej: 2 horas", key="interv_duracion")
        frecuencia = st.selectbox(
            "Frecuencia:",
            ["Única", "Semanal", "Quincenal", "Mensual", "Trimestral", "Semestral"],
            key="interv_frecuencia"
        )
        
        # Recursos necesarios
        recursos = st.text_area("Recursos Necesarios:", key="interv_recursos")
        
        if st.button("💾 Guardar Intervención", key="guardar_intervencion"):
            if nombre and contenido and objetivos:
                intervencion = {
                    'id': len(st.session_state.educacion_promocion_salud['intervenciones_educativas']) + 1,
                    'nombre': nombre,
                    'tipo': tipo_intervencion,
                    'metodologia': metodologia,
                    'contenido': contenido,
                    'objetivos': objetivos,
                    'duracion': duracion,
                    'frecuencia': frecuencia,
                    'recursos': recursos,
                    'fecha_creacion': datetime.now().strftime("%Y-%m-%d %H:%M"),
                    'estado': 'Planificada'
                }
                
                st.session_state.educacion_promocion_salud['intervenciones_educativas'].append(intervencion)
                st.success("✅ Intervención educativa guardada exitosamente")
                st.rerun()
            else:
                st.error("❌ Por favor completa los campos obligatorios")
    
    with col2:
        st.subheader("📋 Intervenciones Registradas")
        
        if st.session_state.educacion_promocion_salud['intervenciones_educativas']:
            for interv in st.session_state.educacion_promocion_salud['intervenciones_educativas']:
                with st.expander(f"📖 {interv['nombre']} - {interv['tipo']}", expanded=False):
                    st.write(f"**Metodología:** {', '.join(interv['metodologia'])}")
                    st.write(f"**Duración:** {interv['duracion']}")
                    st.write(f"**Frecuencia:** {interv['frecuencia']}")
                    st.write(f"**Objetivos:** {interv['objetivos']}")
                    st.write(f"**Contenido:** {interv['contenido']}")
                    st.write(f"**Recursos:** {interv['recursos']}")
                    st.write(f"**Estado:** {interv['estado']}")
                    
                    # Cambiar estado
                    nuevo_estado = st.selectbox(
                        "Cambiar estado:",
                        ["Planificada", "En Ejecución", "Completada", "Evaluada"],
                        index=["Planificada", "En Ejecución", "Completada", "Evaluada"].index(interv['estado']),
                        key=f"estado_interv_{interv['id']}"
                    )
                    if nuevo_estado != interv['estado']:
                        interv['estado'] = nuevo_estado
                        st.success(f"Estado actualizado a: {nuevo_estado}")
        else:
            st.info("📝 No hay intervenciones registradas. Crea la primera en el panel izquierdo.")

def mostrar_modelo_creencias():
    """Evaluación basada en el Modelo de Creencias en Salud"""
    
    st.header("🧠 Modelo de Creencias en Salud")
    st.markdown("**Evaluación de susceptibilidad, severidad, beneficios y barreras**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🔍 Evaluación de Creencias")
        
        # Seleccionar población
        poblacion_evaluacion = st.selectbox(
            "Población a Evaluar:",
            [
                "Familias con niños pequeños", "Adultos con enfermedades crónicas",
                "Mujeres embarazadas", "Adultos mayores", "Adolescentes",
                "Trabajadores", "Comunidad general"
            ],
            key="creencias_poblacion"
        )
        
        # Problema de salud
        problema_salud = st.text_input("Problema de Salud:", key="creencias_problema")
        
        st.markdown("#### Componentes del Modelo de Creencias:")
        
        # Susceptibilidad percibida
        susceptibilidad = st.slider(
            "**Susceptibilidad Percibida:** ¿Qué tan vulnerable se siente la población?",
            1, 10, 5, key="creencias_susceptibilidad"
        )
        
        # Severidad percibida
        severidad = st.slider(
            "**Severidad Percibida:** ¿Qué tan grave considera el problema?",
            1, 10, 5, key="creencias_severidad"
        )
        
        # Beneficios percibidos
        beneficios = st.slider(
            "**Beneficios Percibidos:** ¿Qué tan beneficiosa considera la acción preventiva?",
            1, 10, 5, key="creencias_beneficios"
        )
        
        # Barreras percibidas
        barreras = st.slider(
            "**Barreras Percibidas:** ¿Qué tan difícil considera realizar la acción?",
            1, 10, 5, key="creencias_barreras"
        )
        
        # Señales para la acción
        senales = st.text_area("**Señales para la Acción:** ¿Qué factores motivan la acción?", key="creencias_senales")
        
        # Autoeficacia
        autoeficacia = st.slider(
            "**Autoeficacia:** ¿Qué tan capaz se siente de realizar la acción?",
            1, 10, 5, key="creencias_autoeficacia"
        )
        
        # Recomendaciones basadas en el modelo
        recomendaciones = st.text_area("**Recomendaciones:** Estrategias basadas en el análisis", key="creencias_recomendaciones")
        
        if st.button("💾 Guardar Evaluación", key="guardar_creencias"):
            if problema_salud and senales and recomendaciones:
                evaluacion = {
                    'id': len(st.session_state.educacion_promocion_salud['evaluacion_creencias']) + 1,
                    'poblacion': poblacion_evaluacion,
                    'problema_salud': problema_salud,
                    'susceptibilidad': susceptibilidad,
                    'severidad': severidad,
                    'beneficios': beneficios,
                    'barreras': barreras,
                    'senales': senales,
                    'autoeficacia': autoeficacia,
                    'recomendaciones': recomendaciones,
                    'fecha_evaluacion': datetime.now().strftime("%Y-%m-%d %H:%M")
                }
                
                st.session_state.educacion_promocion_salud['evaluacion_creencias'].append(evaluacion)
                st.success("✅ Evaluación de creencias guardada exitosamente")
                st.rerun()
            else:
                st.error("❌ Por favor completa los campos obligatorios")
    
    with col2:
        st.subheader("📊 Análisis de Creencias")
        
        if st.session_state.educacion_promocion_salud['evaluacion_creencias']:
            # Gráfico de radar para la última evaluación
            ultima_eval = st.session_state.educacion_promocion_salud['evaluacion_creencias'][-1]
            
            fig = go.Figure()
            
            fig.add_trace(go.Scatterpolar(
                r=[ultima_eval['susceptibilidad'], ultima_eval['severidad'], 
                   ultima_eval['beneficios'], ultima_eval['barreras'], ultima_eval['autoeficacia']],
                theta=['Susceptibilidad', 'Severidad', 'Beneficios', 'Barreras', 'Autoeficacia'],
                fill='toself',
                name='Percepción Actual'
            ))
            
            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, 10]
                    )),
                showlegend=True,
                title=f"Análisis de Creencias: {ultima_eval['problema_salud']}"
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Lista de evaluaciones
            st.markdown("#### Evaluaciones Realizadas:")
            for eval in st.session_state.educacion_promocion_salud['evaluacion_creencias']:
                with st.expander(f"🔍 {eval['problema_salud']} - {eval['poblacion']}", expanded=False):
                    st.write(f"**Susceptibilidad:** {eval['susceptibilidad']}/10")
                    st.write(f"**Severidad:** {eval['severidad']}/10")
                    st.write(f"**Beneficios:** {eval['beneficios']}/10")
                    st.write(f"**Barreras:** {eval['barreras']}/10")
                    st.write(f"**Autoeficacia:** {eval['autoeficacia']}/10")
                    st.write(f"**Señales:** {eval['senales']}")
                    st.write(f"**Recomendaciones:** {eval['recomendaciones']}")
        else:
            st.info("📝 No hay evaluaciones de creencias registradas. Realiza la primera en el panel izquierdo.")

def mostrar_etapas_ciclo_vida():
    """Educación en salud según etapas del ciclo de vida"""
    
    st.header("👶 Educación en Salud por Etapas del Ciclo de Vida")
    st.markdown("**Intervenciones educativas específicas para cada etapa**")
    
    # Seleccionar etapa del ciclo de vida
    etapa = st.selectbox(
        "Seleccionar Etapa del Ciclo de Vida:",
        [
            "Embarazo y Parto",
            "Primera Infancia (0-2 años)",
            "Edad Preescolar (3-5 años)",
            "Edad Escolar (6-12 años)",
            "Adolescencia (13-17 años)",
            "Adultez Joven (18-29 años)",
            "Adultez Media (30-59 años)",
            "Adultez Mayor (60+ años)"
        ],
        key="ciclo_vida_etapa"
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader(f"📚 Programa Educativo - {etapa}")
        
        # Contenidos específicos por etapa
        contenidos_etapa = {
            "Embarazo y Parto": [
                "Cuidados prenatales", "Nutrición durante el embarazo", "Preparación para el parto",
                "Lactancia materna", "Cuidados del recién nacido", "Salud mental perinatal"
            ],
            "Primera Infancia (0-2 años)": [
                "Desarrollo psicomotor", "Vacunación", "Alimentación complementaria",
                "Prevención de accidentes", "Estimulación temprana", "Control de crecimiento"
            ],
            "Edad Preescolar (3-5 años)": [
                "Desarrollo social y emocional", "Hábitos de higiene", "Alimentación saludable",
                "Prevención de accidentes", "Desarrollo del lenguaje", "Actividad física"
            ],
            "Edad Escolar (6-12 años)": [
                "Salud bucal", "Nutrición escolar", "Actividad física y deportes",
                "Prevención de bullying", "Uso seguro de internet", "Hábitos de estudio"
            ],
            "Adolescencia (13-17 años)": [
                "Salud sexual y reproductiva", "Prevención de adicciones", "Salud mental",
                "Alimentación y trastornos alimentarios", "Actividad física", "Proyecto de vida"
            ],
            "Adultez Joven (18-29 años)": [
                "Planificación familiar", "Prevención de ITS", "Salud ocupacional",
                "Estilos de vida saludables", "Prevención de violencia", "Desarrollo profesional"
            ],
            "Adultez Media (30-59 años)": [
                "Prevención de enfermedades crónicas", "Salud cardiovascular", "Cáncer",
                "Salud mental y estrés", "Equilibrio trabajo-familia", "Envejecimiento saludable"
            ],
            "Adultez Mayor (60+ años)": [
                "Envejecimiento activo", "Prevención de caídas", "Salud mental",
                "Nutrición en el adulto mayor", "Actividad física adaptada", "Cuidados paliativos"
            ]
        }
        
        # Mostrar contenidos específicos
        st.markdown("#### Contenidos Educativos Específicos:")
        for contenido in contenidos_etapa[etapa]:
            st.write(f"• {contenido}")
        
        # Nuevo programa educativo
        st.markdown("#### Crear Nuevo Programa:")
        
        nombre_programa = st.text_input("Nombre del Programa:", key="programa_nombre")
        objetivo_programa = st.text_area("Objetivo del Programa:", key="programa_objetivo")
        metodologia_programa = st.multiselect(
            "Metodología:",
            [
                "Talleres grupales", "Educación individual", "Material educativo",
                "Tecnologías digitales", "Actividades prácticas", "Educación entre pares"
            ],
            key="programa_metodologia"
        )
        duracion_programa = st.text_input("Duración:", key="programa_duracion")
        recursos_programa = st.text_area("Recursos Necesarios:", key="programa_recursos")
        
        if st.button("💾 Guardar Programa", key="guardar_programa"):
            if nombre_programa and objetivo_programa:
                programa = {
                    'id': len(st.session_state.educacion_promocion_salud['programas_ciclo_vida']) + 1,
                    'etapa': etapa,
                    'nombre': nombre_programa,
                    'objetivo': objetivo_programa,
                    'metodologia': metodologia_programa,
                    'duracion': duracion_programa,
                    'recursos': recursos_programa,
                    'fecha_creacion': datetime.now().strftime("%Y-%m-%d %H:%M"),
                    'estado': 'Planificado'
                }
                
                st.session_state.educacion_promocion_salud['programas_ciclo_vida'].append(programa)
                st.success("✅ Programa educativo guardado exitosamente")
                st.rerun()
            else:
                st.error("❌ Por favor completa los campos obligatorios")
    
    with col2:
        st.subheader("📋 Programas por Etapa")
        
        # Filtrar programas por etapa seleccionada
        programas_etapa = [p for p in st.session_state.educacion_promocion_salud['programas_ciclo_vida'] 
                          if p['etapa'] == etapa]
        
        if programas_etapa:
            for programa in programas_etapa:
                with st.expander(f"📚 {programa['nombre']}", expanded=False):
                    st.write(f"**Objetivo:** {programa['objetivo']}")
                    st.write(f"**Metodología:** {', '.join(programa['metodologia'])}")
                    st.write(f"**Duración:** {programa['duracion']}")
                    st.write(f"**Recursos:** {programa['recursos']}")
                    st.write(f"**Estado:** {programa['estado']}")
                    
                    # Cambiar estado
                    nuevo_estado = st.selectbox(
                        "Cambiar estado:",
                        ["Planificado", "En Ejecución", "Completado", "Evaluado"],
                        index=["Planificado", "En Ejecución", "Completado", "Evaluado"].index(programa['estado']),
                        key=f"estado_programa_{programa['id']}"
                    )
                    if nuevo_estado != programa['estado']:
                        programa['estado'] = nuevo_estado
                        st.success(f"Estado actualizado a: {nuevo_estado}")
        else:
            st.info(f"📝 No hay programas registrados para {etapa}. Crea el primero en el panel izquierdo.")

def mostrar_indicadores_educacion():
    """Indicadores de evaluación de programas educativos"""
    
    st.header("📊 Indicadores de Educación en Salud")
    st.markdown("**Evaluación y seguimiento de programas educativos**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Nuevo Indicador")
        
        nombre_indicador = st.text_input("Nombre del Indicador:", key="indicador_nombre")
        
        tipo_indicador = st.selectbox(
            "Tipo de Indicador:",
            [
                "Cobertura", "Conocimientos", "Actitudes", "Prácticas",
                "Satisfacción", "Retención", "Aplicación", "Impacto"
            ],
            key="indicador_tipo"
        )
        
        descripcion = st.text_area("Descripción:", key="indicador_descripcion")
        
        metodo_medicion = st.text_area("Método de Medición:", key="indicador_metodo")
        
        meta = st.number_input("Meta (%):", min_value=0, max_value=100, value=80, key="indicador_meta")
        
        valor_actual = st.number_input("Valor Actual (%):", min_value=0, max_value=100, value=0, key="indicador_actual")
        
        programa_asociado = st.selectbox(
            "Programa Asociado:",
            ["Todos"] + [p['nombre'] for p in st.session_state.educacion_promocion_salud['programas_ciclo_vida']],
            key="indicador_programa"
        )
        
        if st.button("💾 Guardar Indicador", key="guardar_indicador"):
            if nombre_indicador and descripcion and metodo_medicion:
                indicador = {
                    'id': len(st.session_state.educacion_promocion_salud['indicadores_educacion']) + 1,
                    'nombre': nombre_indicador,
                    'tipo': tipo_indicador,
                    'descripcion': descripcion,
                    'metodo_medicion': metodo_medicion,
                    'meta': meta,
                    'valor_actual': valor_actual,
                    'programa_asociado': programa_asociado,
                    'fecha_creacion': datetime.now().strftime("%Y-%m-%d %H:%M")
                }
                
                st.session_state.educacion_promocion_salud['indicadores_educacion'].append(indicador)
                st.success("✅ Indicador guardado exitosamente")
                st.rerun()
            else:
                st.error("❌ Por favor completa los campos obligatorios")
    
    with col2:
        st.subheader("📊 Dashboard de Indicadores")
        
        if st.session_state.educacion_promocion_salud['indicadores_educacion']:
            # Gráfico de barras para indicadores
            df_indicadores = pd.DataFrame(st.session_state.educacion_promocion_salud['indicadores_educacion'])
            
            fig = go.Figure()
            
            fig.add_trace(go.Bar(
                x=df_indicadores['nombre'],
                y=df_indicadores['valor_actual'],
                name='Valor Actual',
                marker_color='lightblue'
            ))
            
            fig.add_trace(go.Bar(
                x=df_indicadores['nombre'],
                y=df_indicadores['meta'],
                name='Meta',
                marker_color='orange'
            ))
            
            fig.update_layout(
                title="Progreso de Indicadores",
                xaxis_title="Indicadores",
                yaxis_title="Porcentaje (%)",
                barmode='group'
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Resumen de indicadores
            st.markdown("#### Resumen:")
            total_indicadores = len(st.session_state.educacion_promocion_salud['indicadores_educacion'])
            indicadores_cumplidos = len([i for i in st.session_state.educacion_promocion_salud['indicadores_educacion'] 
                                       if i['valor_actual'] >= i['meta']])
            
            st.metric("Total de Indicadores", total_indicadores)
            st.metric("Indicadores Cumplidos", indicadores_cumplidos)
            st.metric("Porcentaje de Cumplimiento", f"{(indicadores_cumplidos/total_indicadores)*100:.1f}%" if total_indicadores > 0 else "0%")
        else:
            st.info("📝 No hay indicadores registrados. Crea el primero en el panel izquierdo.")
    
    # Exportar datos
    if st.session_state.educacion_promocion_salud['indicadores_educacion']:
        st.markdown("---")
        st.subheader("📤 Exportar Datos")
        
        if st.button("📊 Exportar a JSON"):
            st.json(st.session_state.educacion_promocion_salud) 