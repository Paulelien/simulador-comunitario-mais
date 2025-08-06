import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
from sistema_inteligente import analizar_datos_comunidad

def mostrar_diagnostico():
    st.markdown("""
    <div class="section-header">
        <h2>🔍 Diagnóstico Familiar y Comunitario</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ### 📋 ¿Qué es el Diagnóstico Comunitario?
    
    El diagnóstico comunitario es el proceso de análisis e interpretación de la información 
    recopilada sobre las familias y la comunidad. Permite identificar problemas prioritarios, 
    recursos disponibles y oportunidades de intervención.
    """)
    
    # Verificar si hay datos suficientes
    if not st.session_state.sectores:
        st.warning("⚠️ No hay sectores registrados. Completa la sectorización primero.")
        return
    
    if not st.session_state.familias:
        st.warning("⚠️ No hay familias registradas. Completa el registro familiar primero.")
        return
    
    # Resumen ejecutivo
    st.markdown("### 📊 Resumen Ejecutivo del Diagnóstico")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_sectores = len(st.session_state.sectores)
        st.metric("Sectores", total_sectores)
    
    with col2:
        total_familias = len(st.session_state.familias)
        st.metric("Familias Registradas", total_familias)
    
    with col3:
        total_poblacion = sum(s["poblacion_total"] for s in st.session_state.sectores)
        st.metric("Población Total", f"{total_poblacion:,}")
    
    with col4:
        familias_alto_riesgo = sum(1 for f in st.session_state.familias 
                                 if f["riesgos"]["social"]["nivel"] == "Alto" or 
                                 f["riesgos"]["sanitario"]["nivel"] == "Alto")
        st.metric("Familias Alto Riesgo", familias_alto_riesgo)
    
    # Análisis por sectores
    st.markdown("### 🗺️ Análisis por Sectores")
    
    diagnostico_data = []
    for sector in st.session_state.sectores:
        sector_nombre = sector["nombre"]
        familias_sector = [f for f in st.session_state.familias if f["sector"] == sector_nombre]
        
        if familias_sector:
            # Calcular estadísticas del sector
            total_familias_sector = len(familias_sector)
            familias_alto_riesgo_sector = sum(1 for f in familias_sector 
                                            if f["riesgos"]["social"]["nivel"] == "Alto" or 
                                            f["riesgos"]["sanitario"]["nivel"] == "Alto")
            
            # Problemas más frecuentes
            problemas_frecuentes = []
            for familia in familias_sector:
                if familia["vivienda"]["hacinamiento"] == "Alto":
                    problemas_frecuentes.append("Hacinamiento")
                if familia["salud"]["violencia_intrafamiliar"]:
                    problemas_frecuentes.append("Violencia Intrafamiliar")
                if familia["salud"]["consumo_drogas"]:
                    problemas_frecuentes.append("Consumo de Drogas")
                if familia["salud"]["embarazo_adolescente"]:
                    problemas_frecuentes.append("Embarazo Adolescente")
            
            # Contar problemas
            from collections import Counter
            problemas_count = Counter(problemas_frecuentes)
            problema_principal = problemas_count.most_common(1)[0][0] if problemas_count else "Ninguno"
            
            diagnostico_data.append({
                "Sector": sector_nombre,
                "Total Familias": total_familias_sector,
                "Familias Alto Riesgo": familias_alto_riesgo_sector,
                "Porcentaje Alto Riesgo": (familias_alto_riesgo_sector / total_familias_sector) * 100,
                "Problema Principal": problema_principal,
                "Vulnerabilidad": sector["vulnerabilidad"],
                "Tipo Territorio": sector["tipo_territorio"]
            })
    
    if diagnostico_data:
        df_diagnostico = pd.DataFrame(diagnostico_data)
        
        # Mostrar tabla de diagnóstico
        st.dataframe(df_diagnostico, use_container_width=True)
        
        # Gráficos de diagnóstico
        col1, col2 = st.columns(2)
        
        with col1:
            fig_vulnerabilidad = px.bar(
                df_diagnostico,
                x="Sector",
                y="Porcentaje Alto Riesgo",
                title="Porcentaje de Familias en Alto Riesgo por Sector",
                color="Vulnerabilidad",
                color_discrete_map={"Alta": "red", "Media": "orange", "Baja": "green", "Crítica": "darkred"}
            )
            fig_vulnerabilidad.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig_vulnerabilidad, use_container_width=True)
        
        with col2:
            fig_problemas = px.bar(
                df_diagnostico,
                x="Sector",
                y="Familias Alto Riesgo",
                title="Familias en Alto Riesgo por Sector",
                color="Problema Principal",
                color_discrete_map={
                    "Hacinamiento": "orange",
                    "Violencia Intrafamiliar": "red",
                    "Consumo de Drogas": "purple",
                    "Embarazo Adolescente": "pink",
                    "Ninguno": "green"
                }
            )
            fig_problemas.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig_problemas, use_container_width=True)
    
    # Análisis de factores de riesgo
    st.markdown("### 🚨 Análisis de Factores de Riesgo")
    
    if st.session_state.familias:
        # Crear DataFrame para análisis
        familias_data = []
        for familia in st.session_state.familias:
            familias_data.append({
                "Sector": familia["sector"],
                "Apellido": familia["apellido"],
                "Riesgo Social": familia["riesgos"]["social"]["nivel"],
                "Riesgo Sanitario": familia["riesgos"]["sanitario"]["nivel"],
                "Puntaje Social": familia["riesgos"]["social"]["puntaje"],
                "Puntaje Sanitario": familia["riesgos"]["sanitario"]["puntaje"],
                "Hacinamiento": familia["vivienda"]["hacinamiento"],
                "Red Apoyo": familia["vivienda"]["red_apoyo"],
                "Participación Social": familia["vivienda"]["participacion_social"],
                "Acceso APS": familia["vivienda"]["acceso_aps"],
                "Violencia Intrafamiliar": familia["salud"]["violencia_intrafamiliar"],
                "Consumo Drogas": familia["salud"]["consumo_drogas"],
                "Embarazo Adolescente": familia["salud"]["embarazo_adolescente"],
                "Desempleo": familia["salud"]["desempleo"]
            })
        
        df_familias = pd.DataFrame(familias_data)
        
        # Análisis de correlaciones
        col1, col2 = st.columns(2)
        
        with col1:
            # Distribución de riesgos
            fig_riesgos = px.histogram(
                df_familias,
                x="Puntaje Social",
                color="Riesgo Social",
                title="Distribución de Riesgo Social",
                color_discrete_map={"Alto": "red", "Medio": "orange", "Bajo": "green"}
            )
            st.plotly_chart(fig_riesgos, use_container_width=True)
        
        with col2:
            fig_riesgo_sanitario = px.histogram(
                df_familias,
                x="Puntaje Sanitario",
                color="Riesgo Sanitario",
                title="Distribución de Riesgo Sanitario",
                color_discrete_map={"Alto": "red", "Medio": "orange", "Bajo": "green"}
            )
            st.plotly_chart(fig_riesgo_sanitario, use_container_width=True)
        
        # Análisis de problemas específicos
        st.markdown("### 📈 Análisis de Problemas Específicos")
        
        problemas_data = {
            "Problema": ["Violencia Intrafamiliar", "Consumo de Drogas", "Embarazo Adolescente", 
                        "Desempleo", "Hacinamiento Alto", "Red de Apoyo Débil"],
            "Cantidad": [
                sum(1 for f in st.session_state.familias if f["salud"]["violencia_intrafamiliar"]),
                sum(1 for f in st.session_state.familias if f["salud"]["consumo_drogas"]),
                sum(1 for f in st.session_state.familias if f["salud"]["embarazo_adolescente"]),
                sum(1 for f in st.session_state.familias if f["salud"]["desempleo"]),
                sum(1 for f in st.session_state.familias if f["vivienda"]["hacinamiento"] == "Alto"),
                sum(1 for f in st.session_state.familias if f["vivienda"]["red_apoyo"] == "Débil")
            ]
        }
        
        df_problemas = pd.DataFrame(problemas_data)
        df_problemas["Porcentaje"] = (df_problemas["Cantidad"] / len(st.session_state.familias)) * 100
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig_problemas_barras = px.bar(
                df_problemas,
                x="Problema",
                y="Cantidad",
                title="Problemas Identificados",
                color="Cantidad",
                color_continuous_scale="Reds"
            )
            fig_problemas_barras.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig_problemas_barras, use_container_width=True)
        
        with col2:
            fig_problemas_pie = px.pie(
                df_problemas,
                values="Cantidad",
                names="Problema",
                title="Distribución de Problemas"
            )
            st.plotly_chart(fig_problemas_pie, use_container_width=True)
    
    # Preguntas orientadoras para el diagnóstico
    st.markdown("### 🤔 Preguntas Orientadoras para el Diagnóstico")
    
    st.markdown("""
    **Responde estas preguntas para formular tu diagnóstico comunitario:**
    """)
    
    with st.expander("📝 Formulario de Diagnóstico", expanded=True):
        # Preguntas sobre la situación actual
        st.markdown("**1. Situación Actual de la Comunidad:**")
        
        problema_principal = st.text_area(
            "¿Cuál es el problema principal identificado en la comunidad?",
            placeholder="Describe el problema más relevante..."
        )
        
        factores_riesgo = st.multiselect(
            "¿Qué factores de riesgo son más prevalentes?",
            ["Hacinamiento", "Violencia intrafamiliar", "Consumo de drogas", 
             "Embarazo adolescente", "Desempleo", "Falta de acceso a servicios", 
             "Enfermedades crónicas", "Discriminación", "Otros"]
        )
        
        recursos_comunidad = st.text_area(
            "¿Qué recursos y fortalezas tiene la comunidad?",
            placeholder="Describe los recursos disponibles..."
        )
        
        # Preguntas sobre priorización
        st.markdown("**2. Priorización de Intervenciones:**")
        
        grupo_prioritario = st.selectbox(
            "¿Qué grupo requiere intervención prioritaria?",
            ["Familias en alto riesgo", "Adolescentes", "Adultos mayores", 
             "Personas con discapacidad", "Mujeres embarazadas", "Otros"]
        )
        
        justificacion_prioridad = st.text_area(
            "¿Por qué es prioritario este grupo?",
            placeholder="Justifica tu selección..."
        )
        
        # Preguntas sobre estrategias
        st.markdown("**3. Estrategias de Intervención:**")
        
        enfoque_intervencion = st.selectbox(
            "¿Qué enfoque de intervención es más apropiado?",
            ["Individual", "Familiar", "Comunitario", "Intersectorial", "Mixto"]
        )
        
        estrategias_propuestas = st.multiselect(
            "¿Qué estrategias propones?",
            ["Educación en salud", "Acompañamiento familiar", "Trabajo en red", 
             "Promoción de participación", "Mejora de acceso a servicios", 
             "Prevención de violencia", "Otros"]
        )
        
        # Preguntas sobre evaluación
        st.markdown("**4. Evaluación y Seguimiento:**")
        
        indicadores_evaluacion = st.multiselect(
            "¿Qué indicadores usarías para evaluar las intervenciones?",
            ["Reducción de factores de riesgo", "Mejora en acceso a servicios", 
             "Aumento de participación social", "Reducción de violencia", 
             "Mejora en condiciones de vivienda", "Otros"]
        )
        
        tiempo_intervencion = st.selectbox(
            "¿En qué plazo esperas ver resultados?",
            ["Corto plazo (3-6 meses)", "Mediano plazo (6-12 meses)", 
             "Largo plazo (1-2 años)", "Continuo"]
        )
        
        # Guardar diagnóstico
        if st.button("💾 Guardar Diagnóstico", type="primary"):
            diagnostico_completo = {
                "problema_principal": problema_principal,
                "factores_riesgo": factores_riesgo,
                "recursos_comunidad": recursos_comunidad,
                "grupo_prioritario": grupo_prioritario,
                "justificacion_prioridad": justificacion_prioridad,
                "enfoque_intervencion": enfoque_intervencion,
                "estrategias_propuestas": estrategias_propuestas,
                "indicadores_evaluacion": indicadores_evaluacion,
                "tiempo_intervencion": tiempo_intervencion,
                "fecha_diagnostico": datetime.now().strftime("%Y-%m-%d %H:%M")
            }
            
            st.session_state.diagnostico = diagnostico_completo
            st.success("✅ Diagnóstico guardado exitosamente!")
    
    # Mostrar diagnóstico guardado
    if hasattr(st.session_state, 'diagnostico') and st.session_state.diagnostico:
        st.markdown("### 📋 Diagnóstico Guardado")
        
        diagnostico = st.session_state.diagnostico
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Problema Principal:**")
            st.info(diagnostico["problema_principal"])
            
            st.markdown("**Grupo Prioritario:**")
            st.success(diagnostico["grupo_prioritario"])
            
            st.markdown("**Enfoque de Intervención:**")
            st.warning(diagnostico["enfoque_intervencion"])
        
        with col2:
            st.markdown("**Factores de Riesgo:**")
            for factor in diagnostico["factores_riesgo"]:
                st.write(f"• {factor}")
            
            st.markdown("**Estrategias Propuestas:**")
            for estrategia in diagnostico["estrategias_propuestas"]:
                st.write(f"• {estrategia}")
        
        st.markdown("**Recursos de la Comunidad:**")
        st.info(diagnostico["recursos_comunidad"])
        
        st.markdown("**Justificación de Prioridad:**")
        st.info(diagnostico["justificacion_prioridad"])
        
        st.markdown(f"**Fecha del Diagnóstico:** {diagnostico['fecha_diagnostico']}")
    
    # Recomendaciones finales
    st.markdown("### 💡 Recomendaciones para el Diagnóstico")
    
    if st.session_state.familias:
        total_familias = len(st.session_state.familias)
        familias_alto_riesgo = sum(1 for f in st.session_state.familias 
                                 if f["riesgos"]["social"]["nivel"] == "Alto" or 
                                 f["riesgos"]["sanitario"]["nivel"] == "Alto")
        
        porcentaje_alto_riesgo = (familias_alto_riesgo / total_familias) * 100
        
        if porcentaje_alto_riesgo > 30:
            st.error("🚨 **ALERTA:** Más del 30% de las familias están en alto riesgo. Se requiere intervención inmediata.")
        elif porcentaje_alto_riesgo > 15:
            st.warning("⚠️ **ATENCIÓN:** Entre 15-30% de las familias están en alto riesgo. Se requiere plan de intervención.")
        else:
            st.success("✅ **SITUACIÓN CONTROLADA:** Menos del 15% de las familias están en alto riesgo.")
        
        # Recomendaciones específicas
        st.markdown("**Recomendaciones específicas:**")
        
        if sum(1 for f in st.session_state.familias if f["salud"]["violencia_intrafamiliar"]) > 0:
            st.error("• Implementar protocolos de detección y derivación de violencia intrafamiliar")
        
        if sum(1 for f in st.session_state.familias if f["vivienda"]["hacinamiento"] == "Alto") > 0:
            st.warning("• Trabajar con servicios de vivienda para mejorar condiciones habitacionales")
        
        if sum(1 for f in st.session_state.familias if f["salud"]["consumo_drogas"]) > 0:
            st.error("• Establecer alianzas con programas de tratamiento de adicciones")
        
        if sum(1 for f in st.session_state.familias if f["vivienda"]["red_apoyo"] == "Débil") > 0:
            st.info("• Fortalecer redes de apoyo comunitario")
    
    # Dashboard Inteligente
    st.markdown("---")
    st.markdown("### 🤖 Dashboard Inteligente")
    
    if st.button("🔄 Actualizar Análisis Inteligente", key="actualizar_dashboard"):
        with st.spinner("Analizando datos en tiempo real..."):
            diagnostico_inteligente = analizar_datos_comunidad()
            
            # Métricas inteligentes
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                total_problemas = len(diagnostico_inteligente['problemas_prioritarios'])
                st.metric("Problemas Prioritarios", total_problemas)
            
            with col2:
                total_vulnerables = len(diagnostico_inteligente['poblaciones_vulnerables'])
                st.metric("Poblaciones Vulnerables", total_vulnerables)
            
            with col3:
                total_fortalezas = len(set(diagnostico_inteligente['fortalezas_comunitarias']))
                st.metric("Fortalezas Identificadas", total_fortalezas)
            
            with col4:
                total_recursos = len(diagnostico_inteligente['recursos_disponibles'])
                st.metric("Recursos Disponibles", total_recursos)
            
            # Alertas inteligentes
            st.subheader("🚨 Alertas Inteligentes")
            
            if diagnostico_inteligente['problemas_prioritarios']:
                st.error("**ALERTA CRÍTICA:** Se identificaron problemas prioritarios que requieren intervención inmediata")
                for problema in diagnostico_inteligente['problemas_prioritarios']:
                    st.write(f"• **{problema['problema'].title()}**: {problema['cantidad']} familias afectadas ({problema['porcentaje']:.1f}%)")
            else:
                st.success("✅ **SITUACIÓN ESTABLE:** No se identificaron problemas prioritarios")
            
            if diagnostico_inteligente['poblaciones_vulnerables']:
                st.warning("**ATENCIÓN:** Poblaciones vulnerables identificadas")
                for poblacion in diagnostico_inteligente['poblaciones_vulnerables']:
                    st.write(f"• {poblacion}")
            
            # Oportunidades de intervención
            if diagnostico_inteligente['fortalezas_comunitarias']:
                st.subheader("💪 Oportunidades de Intervención")
                st.success("**Fortalezas comunitarias que pueden potenciarse:**")
                for fortaleza in set(diagnostico_inteligente['fortalezas_comunitarias']):
                    st.write(f"• {fortaleza}")
            
            if diagnostico_inteligente['recursos_disponibles']:
                st.info("**Recursos disponibles para alianzas:**")
                for recurso in diagnostico_inteligente['recursos_disponibles']:
                    st.write(f"• {recurso}")
            
            # Recomendaciones automáticas
            st.subheader("🎯 Recomendaciones Automáticas")
            
            if diagnostico_inteligente['problemas_prioritarios']:
                st.info("**Acciones recomendadas:**")
                
                for problema in diagnostico_inteligente['problemas_prioritarios']:
                    if problema['problema'] == 'diabetes':
                        st.write("• Implementar programa de educación diabetológica")
                        st.write("• Establecer grupos de apoyo para diabéticos")
                    elif problema['problema'] == 'hipertension':
                        st.write("• Crear programa de control de presión arterial")
                        st.write("• Talleres de reducción de sodio")
                    elif problema['problema'] == 'obesidad':
                        st.write("• Programa de actividad física comunitaria")
                        st.write("• Talleres de nutrición")
                    elif problema['problema'] == 'violencia_intrafamiliar':
                        st.write("• Protocolos de detección temprana")
                        st.write("• Talleres de resolución pacífica de conflictos")
                    elif problema['problema'] == 'consumo_drogas':
                        st.write("• Programa de prevención en colegios")
                        st.write("• Actividades deportivas y recreativas")
                    elif problema['problema'] == 'embarazo_adolescente':
                        st.write("• Educación sexual integral")
                        st.write("• Acceso a métodos anticonceptivos")
                    elif problema['problema'] == 'hacinamiento':
                        st.write("• Gestión de subsidios habitacionales")
                        st.write("• Asesoría en mejoras habitacionales")
                    elif problema['problema'] == 'desempleo':
                        st.write("• Programa de capacitación laboral")
                        st.write("• Talleres de emprendimiento")
                    elif problema['problema'] == 'baja_escolaridad':
                        st.write("• Programa de alfabetización")
                        st.write("• Apoyo escolar")
                    elif problema['problema'] == 'acceso_salud':
                        st.write("• Transporte comunitario a centros de salud")
                        st.write("• Atención domiciliaria")
            
            # Botón para generar plan automático
            if st.button("📋 Generar Plan de Intervención Automático", key="generar_plan_auto"):
                st.success("✅ Plan generado automáticamente. Revisa el módulo 'Plan Anual' para ver las sugerencias.")
                st.info("💡 **Tip:** Usa el botón 'Generar Sugerencias Inteligentes' en el módulo de Plan Anual para obtener intervenciones específicas.") 