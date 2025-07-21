import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import numpy as np

def mostrar_epidemiologia():
    st.title("🦠 Epidemiología Comunitaria")
    st.markdown("---")
    
    # Inicializar session state
    if 'epidemiologia' not in st.session_state:
        st.session_state.epidemiologia = {
            'indicadores_basicos': [],
            'patologias_prioritarias': [],
            'vigilancia_epidemiologica': [],
            'factores_riesgo': [],
            'analisis_geografico': []
        }
    
    # Tabs para organizar las secciones
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📊 Indicadores Básicos", 
        "🏥 Patologías Prioritarias", 
        "📅 Vigilancia Epidemiológica", 
        "🎯 Factores de Riesgo",
        "🗺️ Análisis Geográfico"
    ])
    
    with tab1:
        mostrar_indicadores_basicos()
    
    with tab2:
        mostrar_patologias_prioritarias()
    
    with tab3:
        mostrar_vigilancia_epidemiologica()
    
    with tab4:
        mostrar_factores_riesgo()
    
    with tab5:
        mostrar_analisis_geografico()

def mostrar_indicadores_basicos():
    st.header("📊 Indicadores Epidemiológicos Básicos")
    st.markdown("**Objetivo:** Calcular y analizar indicadores fundamentales de salud comunitaria.")
    
    # Formulario para nuevos indicadores
    with st.expander("➕ Agregar Nuevos Indicadores", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            tipo_indicador = st.selectbox(
                "Tipo de Indicador:",
                ["Morbilidad", "Mortalidad", "Demográfico", "Otro"],
                key="tipo_indicador"
            )
            
            fecha_registro = st.date_input("Fecha de Registro:", key="fecha_registro_epi")
            
            sector_indicador = st.selectbox(
                "Sector:",
                ["Sector A", "Sector B", "Sector C", "Todos los Sectores"],
                key="sector_indicador"
            )
        
        with col2:
            periodo_analisis = st.selectbox(
                "Período de Análisis:",
                ["Último mes", "Último trimestre", "Último semestre", "Último año"],
                key="periodo_analisis"
            )
            
            fuente_datos = st.selectbox(
                "Fuente de Datos:",
                ["Fichas clínicas", "Sistema de información", "Encuesta comunitaria", "Otro"],
                key="fuente_datos"
            )
        
        # Datos específicos según tipo de indicador
        st.subheader("📋 Datos del Indicador")
        
        if tipo_indicador == "Morbilidad":
            col1, col2, col3 = st.columns(3)
            
            with col1:
                casos_nuevos = st.number_input("Casos Nuevos:", min_value=0, value=50, key="casos_nuevos")
                casos_existentes = st.number_input("Casos Existentes:", min_value=0, value=120, key="casos_existentes")
            
            with col2:
                poblacion_riesgo = st.number_input("Población en Riesgo:", min_value=0, value=1000, key="poblacion_riesgo")
                periodo_tiempo = st.number_input("Período (días):", min_value=1, value=30, key="periodo_tiempo")
            
            with col3:
                # Cálculos automáticos
                if poblacion_riesgo > 0:
                    incidencia = (casos_nuevos / poblacion_riesgo) * 1000
                    prevalencia = (casos_existentes / poblacion_riesgo) * 1000
                    
                    st.metric("Incidencia (por 1000 hab.)", f"{incidencia:.1f}")
                    st.metric("Prevalencia (por 1000 hab.)", f"{prevalencia:.1f}")
        
        elif tipo_indicador == "Mortalidad":
            col1, col2, col3 = st.columns(3)
            
            with col1:
                defunciones = st.number_input("Defunciones:", min_value=0, value=5, key="defunciones")
                poblacion_total = st.number_input("Población Total:", min_value=0, value=1000, key="poblacion_total")
            
            with col2:
                causas_principales = st.multiselect(
                    "Causas Principales:",
                    ["Enfermedades cardiovasculares", "Cáncer", "Accidentes", "Enfermedades respiratorias", "Diabetes", "Otro"],
                    key="causas_principales"
                )
            
            with col3:
                if poblacion_total > 0:
                    tasa_mortalidad = (defunciones / poblacion_total) * 1000
                    st.metric("Tasa de Mortalidad (por 1000 hab.)", f"{tasa_mortalidad:.1f}")
        
        elif tipo_indicador == "Demográfico":
            col1, col2 = st.columns(2)
            
            with col1:
                poblacion_total = st.number_input("Población Total:", min_value=0, value=1000, key="poblacion_total_demo")
                menores_15 = st.number_input("Menores de 15 años:", min_value=0, value=200, key="menores_15")
                mayores_65 = st.number_input("Mayores de 65 años:", min_value=0, value=150, key="mayores_65")
            
            with col2:
                if poblacion_total > 0:
                    indice_dependencia = ((menores_15 + mayores_65) / poblacion_total) * 100
                    st.metric("Índice de Dependencia (%)", f"{indice_dependencia:.1f}")
        
        observaciones = st.text_area("Observaciones:", key="observaciones_indicador")
        
        if st.button("💾 Guardar Indicador", key="guardar_indicador"):
            nuevo_indicador = {
                'id': len(st.session_state.epidemiologia['indicadores_basicos']) + 1,
                'tipo': tipo_indicador,
                'fecha': str(fecha_registro),
                'sector': sector_indicador,
                'periodo': periodo_analisis,
                'fuente': fuente_datos,
                'observaciones': observaciones
            }
            
            # Agregar datos específicos según tipo
            if tipo_indicador == "Morbilidad":
                nuevo_indicador.update({
                    'casos_nuevos': casos_nuevos,
                    'casos_existentes': casos_existentes,
                    'poblacion_riesgo': poblacion_riesgo,
                    'incidencia': incidencia if 'incidencia' in locals() else 0,
                    'prevalencia': prevalencia if 'prevalencia' in locals() else 0
                })
            elif tipo_indicador == "Mortalidad":
                nuevo_indicador.update({
                    'defunciones': defunciones,
                    'poblacion_total': poblacion_total,
                    'tasa_mortalidad': tasa_mortalidad if 'tasa_mortalidad' in locals() else 0,
                    'causas': causas_principales
                })
            elif tipo_indicador == "Demográfico":
                nuevo_indicador.update({
                    'poblacion_total': poblacion_total,
                    'menores_15': menores_15,
                    'mayores_65': mayores_65,
                    'indice_dependencia': indice_dependencia if 'indice_dependencia' in locals() else 0
                })
            
            st.session_state.epidemiologia['indicadores_basicos'].append(nuevo_indicador)
            st.success("✅ Indicador guardado exitosamente")
            st.rerun()
    
    # Mostrar indicadores existentes
    if st.session_state.epidemiologia['indicadores_basicos']:
        st.subheader("📋 Indicadores Registrados")
        
        df_indicadores = pd.DataFrame(st.session_state.epidemiologia['indicadores_basicos'])
        
        # Métricas generales
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Indicadores", len(df_indicadores))
        
        with col2:
            morbilidad_count = len(df_indicadores[df_indicadores['tipo'] == 'Morbilidad'])
            st.metric("Indicadores Morbilidad", morbilidad_count)
        
        with col3:
            mortalidad_count = len(df_indicadores[df_indicadores['tipo'] == 'Mortalidad'])
            st.metric("Indicadores Mortalidad", mortalidad_count)
        
        with col4:
            demografico_count = len(df_indicadores[df_indicadores['tipo'] == 'Demográfico'])
            st.metric("Indicadores Demográficos", demografico_count)
        
        # Gráfico de distribución por tipo
        fig_tipos = px.pie(
            df_indicadores.groupby('tipo').size().reset_index(name='count'),
            values='count',
            names='tipo',
            title="Distribución de Indicadores por Tipo"
        )
        st.plotly_chart(fig_tipos, use_container_width=True)
        
        # Tabla de indicadores
        st.dataframe(df_indicadores[['tipo', 'fecha', 'sector', 'periodo']], use_container_width=True)

def mostrar_patologias_prioritarias():
    st.header("🏥 Análisis de Patologías Prioritarias")
    st.markdown("**Objetivo:** Identificar y analizar las principales patologías de la comunidad.")
    
    # Formulario para nueva patología
    with st.expander("➕ Agregar Nueva Patología", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            patologia = st.selectbox(
                "Patología:",
                ["Diabetes Mellitus", "Hipertensión Arterial", "Obesidad", "EPOC", "Asma", 
                 "Depresión", "Ansiedad", "Embarazo Adolescente", "Obesidad Infantil", "Otro"],
                key="patologia_prioritaria"
            )
            
            fecha_analisis = st.date_input("Fecha de Análisis:", key="fecha_analisis_patologia")
            
            sector_patologia = st.selectbox(
                "Sector:",
                ["Sector A", "Sector B", "Sector C", "Todos los Sectores"],
                key="sector_patologia"
            )
        
        with col2:
            nivel_prioridad = st.selectbox(
                "Nivel de Prioridad:",
                ["Alta", "Media", "Baja"],
                key="nivel_prioridad"
            )
            
            tendencia = st.selectbox(
                "Tendencia:",
                ["En aumento", "Estable", "En disminución"],
                key="tendencia_patologia"
            )
        
        # Datos epidemiológicos
        st.subheader("📊 Datos Epidemiológicos")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            casos_activos = st.number_input("Casos Activos:", min_value=0, value=25, key="casos_activos")
            casos_nuevos_mes = st.number_input("Casos Nuevos (último mes):", min_value=0, value=5, key="casos_nuevos_mes")
        
        with col2:
            poblacion_afectada = st.number_input("Población Afectada:", min_value=0, value=1000, key="poblacion_afectada")
            edad_promedio = st.number_input("Edad Promedio:", min_value=0, value=45, key="edad_promedio")
        
        with col3:
            # Cálculos automáticos
            if poblacion_afectada > 0:
                prevalencia_patologia = (casos_activos / poblacion_afectada) * 1000
                incidencia_mensual = (casos_nuevos_mes / poblacion_afectada) * 1000
                
                st.metric("Prevalencia (por 1000 hab.)", f"{prevalencia_patologia:.1f}")
                st.metric("Incidencia Mensual (por 1000 hab.)", f"{incidencia_mensual:.1f}")
        
        # Factores asociados
        st.subheader("🔗 Factores Asociados")
        factores_asociados = st.multiselect(
            "Factores de Riesgo Identificados:",
            ["Obesidad", "Sedentarismo", "Tabaquismo", "Alcoholismo", "Mala alimentación", 
             "Estrés", "Pobreza", "Bajo nivel educacional", "Otro"],
            key="factores_asociados"
        )
        
        # Intervenciones recomendadas
        st.subheader("💡 Intervenciones Recomendadas")
        intervenciones = st.multiselect(
            "Intervenciones Sugeridas:",
            ["Educación en salud", "Screening poblacional", "Programa de ejercicio", 
             "Control nutricional", "Apoyo psicológico", "Coordinación con especialistas", "Otro"],
            key="intervenciones_patologia"
        )
        
        observaciones = st.text_area("Observaciones:", key="observaciones_patologia")
        
        if st.button("💾 Guardar Patología", key="guardar_patologia"):
            nueva_patologia = {
                'id': len(st.session_state.epidemiologia['patologias_prioritarias']) + 1,
                'patologia': patologia,
                'fecha': str(fecha_analisis),
                'sector': sector_patologia,
                'prioridad': nivel_prioridad,
                'tendencia': tendencia,
                'casos_activos': casos_activos,
                'casos_nuevos': casos_nuevos_mes,
                'poblacion': poblacion_afectada,
                'edad_promedio': edad_promedio,
                'prevalencia': prevalencia_patologia if 'prevalencia_patologia' in locals() else 0,
                'incidencia_mensual': incidencia_mensual if 'incidencia_mensual' in locals() else 0,
                'factores_asociados': factores_asociados,
                'intervenciones': intervenciones,
                'observaciones': observaciones
            }
            
            st.session_state.epidemiologia['patologias_prioritarias'].append(nueva_patologia)
            st.success("✅ Patología guardada exitosamente")
            st.rerun()
    
    # Mostrar patologías existentes
    if st.session_state.epidemiologia['patologias_prioritarias']:
        st.subheader("📋 Patologías Prioritarias Registradas")
        
        df_patologias = pd.DataFrame(st.session_state.epidemiologia['patologias_prioritarias'])
        
        # Métricas
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total Patologías", len(df_patologias))
        
        with col2:
            alta_prioridad = len(df_patologias[df_patologias['prioridad'] == 'Alta'])
            st.metric("Alta Prioridad", alta_prioridad)
        
        with col3:
            en_aumento = len(df_patologias[df_patologias['tendencia'] == 'En aumento'])
            st.metric("En Aumento", en_aumento)
        
        # Gráfico de prevalencia por patología
        if 'prevalencia' in df_patologias.columns:
            fig_prevalencia = px.bar(
                df_patologias,
                x='patologia',
                y='prevalencia',
                color='prioridad',
                title="Prevalencia por Patología",
                labels={'prevalencia': 'Prevalencia (por 1000 hab.)', 'patologia': 'Patología'}
            )
            st.plotly_chart(fig_prevalencia, use_container_width=True)
        
        # Tabla de patologías
        st.dataframe(df_patologias[['patologia', 'sector', 'prioridad', 'tendencia', 'casos_activos', 'prevalencia']], use_container_width=True)

def mostrar_vigilancia_epidemiologica():
    st.header("📅 Vigilancia Epidemiológica")
    st.markdown("**Objetivo:** Monitorear tendencias temporales y detectar alertas epidemiológicas.")
    
    # Formulario para nuevo registro de vigilancia
    with st.expander("➕ Agregar Registro de Vigilancia", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            evento_vigilancia = st.selectbox(
                "Evento de Vigilancia:",
                ["Infección Respiratoria", "Gastroenteritis", "Dengue", "COVID-19", 
                 "Enfermedad Cardiovascular", "Salud Mental", "Otro"],
                key="evento_vigilancia"
            )
            
            fecha_inicio = st.date_input("Fecha de Inicio:", key="fecha_inicio_vigilancia")
            fecha_fin = st.date_input("Fecha de Fin:", key="fecha_fin_vigilancia")
        
        with col2:
            nivel_alerta = st.selectbox(
                "Nivel de Alerta:",
                ["Normal", "Atención", "Alerta", "Emergencia"],
                key="nivel_alerta"
            )
            
            sector_vigilancia = st.selectbox(
                "Sector:",
                ["Sector A", "Sector B", "Sector C", "Todos los Sectores"],
                key="sector_vigilancia"
            )
        
        # Datos de casos
        st.subheader("📊 Datos de Casos")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            casos_sospechosos = st.number_input("Casos Sospechosos:", min_value=0, value=10, key="casos_sospechosos")
            casos_confirmados = st.number_input("Casos Confirmados:", min_value=0, value=5, key="casos_confirmados")
        
        with col2:
            casos_graves = st.number_input("Casos Graves:", min_value=0, value=1, key="casos_graves")
            defunciones = st.number_input("Defunciones:", min_value=0, value=0, key="defunciones_vigilancia")
        
        with col3:
            poblacion_expuesta = st.number_input("Población Expuesta:", min_value=0, value=1000, key="poblacion_expuesta")
            
            if poblacion_expuesta > 0:
                tasa_ataque = (casos_confirmados / poblacion_expuesta) * 100
                st.metric("Tasa de Ataque (%)", f"{tasa_ataque:.1f}")
        
        # Características del evento
        st.subheader("🔍 Características del Evento")
        col1, col2 = st.columns(2)
        
        with col1:
            grupo_edad_afectado = st.multiselect(
                "Grupo de Edad Más Afectado:",
                ["0-4 años", "5-14 años", "15-44 años", "45-64 años", "65+ años"],
                key="grupo_edad_afectado"
            )
            
            sintomas_principales = st.multiselect(
                "Síntomas Principales:",
                ["Fiebre", "Tos", "Dolor de cabeza", "Diarrea", "Dificultad respiratoria", "Otro"],
                key="sintomas_principales"
            )
        
        with col2:
            factores_riesgo = st.multiselect(
                "Factores de Riesgo Identificados:",
                ["Hacinamiento", "Mala higiene", "Contacto con enfermos", "Viajes recientes", "Otro"],
                key="factores_riesgo_vigilancia"
            )
        
        # Acciones tomadas
        st.subheader("⚡ Acciones Tomadas")
        acciones_tomadas = st.multiselect(
            "Acciones Implementadas:",
            ["Aislamiento de casos", "Educación comunitaria", "Desinfección", 
             "Coordinación con autoridades", "Refuerzo de medidas preventivas", "Otro"],
            key="acciones_tomadas"
        )
        
        observaciones = st.text_area("Observaciones:", key="observaciones_vigilancia")
        
        if st.button("💾 Guardar Registro", key="guardar_vigilancia"):
            nuevo_registro = {
                'id': len(st.session_state.epidemiologia['vigilancia_epidemiologica']) + 1,
                'evento': evento_vigilancia,
                'fecha_inicio': str(fecha_inicio),
                'fecha_fin': str(fecha_fin),
                'nivel_alerta': nivel_alerta,
                'sector': sector_vigilancia,
                'casos_sospechosos': casos_sospechosos,
                'casos_confirmados': casos_confirmados,
                'casos_graves': casos_graves,
                'defunciones': defunciones,
                'poblacion_expuesta': poblacion_expuesta,
                'tasa_ataque': tasa_ataque if 'tasa_ataque' in locals() else 0,
                'grupo_edad': grupo_edad_afectado,
                'sintomas': sintomas_principales,
                'factores_riesgo': factores_riesgo,
                'acciones': acciones_tomadas,
                'observaciones': observaciones
            }
            
            st.session_state.epidemiologia['vigilancia_epidemiologica'].append(nuevo_registro)
            st.success("✅ Registro de vigilancia guardado exitosamente")
            st.rerun()
    
    # Mostrar registros de vigilancia
    if st.session_state.epidemiologia['vigilancia_epidemiologica']:
        st.subheader("📋 Registros de Vigilancia Epidemiológica")
        
        df_vigilancia = pd.DataFrame(st.session_state.epidemiologia['vigilancia_epidemiologica'])
        
        # Métricas
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Eventos", len(df_vigilancia))
        
        with col2:
            alertas = len(df_vigilancia[df_vigilancia['nivel_alerta'].isin(['Alerta', 'Emergencia'])])
            st.metric("Alertas/Emergencias", alertas)
        
        with col3:
            total_casos = df_vigilancia['casos_confirmados'].sum()
            st.metric("Total Casos Confirmados", total_casos)
        
        with col4:
            total_defunciones = df_vigilancia['defunciones'].sum()
            st.metric("Total Defunciones", total_defunciones)
        
        # Gráfico de nivel de alerta
        fig_alertas = px.pie(
            df_vigilancia.groupby('nivel_alerta').size().reset_index(name='count'),
            values='count',
            names='nivel_alerta',
            title="Distribución por Nivel de Alerta",
            color_discrete_map={
                'Normal': '#2ca02c',
                'Atención': '#ff7f0e',
                'Alerta': '#d62728',
                'Emergencia': '#8b0000'
            }
        )
        st.plotly_chart(fig_alertas, use_container_width=True)
        
        # Tabla de vigilancia
        st.dataframe(df_vigilancia[['evento', 'fecha_inicio', 'nivel_alerta', 'sector', 'casos_confirmados', 'defunciones']], use_container_width=True)

def mostrar_factores_riesgo():
    st.header("🎯 Análisis de Factores de Riesgo")
    st.markdown("**Objetivo:** Identificar y analizar factores de riesgo para la salud comunitaria.")
    
    # Formulario para nuevo factor de riesgo
    with st.expander("➕ Agregar Factor de Riesgo", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            factor_riesgo = st.selectbox(
                "Factor de Riesgo:",
                ["Obesidad", "Tabaquismo", "Alcoholismo", "Sedentarismo", "Mala alimentación",
                 "Hacinamiento", "Pobreza", "Bajo nivel educacional", "Estrés", "Otro"],
                key="factor_riesgo"
            )
            
            fecha_identificacion = st.date_input("Fecha de Identificación:", key="fecha_identificacion")
            
            sector_factor = st.selectbox(
                "Sector:",
                ["Sector A", "Sector B", "Sector C", "Todos los Sectores"],
                key="sector_factor"
            )
        
        with col2:
            nivel_riesgo = st.selectbox(
                "Nivel de Riesgo:",
                ["Alto", "Medio", "Bajo"],
                key="nivel_riesgo"
            )
            
            tendencia_factor = st.selectbox(
                "Tendencia:",
                ["En aumento", "Estable", "En disminución"],
                key="tendencia_factor"
            )
        
        # Datos del factor de riesgo
        st.subheader("📊 Datos del Factor de Riesgo")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            prevalencia_factor = st.number_input("Prevalencia (%):", min_value=0.0, max_value=100.0, value=25.0, key="prevalencia_factor")
            poblacion_expuesta = st.number_input("Población Expuesta:", min_value=0, value=250, key="poblacion_expuesta_factor")
        
        with col2:
            edad_promedio = st.number_input("Edad Promedio:", min_value=0, value=35, key="edad_promedio_factor")
            genero_mas_afectado = st.selectbox(
                "Género Más Afectado:",
                ["Hombres", "Mujeres", "Ambos"],
                key="genero_mas_afectado"
            )
        
        with col3:
            # Cálculo de impacto
            if poblacion_expuesta > 0:
                impacto_poblacional = (prevalencia_factor / 100) * poblacion_expuesta
                st.metric("Impacto Poblacional", f"{impacto_poblacional:.0f} personas")
        
        # Patologías asociadas
        st.subheader("🏥 Patologías Asociadas")
        patologias_asociadas = st.multiselect(
            "Patologías Relacionadas:",
            ["Diabetes", "Hipertensión", "Enfermedades cardiovasculares", "Cáncer", 
             "Enfermedades respiratorias", "Salud mental", "Otro"],
            key="patologias_asociadas"
        )
        
        # Intervenciones recomendadas
        st.subheader("💡 Intervenciones Recomendadas")
        intervenciones_factor = st.multiselect(
            "Intervenciones Sugeridas:",
            ["Educación en salud", "Programa de ejercicio", "Apoyo nutricional", 
             "Apoyo psicológico", "Coordinación intersectorial", "Otro"],
            key="intervenciones_factor"
        )
        
        observaciones = st.text_area("Observaciones:", key="observaciones_factor")
        
        if st.button("💾 Guardar Factor de Riesgo", key="guardar_factor"):
            nuevo_factor = {
                'id': len(st.session_state.epidemiologia['factores_riesgo']) + 1,
                'factor': factor_riesgo,
                'fecha': str(fecha_identificacion),
                'sector': sector_factor,
                'nivel_riesgo': nivel_riesgo,
                'tendencia': tendencia_factor,
                'prevalencia': prevalencia_factor,
                'poblacion_expuesta': poblacion_expuesta,
                'edad_promedio': edad_promedio,
                'genero': genero_mas_afectado,
                'impacto_poblacional': impacto_poblacional if 'impacto_poblacional' in locals() else 0,
                'patologias_asociadas': patologias_asociadas,
                'intervenciones': intervenciones_factor,
                'observaciones': observaciones
            }
            
            st.session_state.epidemiologia['factores_riesgo'].append(nuevo_factor)
            st.success("✅ Factor de riesgo guardado exitosamente")
            st.rerun()
    
    # Mostrar factores de riesgo
    if st.session_state.epidemiologia['factores_riesgo']:
        st.subheader("📋 Factores de Riesgo Identificados")
        
        df_factores = pd.DataFrame(st.session_state.epidemiologia['factores_riesgo'])
        
        # Métricas
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total Factores", len(df_factores))
        
        with col2:
            alto_riesgo = len(df_factores[df_factores['nivel_riesgo'] == 'Alto'])
            st.metric("Alto Riesgo", alto_riesgo)
        
        with col3:
            en_aumento = len(df_factores[df_factores['tendencia'] == 'En aumento'])
            st.metric("En Aumento", en_aumento)
        
        # Gráfico de prevalencia por factor
        fig_prevalencia_factor = px.bar(
            df_factores,
            x='factor',
            y='prevalencia',
            color='nivel_riesgo',
            title="Prevalencia de Factores de Riesgo",
            labels={'prevalencia': 'Prevalencia (%)', 'factor': 'Factor de Riesgo'}
        )
        st.plotly_chart(fig_prevalencia_factor, use_container_width=True)
        
        # Tabla de factores
        st.dataframe(df_factores[['factor', 'sector', 'nivel_riesgo', 'tendencia', 'prevalencia', 'impacto_poblacional']], use_container_width=True)

def mostrar_analisis_geografico():
    st.header("🗺️ Análisis Geográfico Epidemiológico")
    st.markdown("**Objetivo:** Analizar la distribución geográfica de eventos de salud.")
    
    # Formulario para nuevo análisis geográfico
    with st.expander("➕ Agregar Análisis Geográfico", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            evento_geografico = st.selectbox(
                "Evento de Salud:",
                ["Infección Respiratoria", "Diabetes", "Hipertensión", "Obesidad", 
                 "Embarazo Adolescente", "Accidentes", "Otro"],
                key="evento_geografico"
            )
            
            fecha_analisis = st.date_input("Fecha de Análisis:", key="fecha_analisis_geo")
            
            tipo_analisis = st.selectbox(
                "Tipo de Análisis:",
                ["Prevalencia", "Incidencia", "Mortalidad", "Otro"],
                key="tipo_analisis_geo"
            )
        
        with col2:
            unidad_geografica = st.selectbox(
                "Unidad Geográfica:",
                ["Sector", "Microárea", "Manzana", "Otro"],
                key="unidad_geografica"
            )
            
            periodo_analisis = st.selectbox(
                "Período de Análisis:",
                ["Último mes", "Último trimestre", "Último semestre", "Último año"],
                key="periodo_analisis_geo"
            )
        
        # Datos por sector
        st.subheader("📊 Datos por Sector")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("**Sector A**")
            casos_sector_a = st.number_input("Casos Sector A:", min_value=0, value=15, key="casos_sector_a")
            poblacion_sector_a = st.number_input("Población Sector A:", min_value=0, value=300, key="poblacion_sector_a")
        
        with col2:
            st.markdown("**Sector B**")
            casos_sector_b = st.number_input("Casos Sector B:", min_value=0, value=20, key="casos_sector_b")
            poblacion_sector_b = st.number_input("Población Sector B:", min_value=0, value=400, key="poblacion_sector_b")
        
        with col3:
            st.markdown("**Sector C**")
            casos_sector_c = st.number_input("Casos Sector C:", min_value=0, value=10, key="casos_sector_c")
            poblacion_sector_c = st.number_input("Población Sector C:", min_value=0, value=300, key="poblacion_sector_c")
        
        # Cálculos automáticos
        st.subheader("📈 Tasas Calculadas")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if poblacion_sector_a > 0:
                tasa_sector_a = (casos_sector_a / poblacion_sector_a) * 1000
                st.metric("Tasa Sector A (por 1000 hab.)", f"{tasa_sector_a:.1f}")
        
        with col2:
            if poblacion_sector_b > 0:
                tasa_sector_b = (casos_sector_b / poblacion_sector_b) * 1000
                st.metric("Tasa Sector B (por 1000 hab.)", f"{tasa_sector_b:.1f}")
        
        with col3:
            if poblacion_sector_c > 0:
                tasa_sector_c = (casos_sector_c / poblacion_sector_c) * 1000
                st.metric("Tasa Sector C (por 1000 hab.)", f"{tasa_sector_c:.1f}")
        
        # Análisis de clusters
        st.subheader("🔍 Análisis de Clusters")
        cluster_identificado = st.selectbox(
            "¿Se identificó algún cluster?",
            ["Sí", "No", "En análisis"],
            key="cluster_identificado"
        )
        
        if cluster_identificado == "Sí":
            caracteristicas_cluster = st.text_area("Características del Cluster:", key="caracteristicas_cluster")
            factores_cluster = st.multiselect(
                "Factores del Cluster:",
                ["Hacinamiento", "Pobreza", "Mala higiene", "Acceso limitado a servicios", "Otro"],
                key="factores_cluster"
            )
        
        # Intervenciones geográficas
        st.subheader("🎯 Intervenciones Geográficas")
        intervenciones_geo = st.multiselect(
            "Intervenciones Sugeridas:",
            ["Focalización en sector específico", "Educación comunitaria", "Mejora de servicios",
             "Coordinación intersectorial", "Monitoreo intensivo", "Otro"],
            key="intervenciones_geo"
        )
        
        observaciones = st.text_area("Observaciones:", key="observaciones_geo")
        
        if st.button("💾 Guardar Análisis", key="guardar_analisis_geo"):
            nuevo_analisis = {
                'id': len(st.session_state.epidemiologia['analisis_geografico']) + 1,
                'evento': evento_geografico,
                'fecha': str(fecha_analisis),
                'tipo_analisis': tipo_analisis,
                'unidad_geografica': unidad_geografica,
                'periodo': periodo_analisis,
                'sector_a': {'casos': casos_sector_a, 'poblacion': poblacion_sector_a, 'tasa': tasa_sector_a if 'tasa_sector_a' in locals() else 0},
                'sector_b': {'casos': casos_sector_b, 'poblacion': poblacion_sector_b, 'tasa': tasa_sector_b if 'tasa_sector_b' in locals() else 0},
                'sector_c': {'casos': casos_sector_c, 'poblacion': poblacion_sector_c, 'tasa': tasa_sector_c if 'tasa_sector_c' in locals() else 0},
                'cluster': cluster_identificado,
                'caracteristicas_cluster': caracteristicas_cluster if cluster_identificado == "Sí" else "",
                'factores_cluster': factores_cluster if cluster_identificado == "Sí" else [],
                'intervenciones': intervenciones_geo,
                'observaciones': observaciones
            }
            
            st.session_state.epidemiologia['analisis_geografico'].append(nuevo_analisis)
            st.success("✅ Análisis geográfico guardado exitosamente")
            st.rerun()
    
    # Mostrar análisis geográficos
    if st.session_state.epidemiologia['analisis_geografico']:
        st.subheader("📋 Análisis Geográficos Realizados")
        
        df_geo = pd.DataFrame(st.session_state.epidemiologia['analisis_geografico'])
        
        # Métricas
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total Análisis", len(df_geo))
        
        with col2:
            clusters = len(df_geo[df_geo['cluster'] == 'Sí'])
            st.metric("Clusters Identificados", clusters)
        
        with col3:
            eventos_unicos = df_geo['evento'].nunique()
            st.metric("Eventos Analizados", eventos_unicos)
        
        # Gráfico de distribución por sector
        if len(df_geo) > 0:
            # Crear datos para el gráfico
            sectores_data = []
            for _, row in df_geo.iterrows():
                sectores_data.append({
                    'Sector': 'Sector A',
                    'Tasa': row['sector_a']['tasa'],
                    'Evento': row['evento']
                })
                sectores_data.append({
                    'Sector': 'Sector B',
                    'Tasa': row['sector_b']['tasa'],
                    'Evento': row['evento']
                })
                sectores_data.append({
                    'Sector': 'Sector C',
                    'Tasa': row['sector_c']['tasa'],
                    'Evento': row['evento']
                })
            
            df_sectores = pd.DataFrame(sectores_data)
            
            fig_sectores = px.bar(
                df_sectores,
                x='Sector',
                y='Tasa',
                color='Evento',
                title="Distribución de Tasas por Sector",
                labels={'Tasa': 'Tasa (por 1000 hab.)', 'Sector': 'Sector'}
            )
            st.plotly_chart(fig_sectores, use_container_width=True)
        
        # Tabla de análisis
        st.dataframe(df_geo[['evento', 'fecha', 'tipo_analisis', 'cluster', 'intervenciones']], use_container_width=True)
    
    # Footer
    st.markdown("---")
    st.markdown("*Aplicación educativa desarrollada por Ricardo Delannoy Suazo para formación en diagnóstico comunitario en salud familiar. © 2025. Todos los derechos reservados.*") 