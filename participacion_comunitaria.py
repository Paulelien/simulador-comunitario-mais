import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json

def mostrar_participacion_comunitaria():
    st.title("🏘️ Participación Comunitaria y Análisis FODA")
    st.markdown("---")
    
    # Inicializar session state
    if 'participacion_comunitaria' not in st.session_state:
        st.session_state.participacion_comunitaria = {
            'encuestas': [],
            'grupos_focales': [],
            'analisis_foda': {
                'fortalezas': [],
                'oportunidades': [],
                'debilidades': [],
                'amenazas': []
            },
            'plan_anual': []
        }
    
    # Tabs para organizar las secciones
    tab1, tab2, tab3, tab4 = st.tabs([
        "📊 Encuestas Comunitarias", 
        "👥 Grupos Focales", 
        "🔍 Análisis FODA", 
        "📋 Plan Anual"
    ])
    
    with tab1:
        mostrar_encuestas_comunitarias()
    
    with tab2:
        mostrar_grupos_focales()
    
    with tab3:
        mostrar_analisis_foda()
    
    with tab4:
        mostrar_plan_anual()

def mostrar_encuestas_comunitarias():
    st.header("📊 Encuestas Comunitarias")
    st.markdown("**Objetivo:** Recopilar información directa de la comunidad sobre necesidades, percepción de servicios y participación.")
    
    # Formulario para nueva encuesta
    with st.expander("➕ Agregar Nueva Encuesta", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            tipo_encuesta = st.selectbox(
                "Tipo de Encuesta:",
                ["Satisfacción de Usuarios", "Necesidades de Salud", "Participación Comunitaria", 
                 "Acceso a Servicios", "Percepción de Calidad", "Otro"],
                key="tipo_encuesta"
            )
            
            fecha_encuesta = st.date_input("Fecha de Aplicación:", key="fecha_encuesta")
            
            num_encuestados = st.number_input("Número de Encuestados:", min_value=1, value=50, key="num_encuestados")
        
        with col2:
            sector_encuesta = st.selectbox(
                "Sector:",
                ["Sector A", "Sector B", "Sector C", "Todos los Sectores"],
                key="sector_encuesta"
            )
            
            metodo_aplicacion = st.selectbox(
                "Método de Aplicación:",
                ["Presencial", "Telefónica", "Digital", "Mixto"],
                key="metodo_aplicacion"
            )
            
            duracion_encuesta = st.number_input("Duración promedio (minutos):", min_value=1, value=15, key="duracion_encuesta")
        
        # Preguntas específicas según tipo
        st.subheader("Preguntas Clave:")
        
        if tipo_encuesta == "Satisfacción de Usuarios":
            preguntas = [
                "¿Cómo califica la atención recibida? (1-5)",
                "¿Recomendaría el CESFAM a otros? (Sí/No)",
                "¿Cuánto tiempo esperó para ser atendido?",
                "¿El personal fue amable y respetuoso? (1-5)"
            ]
        elif tipo_encuesta == "Necesidades de Salud":
            preguntas = [
                "¿Qué problemas de salud son más frecuentes en su familia?",
                "¿Qué servicios de salud necesita más?",
                "¿Hay barreras para acceder a la atención?",
                "¿Qué actividades preventivas le interesan más?"
            ]
        elif tipo_encuesta == "Participación Comunitaria":
            preguntas = [
                "¿Participa en organizaciones comunitarias? (Sí/No)",
                "¿Qué tipo de actividades comunitarias le interesan?",
                "¿Cómo le gustaría participar en el CESFAM?",
                "¿Conoce los programas de salud disponibles? (Sí/No)"
            ]
        else:
            preguntas = [
                "Pregunta 1:",
                "Pregunta 2:",
                "Pregunta 3:",
                "Pregunta 4:"
            ]
        
        for i, pregunta in enumerate(preguntas):
            st.text_input(f"Pregunta {i+1}:", value=pregunta, key=f"pregunta_encuesta_{i}")
        
        # Resultados principales
        st.subheader("Resultados Principales:")
        col1, col2 = st.columns(2)
        
        with col1:
            satisfaccion_general = st.slider("Satisfacción General (1-5):", 1, 5, 4, key="satisfaccion_general")
            participacion_interes = st.slider("Interés en Participación (1-5):", 1, 5, 3, key="participacion_interes")
        
        with col2:
            necesidades_prioritarias = st.multiselect(
                "Necesidades Prioritarias:",
                ["Salud Mental", "Salud Cardiovascular", "Salud Infantil", "Salud del Adulto Mayor", 
                 "Prevención de Cáncer", "Salud Sexual y Reproductiva", "Otro"],
                key="necesidades_prioritarias"
            )
            barreras_identificadas = st.multiselect(
                "Barreras Identificadas:",
                ["Horarios de Atención", "Distancia", "Falta de Especialistas", "Tiempo de Espera",
                 "Falta de Información", "Problemas de Transporte", "Otro"],
                key="barreras_identificadas"
            )
        
        observaciones = st.text_area("Observaciones y Conclusiones:", key="observaciones_encuesta")
        
        if st.button("💾 Guardar Encuesta", key="guardar_encuesta"):
            nueva_encuesta = {
                'id': len(st.session_state.participacion_comunitaria['encuestas']) + 1,
                'tipo': tipo_encuesta,
                'fecha': str(fecha_encuesta),
                'sector': sector_encuesta,
                'num_encuestados': num_encuestados,
                'metodo': metodo_aplicacion,
                'duracion': duracion_encuesta,
                'satisfaccion': satisfaccion_general,
                'participacion': participacion_interes,
                'necesidades': necesidades_prioritarias,
                'barreras': barreras_identificadas,
                'observaciones': observaciones
            }
            
            st.session_state.participacion_comunitaria['encuestas'].append(nueva_encuesta)
            st.success("✅ Encuesta guardada exitosamente")
            st.rerun()
    
    # Mostrar encuestas existentes
    if st.session_state.participacion_comunitaria['encuestas']:
        st.subheader("📋 Encuestas Realizadas")
        
        df_encuestas = pd.DataFrame(st.session_state.participacion_comunitaria['encuestas'])
        
        # Métricas generales
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Encuestas", len(df_encuestas))
        
        with col2:
            st.metric("Total Encuestados", df_encuestas['num_encuestados'].sum())
        
        with col3:
            st.metric("Satisfacción Promedio", f"{df_encuestas['satisfaccion'].mean():.1f}/5")
        
        with col4:
            st.metric("Participación Promedio", f"{df_encuestas['participacion'].mean():.1f}/5")
        
        # Gráficos
        col1, col2 = st.columns(2)
        
        with col1:
            # Satisfacción por tipo de encuesta
            fig_satisfaccion = px.bar(
                df_encuestas.groupby('tipo')['satisfaccion'].mean().reset_index(),
                x='tipo',
                y='satisfaccion',
                title="Satisfacción por Tipo de Encuesta",
                labels={'satisfaccion': 'Satisfacción (1-5)', 'tipo': 'Tipo de Encuesta'}
            )
            st.plotly_chart(fig_satisfaccion, use_container_width=True)
        
        with col2:
            # Participación por sector
            fig_participacion = px.bar(
                df_encuestas.groupby('sector')['participacion'].mean().reset_index(),
                x='sector',
                y='participacion',
                title="Interés en Participación por Sector",
                labels={'participacion': 'Interés (1-5)', 'sector': 'Sector'}
            )
            st.plotly_chart(fig_participacion, use_container_width=True)
        
        # Tabla de encuestas
        st.dataframe(df_encuestas[['tipo', 'fecha', 'sector', 'num_encuestados', 'satisfaccion', 'participacion']], use_container_width=True)

def mostrar_grupos_focales():
    st.header("👥 Grupos Focales")
    st.markdown("**Objetivo:** Profundizar en temas específicos a través de discusiones grupales estructuradas.")
    
    # Formulario para nuevo grupo focal
    with st.expander("➕ Agregar Nuevo Grupo Focal", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            tema_grupo = st.selectbox(
                "Tema del Grupo Focal:",
                ["Necesidades de Salud Mental", "Acceso a Especialistas", "Programas Preventivos",
                 "Participación Comunitaria", "Calidad de Atención", "Otro"],
                key="tema_grupo"
            )
            
            fecha_grupo = st.date_input("Fecha de Realización:", key="fecha_grupo")
            
            num_participantes = st.number_input("Número de Participantes:", min_value=1, value=12, key="num_participantes")
        
        with col2:
            perfil_participantes = st.selectbox(
                "Perfil de Participantes:",
                ["Usuarios del CESFAM", "Líderes Comunitarios", "Adultos Mayores", "Mujeres",
                 "Hombres", "Jóvenes", "Mixto"],
                key="perfil_participantes"
            )
            
            duracion_grupo = st.number_input("Duración (horas):", min_value=0.5, value=2.0, step=0.5, key="duracion_grupo")
            
            facilitador = st.text_input("Facilitador:", key="facilitador")
        
        # Preguntas guía
        st.subheader("Preguntas Guía:")
        preguntas_grupo = []
        for i in range(5):
            pregunta = st.text_input(f"Pregunta {i+1}:", key=f"pregunta_grupo_focal_{i}")
            if pregunta:
                preguntas_grupo.append(pregunta)
        
        # Hallazgos principales
        st.subheader("Hallazgos Principales:")
        hallazgos_positivos = st.text_area("Hallazgos Positivos:", key="hallazgos_positivos")
        hallazgos_negativos = st.text_area("Hallazgos Negativos:", key="hallazgos_negativos")
        recomendaciones = st.text_area("Recomendaciones:", key="recomendaciones_grupo")
        
        # Nivel de participación
        participacion_nivel = st.slider("Nivel de Participación (1-5):", 1, 5, 4, key="participacion_nivel")
        satisfaccion_grupo = st.slider("Satisfacción del Grupo (1-5):", 1, 5, 4, key="satisfaccion_grupo")
        
        if st.button("💾 Guardar Grupo Focal", key="guardar_grupo_focal"):
            nuevo_grupo = {
                'id': len(st.session_state.participacion_comunitaria['grupos_focales']) + 1,
                'tema': tema_grupo,
                'fecha': str(fecha_grupo),
                'participantes': num_participantes,
                'perfil': perfil_participantes,
                'duracion': duracion_grupo,
                'facilitador': facilitador,
                'preguntas': preguntas_grupo,
                'hallazgos_positivos': hallazgos_positivos,
                'hallazgos_negativos': hallazgos_negativos,
                'recomendaciones': recomendaciones,
                'participacion': participacion_nivel,
                'satisfaccion': satisfaccion_grupo
            }
            
            st.session_state.participacion_comunitaria['grupos_focales'].append(nuevo_grupo)
            st.success("✅ Grupo focal guardado exitosamente")
            st.rerun()
    
    # Mostrar grupos focales existentes
    if st.session_state.participacion_comunitaria['grupos_focales']:
        st.subheader("📋 Grupos Focales Realizados")
        
        df_grupos = pd.DataFrame(st.session_state.participacion_comunitaria['grupos_focales'])
        
        # Métricas
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total Grupos", len(df_grupos))
        
        with col2:
            st.metric("Total Participantes", df_grupos['participantes'].sum())
        
        with col3:
            st.metric("Participación Promedio", f"{df_grupos['participacion'].mean():.1f}/5")
        
        # Gráfico de temas
        fig_temas = px.pie(
            df_grupos.groupby('tema').size().reset_index(name='count'),
            values='count',
            names='tema',
            title="Distribución por Temas"
        )
        st.plotly_chart(fig_temas, use_container_width=True)
        
        # Tabla de grupos
        st.dataframe(df_grupos[['tema', 'fecha', 'participantes', 'perfil', 'participacion', 'satisfaccion']], use_container_width=True)

def mostrar_analisis_foda():
    st.header("🔍 Análisis FODA")
    st.markdown("**Objetivo:** Identificar Fortalezas, Oportunidades, Debilidades y Amenazas del CESFAM y la comunidad.")
    
    # Formulario para agregar elementos FODA
    with st.expander("➕ Agregar Elementos FODA", expanded=True):
        categoria = st.selectbox("Categoría:", ["Fortalezas", "Oportunidades", "Debilidades", "Amenazas"], key="categoria_foda")
        
        col1, col2 = st.columns(2)
        
        with col1:
            elemento = st.text_input("Elemento:", key="elemento_foda")
            descripcion = st.text_area("Descripción:", key="descripcion_foda")
        
        with col2:
            impacto = st.selectbox("Impacto:", ["Alto", "Medio", "Bajo"], key="impacto_foda")
            prioridad = st.selectbox("Prioridad:", ["Alta", "Media", "Baja"], key="prioridad_foda")
            sector_relacionado = st.selectbox("Sector Relacionado:", ["CESFAM", "Comunidad", "Ambos"], key="sector_relacionado")
        
        if st.button("💾 Agregar Elemento", key="agregar_elemento_foda"):
            nuevo_elemento = {
                'id': len(st.session_state.participacion_comunitaria['analisis_foda'][categoria.lower()]) + 1,
                'elemento': elemento,
                'descripcion': descripcion,
                'impacto': impacto,
                'prioridad': prioridad,
                'sector': sector_relacionado
            }
            
            st.session_state.participacion_comunitaria['analisis_foda'][categoria.lower()].append(nuevo_elemento)
            st.success(f"✅ {categoria} agregada exitosamente")
            st.rerun()
    
    # Mostrar análisis FODA
    st.subheader("📊 Matriz FODA")
    
    # Crear matriz visual
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🔵 **FORTALEZAS**")
        fortalezas = st.session_state.participacion_comunitaria['analisis_foda']['fortalezas']
        if fortalezas:
            for f in fortalezas:
                with st.container():
                    st.markdown(f"**{f['elemento']}** ({f['impacto']} impacto, {f['prioridad']} prioridad)")
                    st.markdown(f"*{f['descripcion']}*")
                    st.markdown(f"📍 {f['sector']}")
                    st.markdown("---")
        else:
            st.info("No hay fortalezas registradas")
        
        st.markdown("### 🔴 **DEBILIDADES**")
        debilidades = st.session_state.participacion_comunitaria['analisis_foda']['debilidades']
        if debilidades:
            for d in debilidades:
                with st.container():
                    st.markdown(f"**{d['elemento']}** ({d['impacto']} impacto, {d['prioridad']} prioridad)")
                    st.markdown(f"*{d['descripcion']}*")
                    st.markdown(f"📍 {d['sector']}")
                    st.markdown("---")
        else:
            st.info("No hay debilidades registradas")
    
    with col2:
        st.markdown("### 🟢 **OPORTUNIDADES**")
        oportunidades = st.session_state.participacion_comunitaria['analisis_foda']['oportunidades']
        if oportunidades:
            for o in oportunidades:
                with st.container():
                    st.markdown(f"**{o['elemento']}** ({o['impacto']} impacto, {o['prioridad']} prioridad)")
                    st.markdown(f"*{o['descripcion']}*")
                    st.markdown(f"📍 {o['sector']}")
                    st.markdown("---")
        else:
            st.info("No hay oportunidades registradas")
        
        st.markdown("### 🟡 **AMENAZAS**")
        amenazas = st.session_state.participacion_comunitaria['analisis_foda']['amenazas']
        if amenazas:
            for a in amenazas:
                with st.container():
                    st.markdown(f"**{a['elemento']}** ({a['impacto']} impacto, {a['prioridad']} prioridad)")
                    st.markdown(f"*{a['descripcion']}*")
                    st.markdown(f"📍 {a['sector']}")
                    st.markdown("---")
        else:
            st.info("No hay amenazas registradas")
    
    # Gráfico de distribución FODA
    if any(st.session_state.participacion_comunitaria['analisis_foda'].values()):
        st.subheader("📈 Distribución FODA")
        
        # Contar elementos por categoría
        foda_counts = {
            'Fortalezas': len(fortalezas),
            'Oportunidades': len(oportunidades),
            'Debilidades': len(debilidades),
            'Amenazas': len(amenazas)
        }
        
        fig_foda = px.bar(
            x=list(foda_counts.keys()),
            y=list(foda_counts.values()),
            title="Cantidad de Elementos por Categoría FODA",
            color=list(foda_counts.keys()),
            color_discrete_map={
                'Fortalezas': '#1f77b4',
                'Oportunidades': '#2ca02c',
                'Debilidades': '#d62728',
                'Amenazas': '#ff7f0e'
            }
        )
        st.plotly_chart(fig_foda, use_container_width=True)

def mostrar_plan_anual():
    st.header("📋 Plan Anual de Intervenciones")
    st.markdown("**Objetivo:** Diseñar un plan anual basado en el análisis FODA y la participación comunitaria.")
    
    # Formulario para nueva intervención
    with st.expander("➕ Agregar Nueva Intervención", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            nombre_intervencion = st.text_input("Nombre de la Intervención:", key="nombre_intervencion")
            
            tipo_intervencion = st.selectbox(
                "Tipo de Intervención:",
                ["Preventiva", "Promocional", "Curativa", "Rehabilitadora", "Comunitaria"],
                key="tipo_intervencion"
            )
            
            objetivo = st.text_area("Objetivo:", key="objetivo_intervencion")
        
        with col2:
            sector_objetivo = st.selectbox(
                "Sector Objetivo:",
                ["Sector A", "Sector B", "Sector C", "Todos los Sectores"],
                key="sector_objetivo"
            )
            
            poblacion_objetivo = st.selectbox(
                "Población Objetivo:",
                ["Familias en Riesgo", "Adultos Mayores", "Mujeres", "Hombres", "Niños", "Adolescentes", "Toda la Comunidad"],
                key="poblacion_objetivo"
            )
            
            prioridad = st.selectbox("Prioridad:", ["Alta", "Media", "Baja"], key="prioridad_intervencion")
        
        # Cronograma
        st.subheader("📅 Cronograma")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            fecha_inicio = st.date_input("Fecha de Inicio:", key="fecha_inicio_intervencion")
        
        with col2:
            fecha_fin = st.date_input("Fecha de Fin:", key="fecha_fin_intervencion")
        
        with col3:
            frecuencia = st.selectbox(
                "Frecuencia:",
                ["Una vez", "Semanal", "Quincenal", "Mensual", "Trimestral", "Semestral"],
                key="frecuencia_intervencion"
            )
        
        # Recursos y responsables
        st.subheader("👥 Recursos y Responsables")
        col1, col2 = st.columns(2)
        
        with col1:
            responsable = st.text_input("Responsable Principal:", key="responsable_intervencion")
            equipo_trabajo = st.text_area("Equipo de Trabajo:", key="equipo_trabajo")
        
        with col2:
            recursos_necesarios = st.text_area("Recursos Necesarios:", key="recursos_necesarios")
            presupuesto_estimado = st.number_input("Presupuesto Estimado ($):", min_value=0, value=100000, key="presupuesto_estimado")
        
        # Indicadores
        st.subheader("📊 Indicadores de Evaluación")
        indicadores = st.text_area("Indicadores de Proceso y Resultado:", key="indicadores_intervencion")
        
        # Relación con FODA
        st.subheader("🔗 Relación con Análisis FODA")
        fortalezas_aprovechar = st.multiselect(
            "Fortalezas a Aprovechar:",
            [f['elemento'] for f in st.session_state.participacion_comunitaria['analisis_foda']['fortalezas']],
            key="fortalezas_aprovechar"
        )
        
        debilidades_superar = st.multiselect(
            "Debilidades a Superar:",
            [d['elemento'] for d in st.session_state.participacion_comunitaria['analisis_foda']['debilidades']],
            key="debilidades_superar"
        )
        
        oportunidades_aprovechar = st.multiselect(
            "Oportunidades a Aprovechar:",
            [o['elemento'] for o in st.session_state.participacion_comunitaria['analisis_foda']['oportunidades']],
            key="oportunidades_aprovechar"
        )
        
        amenazas_mitigar = st.multiselect(
            "Amenazas a Mitigar:",
            [a['elemento'] for a in st.session_state.participacion_comunitaria['analisis_foda']['amenazas']],
            key="amenazas_mitigar"
        )
        
        if st.button("💾 Guardar Intervención", key="guardar_intervencion"):
            nueva_intervencion = {
                'id': len(st.session_state.participacion_comunitaria['plan_anual']) + 1,
                'nombre': nombre_intervencion,
                'tipo': tipo_intervencion,
                'objetivo': objetivo,
                'sector': sector_objetivo,
                'poblacion': poblacion_objetivo,
                'prioridad': prioridad,
                'fecha_inicio': str(fecha_inicio),
                'fecha_fin': str(fecha_fin),
                'frecuencia': frecuencia,
                'responsable': responsable,
                'equipo': equipo_trabajo,
                'recursos': recursos_necesarios,
                'presupuesto': presupuesto_estimado,
                'indicadores': indicadores,
                'fortalezas': fortalezas_aprovechar,
                'debilidades': debilidades_superar,
                'oportunidades': oportunidades_aprovechar,
                'amenazas': amenazas_mitigar
            }
            
            st.session_state.participacion_comunitaria['plan_anual'].append(nueva_intervencion)
            st.success("✅ Intervención guardada exitosamente")
            st.rerun()
    
    # Mostrar plan anual
    if st.session_state.participacion_comunitaria['plan_anual']:
        st.subheader("📋 Plan Anual de Intervenciones")
        
        df_plan = pd.DataFrame(st.session_state.participacion_comunitaria['plan_anual'])
        
        # Métricas del plan
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Intervenciones", len(df_plan))
        
        with col2:
            st.metric("Presupuesto Total", f"${df_plan['presupuesto'].sum():,}")
        
        with col3:
            alta_prioridad = len(df_plan[df_plan['prioridad'] == 'Alta'])
            st.metric("Alta Prioridad", alta_prioridad)
        
        with col4:
            st.metric("Tipos de Intervención", df_plan['tipo'].nunique())
        
        # Gráfico de intervenciones por tipo
        fig_tipos = px.pie(
            df_plan.groupby('tipo').size().reset_index(name='count'),
            values='count',
            names='tipo',
            title="Distribución por Tipo de Intervención"
        )
        st.plotly_chart(fig_tipos, use_container_width=True)
        
        # Cronograma visual
        st.subheader("📅 Cronograma de Intervenciones")
        
        # Crear timeline
        timeline_data = []
        for _, row in df_plan.iterrows():
            timeline_data.append({
                'Intervención': row['nombre'],
                'Inicio': row['fecha_inicio'],
                'Fin': row['fecha_fin'],
                'Prioridad': row['prioridad'],
                'Tipo': row['tipo']
            })
        
        df_timeline = pd.DataFrame(timeline_data)
        df_timeline['Inicio'] = pd.to_datetime(df_timeline['Inicio'])
        df_timeline['Fin'] = pd.to_datetime(df_timeline['Fin'])
        
        # Gráfico de timeline
        fig_timeline = px.timeline(
            df_timeline,
            x_start='Inicio',
            x_end='Fin',
            y='Intervención',
            color='Prioridad',
            title="Cronograma de Intervenciones",
            color_discrete_map={
                'Alta': '#d62728',
                'Media': '#ff7f0e',
                'Baja': '#2ca02c'
            }
        )
        st.plotly_chart(fig_timeline, use_container_width=True)
        
        # Tabla detallada
        st.subheader("📊 Detalle de Intervenciones")
        st.dataframe(
            df_plan[['nombre', 'tipo', 'sector', 'poblacion', 'prioridad', 'responsable', 'presupuesto']], 
            use_container_width=True
        )
    
    # Footer
    st.markdown("---")
    st.markdown("*Aplicación educativa desarrollada por Ricardo Delannoy Suazo para formación en diagnóstico comunitario en salud familiar. © 2025. Todos los derechos reservados.*") 