import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, date, timedelta

def mostrar_plan_intervencion():
    st.markdown("""
    <div class="section-header">
        <h2>📋 Plan de Intervención</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ### 🎯 ¿Qué es el Plan de Intervención?
    
    El plan de intervención es la estrategia organizada para abordar los problemas 
    identificados en el diagnóstico comunitario. Incluye objetivos específicos, 
    actividades concretas, responsables, plazos e indicadores de evaluación.
    """)
    
    # Verificar si hay diagnóstico previo
    if not hasattr(st.session_state, 'diagnostico') or not st.session_state.diagnostico:
        st.warning("⚠️ Primero debes completar el diagnóstico comunitario.")
        st.info("Ve a la sección '🔍 Diagnóstico' para formular tu diagnóstico antes de continuar.")
        return
    
    # Mostrar resumen del diagnóstico
    st.markdown("### 📊 Resumen del Diagnóstico")
    
    diagnostico = st.session_state.diagnostico
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Problema Principal:**")
        st.info(diagnostico["problema_principal"])
        
        st.markdown("**Grupo Prioritario:**")
        st.success(diagnostico["grupo_prioritario"])
    
    with col2:
        st.markdown("**Enfoque de Intervención:**")
        st.warning(diagnostico["enfoque_intervencion"])
        
        st.markdown("**Estrategias Propuestas:**")
        for estrategia in diagnostico["estrategias_propuestas"]:
            st.write(f"• {estrategia}")
    
    # Formulario para crear plan de intervención
    with st.expander("➕ Crear Actividad de Intervención", expanded=True):
        st.markdown("**Información General de la Actividad:**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            nombre_actividad = st.text_input("Nombre de la Actividad", placeholder="Ej: Taller de Prevención de Violencia")
            tipo_actividad = st.selectbox(
                "Tipo de Actividad",
                ["Educativa", "Preventiva", "Promocional", "Asistencial", "Organizacional", "Otro"]
            )
            
            objetivo_general = st.text_area(
                "Objetivo General",
                placeholder="¿Qué se busca lograr con esta actividad?"
            )
        
        with col2:
            sector_objetivo = st.multiselect(
                "Sectores Objetivo",
                [s["nombre"] for s in st.session_state.sectores] if st.session_state.sectores else []
            )
            
            poblacion_objetivo = st.multiselect(
                "Población Objetivo",
                ["Familias en alto riesgo", "Adolescentes", "Adultos mayores", 
                 "Mujeres", "Hombres", "Niños", "Población general"]
            )
        
        # Objetivos específicos
        st.markdown("**Objetivos Específicos:**")
        
        # Inicializar contadores si no existen
        if 'num_objetivos' not in st.session_state:
            st.session_state.num_objetivos = 1
        if 'num_actividades' not in st.session_state:
            st.session_state.num_actividades = 1
        
        objetivos_especificos = []
        
        # Mostrar objetivos existentes
        for i in range(st.session_state.num_objetivos):
            objetivo = st.text_input(
                f"Objetivo Específico {i+1}",
                placeholder=f"Objetivo específico {i+1}...",
                key=f"objetivo_{i}"
            )
            if objetivo:
                objetivos_especificos.append(objetivo)
        
        # Botón para agregar objetivo
        col1, col2 = st.columns([1, 4])
        with col1:
            if st.button("➕ Agregar Objetivo", key="agregar_objetivo"):
                st.session_state.num_objetivos += 1
                st.rerun()
        
        with col2:
            if st.session_state.num_objetivos > 1:
                if st.button("➖ Quitar Último Objetivo", key="quitar_objetivo"):
                    st.session_state.num_objetivos -= 1
                    st.rerun()
        
        # Actividades específicas
        st.markdown("**Actividades Específicas:**")
        actividades_especificas = []
        
        # Mostrar actividades existentes
        for i in range(st.session_state.num_actividades):
            actividad = st.text_input(
                f"Actividad {i+1}",
                placeholder=f"Descripción de la actividad {i+1}...",
                key=f"actividad_{i}"
            )
            if actividad:
                actividades_especificas.append(actividad)
        
        # Botón para agregar actividad
        col1, col2 = st.columns([1, 4])
        with col1:
            if st.button("➕ Agregar Actividad", key="agregar_actividad"):
                st.session_state.num_actividades += 1
                st.rerun()
        
        with col2:
            if st.session_state.num_actividades > 1:
                if st.button("➖ Quitar Última Actividad", key="quitar_actividad"):
                    st.session_state.num_actividades -= 1
                    st.rerun()
        
        # Responsables y recursos
        st.markdown("**Responsables y Recursos:**")
        col1, col2 = st.columns(2)
        
        with col1:
            responsables = st.multiselect(
                "Responsables",
                ["TENS", "Enfermera", "Médico", "Psicólogo", "Matrona", 
                 "Trabajador Social", "Otros profesionales", "Voluntarios"]
            )
            
            instituciones_participantes = st.multiselect(
                "Instituciones Participantes",
                [i["nombre"] for i in st.session_state.instituciones] if st.session_state.instituciones else []
            )
        
        with col2:
            recursos_necesarios = st.multiselect(
                "Recursos Necesarios",
                ["Material educativo", "Espacios físicos", "Equipamiento", 
                 "Personal especializado", "Presupuesto", "Transporte", "Otros"]
            )
            
            presupuesto_estimado = st.number_input(
                "Presupuesto Estimado ($)",
                min_value=0,
                value=0,
                step=1000
            )
        
        # Cronograma
        st.markdown("**Cronograma:**")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            fecha_inicio = st.date_input("Fecha de Inicio", value=date.today())
        
        with col2:
            fecha_fin = st.date_input("Fecha de Término", value=date.today() + timedelta(days=30))
        
        with col3:
            frecuencia = st.selectbox(
                "Frecuencia",
                ["Una vez", "Semanal", "Quincenal", "Mensual", "Bimestral", "Otro"]
            )
        
        # Indicadores de evaluación
        st.markdown("**Indicadores de Evaluación:**")
        
        # Inicializar contador de indicadores si no existe
        if 'num_indicadores' not in st.session_state:
            st.session_state.num_indicadores = 1
        
        indicadores = []
        
        # Mostrar indicadores existentes
        for i in range(st.session_state.num_indicadores):
            indicador = st.text_input(
                f"Indicador {i+1}",
                placeholder=f"Indicador de evaluación {i+1}...",
                key=f"indicador_{i}"
            )
            if indicador:
                indicadores.append(indicador)
        
        # Botón para agregar indicador
        col1, col2 = st.columns([1, 4])
        with col1:
            if st.button("➕ Agregar Indicador", key="agregar_indicador"):
                st.session_state.num_indicadores += 1
                st.rerun()
        
        with col2:
            if st.session_state.num_indicadores > 1:
                if st.button("➖ Quitar Último Indicador", key="quitar_indicador"):
                    st.session_state.num_indicadores -= 1
                    st.rerun()
        
        # Metas
        st.markdown("**Metas:**")
        col1, col2 = st.columns(2)
        
        with col1:
            meta_cuantitativa = st.text_input(
                "Meta Cuantitativa",
                placeholder="Ej: 50 familias participarán en el taller"
            )
        
        with col2:
            meta_cualitativa = st.text_input(
                "Meta Cualitativa",
                placeholder="Ej: Mejorar el conocimiento sobre prevención"
            )
        
        # Riesgos y contingencias
        st.markdown("**Riesgos y Contingencias:**")
        riesgos_contingencias = st.text_area(
            "Identifica posibles riesgos y cómo manejarlos",
            placeholder="Riesgos identificados y medidas de contingencia..."
        )
        
        # Botones de acción
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("💾 Guardar Actividad", type="primary"):
                if nombre_actividad and objetivo_general:
                    nueva_actividad = {
                        "nombre": nombre_actividad,
                        "tipo": tipo_actividad,
                        "objetivo_general": objetivo_general,
                        "sectores_objetivo": sector_objetivo,
                        "poblacion_objetivo": poblacion_objetivo,
                        "objetivos_especificos": objetivos_especificos,
                        "actividades_especificas": actividades_especificas,
                        "responsables": responsables,
                        "instituciones_participantes": instituciones_participantes,
                        "recursos_necesarios": recursos_necesarios,
                        "presupuesto_estimado": presupuesto_estimado,
                        "cronograma": {
                            "fecha_inicio": fecha_inicio.strftime("%Y-%m-%d"),
                            "fecha_fin": fecha_fin.strftime("%Y-%m-%d"),
                            "frecuencia": frecuencia
                        },
                        "indicadores": indicadores,
                        "metas": {
                            "cuantitativa": meta_cuantitativa,
                            "cualitativa": meta_cualitativa
                        },
                        "riesgos_contingencias": riesgos_contingencias,
                        "fecha_creacion": datetime.now().strftime("%Y-%m-%d %H:%M"),
                        "estado": "Planificada"
                    }
                    
                    st.session_state.plan_intervencion.append(nueva_actividad)
                    st.success(f"✅ Actividad '{nombre_actividad}' agregada al plan de intervención!")
                    
                    # Resetear contadores después de guardar
                    st.session_state.num_objetivos = 1
                    st.session_state.num_actividades = 1
                    st.session_state.num_indicadores = 1
                    
                    st.rerun()
                else:
                    st.error("❌ Por favor completa los campos obligatorios (nombre y objetivo general)")
        
        with col2:
            if st.button("🧹 Limpiar Formulario", type="secondary"):
                # Resetear contadores
                st.session_state.num_objetivos = 1
                st.session_state.num_actividades = 1
                st.session_state.num_indicadores = 1
                st.rerun()
    
    # Mostrar plan de intervención
    if st.session_state.plan_intervencion:
        st.markdown("### 📋 Plan de Intervención Completo")
        
        # Crear DataFrame para visualización
        plan_data = []
        for actividad in st.session_state.plan_intervencion:
            plan_data.append({
                "Actividad": actividad["nombre"],
                "Tipo": actividad["tipo"],
                "Objetivo General": actividad["objetivo_general"][:50] + "..." if len(actividad["objetivo_general"]) > 50 else actividad["objetivo_general"],
                "Sectores": ", ".join(actividad["sectores_objetivo"]) if actividad["sectores_objetivo"] else "Todos",
                "Población": ", ".join(actividad["poblacion_objetivo"]) if actividad["poblacion_objetivo"] else "General",
                "Responsables": ", ".join(actividad["responsables"]) if actividad["responsables"] else "No especificado",
                "Presupuesto": f"${actividad['presupuesto_estimado']:,}",
                "Fecha Inicio": actividad["cronograma"]["fecha_inicio"],
                "Fecha Fin": actividad["cronograma"]["fecha_fin"],
                "Frecuencia": actividad["cronograma"]["frecuencia"],
                "Estado": actividad["estado"]
            })
        
        df_plan = pd.DataFrame(plan_data)
        
        # Filtros
        col1, col2, col3 = st.columns(3)
        
        with col1:
            tipo_filtro = st.selectbox(
                "Filtrar por Tipo",
                ["Todos"] + list(df_plan["Tipo"].unique())
            )
        
        with col2:
            estado_filtro = st.selectbox(
                "Filtrar por Estado",
                ["Todos"] + list(df_plan["Estado"].unique())
            )
        
        with col3:
            sector_filtro = st.selectbox(
                "Filtrar por Sector",
                ["Todos"] + list(set([s for s in df_plan["Sectores"].unique() if s != "Todos"]))
            )
        
        # Aplicar filtros
        df_filtrado = df_plan.copy()
        
        if tipo_filtro != "Todos":
            df_filtrado = df_filtrado[df_filtrado["Tipo"] == tipo_filtro]
        
        if estado_filtro != "Todos":
            df_filtrado = df_filtrado[df_filtrado["Estado"] == estado_filtro]
        
        if sector_filtro != "Todos":
            df_filtrado = df_filtrado[df_filtrado["Sectores"].str.contains(sector_filtro, na=False)]
        
        # Mostrar tabla filtrada
        st.dataframe(
            df_filtrado[["Actividad", "Tipo", "Sectores", "Población", "Responsables", 
                        "Presupuesto", "Fecha Inicio", "Fecha Fin", "Estado"]],
            use_container_width=True
        )
        
        # Gráficos del plan
        col1, col2 = st.columns(2)
        
        with col1:
            # Gráfico por tipo de actividad
            fig_tipo = px.pie(
                df_plan,
                names="Tipo",
                title="Distribución por Tipo de Actividad"
            )
            st.plotly_chart(fig_tipo, use_container_width=True)
        
        with col2:
            # Gráfico de presupuesto
            df_plan_numeric = df_plan.copy()
            df_plan_numeric["Presupuesto_Numeric"] = df_plan_numeric["Presupuesto"].str.replace("$", "").str.replace(",", "").astype(float)
            
            fig_presupuesto = px.bar(
                df_plan_numeric,
                x="Actividad",
                y="Presupuesto_Numeric",
                title="Presupuesto por Actividad",
                labels={"Presupuesto_Numeric": "Presupuesto ($)"}
            )
            fig_presupuesto.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig_presupuesto, use_container_width=True)
        
        # Cronograma visual
        st.markdown("### 📅 Cronograma de Actividades")
        
        # Crear gráfico de Gantt simple
        fig_gantt = go.Figure()
        
        for i, actividad in enumerate(st.session_state.plan_intervencion):
            fecha_inicio = datetime.strptime(actividad["cronograma"]["fecha_inicio"], "%Y-%m-%d")
            fecha_fin = datetime.strptime(actividad["cronograma"]["fecha_fin"], "%Y-%m-%d")
            
            fig_gantt.add_trace(go.Bar(
                name=actividad["nombre"],
                x=[(fecha_fin - fecha_inicio).days],
                y=[actividad["nombre"]],
                orientation='h',
                text=f"{actividad['cronograma']['fecha_inicio']} - {actividad['cronograma']['fecha_fin']}",
                textposition='auto',
                hovertemplate=f"<b>{actividad['nombre']}</b><br>" +
                             f"Inicio: {actividad['cronograma']['fecha_inicio']}<br>" +
                             f"Fin: {actividad['cronograma']['fecha_fin']}<br>" +
                             f"Frecuencia: {actividad['cronograma']['frecuencia']}<extra></extra>"
            ))
        
        fig_gantt.update_layout(
            title="Cronograma de Actividades",
            xaxis_title="Duración (días)",
            yaxis_title="Actividades",
            height=400
        )
        
        st.plotly_chart(fig_gantt, use_container_width=True)
        
        # Resumen ejecutivo del plan
        st.markdown("### 📊 Resumen Ejecutivo del Plan")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            total_actividades = len(st.session_state.plan_intervencion)
            st.metric("Total Actividades", total_actividades)
        
        with col2:
            total_presupuesto = sum(a["presupuesto_estimado"] for a in st.session_state.plan_intervencion)
            st.metric("Presupuesto Total", f"${total_presupuesto:,}")
        
        with col3:
            actividades_educativas = len([a for a in st.session_state.plan_intervencion if a["tipo"] == "Educativa"])
            st.metric("Actividades Educativas", actividades_educativas)
        
        with col4:
            actividades_preventivas = len([a for a in st.session_state.plan_intervencion if a["tipo"] == "Preventiva"])
            st.metric("Actividades Preventivas", actividades_preventivas)
        
        # Análisis de cobertura
        st.markdown("### 🎯 Análisis de Cobertura del Plan")
        
        # Verificar cobertura de sectores
        sectores_plan = set()
        for actividad in st.session_state.plan_intervencion:
            sectores_plan.update(actividad["sectores_objetivo"])
        
        sectores_totales = set(s["nombre"] for s in st.session_state.sectores)
        sectores_sin_cobertura = sectores_totales - sectores_plan
        
        if sectores_sin_cobertura:
            st.warning(f"⚠️ **Sectores sin cobertura en el plan:** {', '.join(sectores_sin_cobertura)}")
        else:
            st.success("✅ **Todos los sectores tienen cobertura en el plan**")
        
        # Verificar población objetivo
        poblacion_plan = set()
        for actividad in st.session_state.plan_intervencion:
            poblacion_plan.update(actividad["poblacion_objetivo"])
        
        st.info(f"**Población objetivo cubierta:** {', '.join(poblacion_plan)}")
        
        # Verificar recursos
        recursos_plan = set()
        for actividad in st.session_state.plan_intervencion:
            recursos_plan.update(actividad["recursos_necesarios"])
        
        st.info(f"**Recursos necesarios:** {', '.join(recursos_plan)}")
        
        # Recomendaciones finales
        st.markdown("### 💡 Recomendaciones para el Plan")
        
        if total_actividades < 3:
            st.warning("• Considerar agregar más actividades para una intervención integral")
        
        if total_presupuesto == 0:
            st.info("• Evaluar si se requieren recursos presupuestarios para las actividades")
        
        if not any("TENS" in a["responsables"] for a in st.session_state.plan_intervencion):
            st.info("• Considerar incluir TENS como responsables en algunas actividades")
        
        if not any("Familias en alto riesgo" in a["poblacion_objetivo"] for a in st.session_state.plan_intervencion):
            st.warning("• Verificar que las familias en alto riesgo estén incluidas en las actividades")
    
    else:
        st.info("📝 No hay actividades en el plan de intervención. Crea actividades usando el formulario de arriba.")
    
    # Botón para limpiar datos
    if st.session_state.plan_intervencion:
        if st.button("🗑️ Limpiar Todo el Plan"):
            st.session_state.plan_intervencion = []
            st.success("✅ Todo el plan de intervención ha sido eliminado")
            st.rerun() 