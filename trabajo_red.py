import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

def mostrar_trabajo_red():
    st.markdown("""
    <div class="section-header">
        <h2>🌐 Trabajo en Red Intersectorial</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ### 🤝 ¿Qué es el Trabajo en Red?
    
    El trabajo en red intersectorial es la coordinación entre diferentes instituciones y 
    organizaciones para abordar de manera integral los problemas de salud de la comunidad. 
    Permite aprovechar recursos, compartir información y desarrollar intervenciones más efectivas.
    """)
    
    # Formulario para registrar instituciones
    with st.expander("➕ Registrar Institución", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            nombre_institucion = st.text_input("Nombre de la Institución", placeholder="Ej: Escuela Básica San José")
            tipo_institucion = st.selectbox(
                "Tipo de Institución",
                ["Educación", "Salud", "Municipalidad", "Organización Comunitaria", 
                 "Servicios Sociales", "Seguridad", "Deportes y Recreación", "Otro"]
            )
            
            sector_cobertura = st.multiselect(
                "Sectores de Cobertura",
                [s["nombre"] for s in st.session_state.sectores] if st.session_state.sectores else []
            )
        
        with col2:
            contacto_principal = st.text_input("Contacto Principal", placeholder="Nombre del contacto")
            telefono_contacto = st.text_input("Teléfono", placeholder="+56 9 XXXX XXXX")
            email_contacto = st.text_input("Email", placeholder="contacto@institucion.cl")
        
        # Información adicional
        st.markdown("**Información Adicional:**")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            horario_atencion = st.text_input("Horario de Atención", placeholder="Lunes a Viernes 8:00-17:00")
            modalidad_trabajo = st.selectbox(
                "Modalidad de Trabajo",
                ["Presencial", "Híbrido", "Virtual", "Mixto"]
            )
        
        with col2:
            recursos_disponibles = st.multiselect(
                "Recursos Disponibles",
                ["Espacios físicos", "Equipamiento", "Personal especializado", 
                 "Programas educativos", "Atención psicológica", "Apoyo social", 
                 "Actividades recreativas", "Otros"]
            )
            
            poblacion_objetivo = st.multiselect(
                "Población Objetivo",
                ["Niños y adolescentes", "Adultos", "Adultos mayores", 
                 "Familias", "Mujeres", "Hombres", "Personas con discapacidad", 
                 "Población general"]
            )
        
        with col3:
            nivel_coordinacion = st.selectbox(
                "Nivel de Coordinación Actual",
                ["Excelente", "Buena", "Regular", "Débil", "Sin coordinación"]
            )
            
            frecuencia_contacto = st.selectbox(
                "Frecuencia de Contacto",
                ["Diario", "Semanal", "Quincenal", "Mensual", "Ocasional", "Sin contacto"]
            )
        
        # Programas y servicios
        st.markdown("**Programas y Servicios:**")
        programas_servicios = st.text_area(
            "Describe los programas y servicios que ofrece la institución",
            placeholder="Lista de programas, servicios especializados, actividades comunitarias..."
        )
        
        # Fortalezas y debilidades
        col1, col2 = st.columns(2)
        
        with col1:
            fortalezas = st.text_area(
                "Fortalezas de la Institución",
                placeholder="Recursos, experiencia, personal capacitado..."
            )
        
        with col2:
            debilidades = st.text_area(
                "Debilidades o Limitaciones",
                placeholder="Falta de recursos, personal limitado, horarios restringidos..."
            )
        
        # Oportunidades de trabajo conjunto
        oportunidades_trabajo = st.text_area(
            "Oportunidades de Trabajo Conjunto",
            placeholder="Cómo se puede trabajar en conjunto, proyectos compartidos..."
        )
        
        if st.button("💾 Guardar Institución", type="primary"):
            if nombre_institucion and contacto_principal:
                nueva_institucion = {
                    "nombre": nombre_institucion,
                    "tipo": tipo_institucion,
                    "sectores_cobertura": sector_cobertura,
                    "contacto": {
                        "nombre": contacto_principal,
                        "telefono": telefono_contacto,
                        "email": email_contacto
                    },
                    "informacion": {
                        "horario": horario_atencion,
                        "modalidad": modalidad_trabajo,
                        "nivel_coordinacion": nivel_coordinacion,
                        "frecuencia_contacto": frecuencia_contacto
                    },
                    "recursos": recursos_disponibles,
                    "poblacion_objetivo": poblacion_objetivo,
                    "programas_servicios": programas_servicios,
                    "fortalezas": fortalezas,
                    "debilidades": debilidades,
                    "oportunidades_trabajo": oportunidades_trabajo,
                    "fecha_registro": datetime.now().strftime("%Y-%m-%d")
                }
                
                st.session_state.instituciones.append(nueva_institucion)
                st.success(f"✅ Institución '{nombre_institucion}' registrada exitosamente!")
                st.rerun()
            else:
                st.error("❌ Por favor completa los campos obligatorios (nombre de institución y contacto principal)")
    
    # Mostrar instituciones registradas
    if st.session_state.instituciones:
        st.markdown("### 📊 Red de Instituciones")
        
        # Crear DataFrame para visualización
        instituciones_data = []
        for institucion in st.session_state.instituciones:
            instituciones_data.append({
                "Institución": institucion["nombre"],
                "Tipo": institucion["tipo"],
                "Contacto": institucion["contacto"]["nombre"],
                "Teléfono": institucion["contacto"]["telefono"],
                "Nivel Coordinación": institucion["informacion"]["nivel_coordinacion"],
                "Frecuencia Contacto": institucion["informacion"]["frecuencia_contacto"],
                "Modalidad": institucion["informacion"]["modalidad"],
                "Sectores": ", ".join(institucion["sectores_cobertura"]) if institucion["sectores_cobertura"] else "Todos"
            })
        
        df_instituciones = pd.DataFrame(instituciones_data)
        
        # Filtros
        col1, col2, col3 = st.columns(3)
        
        with col1:
            tipo_filtro = st.selectbox(
                "Filtrar por Tipo",
                ["Todos"] + list(df_instituciones["Tipo"].unique())
            )
        
        with col2:
            coordinacion_filtro = st.selectbox(
                "Filtrar por Coordinación",
                ["Todos"] + list(df_instituciones["Nivel Coordinación"].unique())
            )
        
        with col3:
            modalidad_filtro = st.selectbox(
                "Filtrar por Modalidad",
                ["Todos"] + list(df_instituciones["Modalidad"].unique())
            )
        
        # Aplicar filtros
        df_filtrado = df_instituciones.copy()
        
        if tipo_filtro != "Todos":
            df_filtrado = df_filtrado[df_filtrado["Tipo"] == tipo_filtro]
        
        if coordinacion_filtro != "Todos":
            df_filtrado = df_filtrado[df_filtrado["Nivel Coordinación"] == coordinacion_filtro]
        
        if modalidad_filtro != "Todos":
            df_filtrado = df_filtrado[df_filtrado["Modalidad"] == modalidad_filtro]
        
        # Mostrar tabla filtrada
        st.dataframe(
            df_filtrado[["Institución", "Tipo", "Contacto", "Nivel Coordinación", 
                        "Frecuencia Contacto", "Modalidad"]],
            use_container_width=True
        )
        
        # Gráficos
        col1, col2 = st.columns(2)
        
        with col1:
            # Gráfico por tipo de institución
            fig_tipo = px.pie(
                df_instituciones,
                names="Tipo",
                title="Distribución por Tipo de Institución"
            )
            st.plotly_chart(fig_tipo, use_container_width=True)
        
        with col2:
            # Gráfico de nivel de coordinación
            fig_coordinacion = px.bar(
                df_instituciones,
                x="Tipo",
                color="Nivel Coordinación",
                title="Nivel de Coordinación por Tipo de Institución",
                color_discrete_map={
                    "Excelente": "green",
                    "Buena": "lightgreen", 
                    "Regular": "yellow",
                    "Débil": "orange",
                    "Sin coordinación": "red"
                }
            )
            fig_coordinacion.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig_coordinacion, use_container_width=True)
        
        # Análisis de la red
        st.markdown("### 🔗 Análisis de la Red Intersectorial")
        
        # Estadísticas de la red
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            total_instituciones = len(st.session_state.instituciones)
            st.metric("Total Instituciones", total_instituciones)
        
        with col2:
            instituciones_excelente = len([i for i in st.session_state.instituciones 
                                         if i["informacion"]["nivel_coordinacion"] == "Excelente"])
            st.metric("Coordinación Excelente", instituciones_excelente)
        
        with col3:
            instituciones_salud = len([i for i in st.session_state.instituciones 
                                     if i["tipo"] == "Salud"])
            st.metric("Instituciones de Salud", instituciones_salud)
        
        with col4:
            instituciones_educacion = len([i for i in st.session_state.instituciones 
                                         if i["tipo"] == "Educación"])
            st.metric("Instituciones de Educación", instituciones_educacion)
        
        # Mapa de red (simulado)
        st.markdown("### 🗺️ Mapa de Red Intersectorial")
        
        # Crear un gráfico de red simple
        fig_red = go.Figure()
        
        # Posiciones de instituciones por tipo
        posiciones = {
            "Salud": (0, 2),
            "Educación": (2, 2), 
            "Municipalidad": (1, 0),
            "Organización Comunitaria": (-2, 1),
            "Servicios Sociales": (2, 0),
            "Seguridad": (-1, -1),
            "Deportes y Recreación": (0, -2),
            "Otro": (3, 1)
        }
        
        # Agregar nodos (instituciones)
        for institucion in st.session_state.instituciones:
            tipo = institucion["tipo"]
            if tipo in posiciones:
                x, y = posiciones[tipo]
                
                # Color según nivel de coordinación
                color_map = {
                    "Excelente": "green",
                    "Buena": "lightgreen",
                    "Regular": "yellow", 
                    "Débil": "orange",
                    "Sin coordinación": "red"
                }
                color = color_map.get(institucion["informacion"]["nivel_coordinacion"], "blue")
                
                fig_red.add_trace(go.Scatter(
                    x=[x], y=[y],
                    mode='markers+text',
                    marker=dict(size=15, color=color),
                    text=institucion["nombre"][:20] + "..." if len(institucion["nombre"]) > 20 else institucion["nombre"],
                    textposition="top center",
                    name=institucion["nombre"],
                    hovertemplate=f"<b>{institucion['nombre']}</b><br>" +
                                 f"Tipo: {institucion['tipo']}<br>" +
                                 f"Coordinación: {institucion['informacion']['nivel_coordinacion']}<br>" +
                                 f"Contacto: {institucion['contacto']['nombre']}<extra></extra>"
                ))
        
        fig_red.update_layout(
            title="Red Intersectorial - Mapa de Instituciones",
            xaxis_title="",
            yaxis_title="",
            showlegend=False,
            height=500
        )
        
        st.plotly_chart(fig_red, use_container_width=True)
        
        # Análisis de fortalezas y oportunidades
        st.markdown("### 💪 Fortalezas y Oportunidades de la Red")
        
        # Contar recursos disponibles
        todos_recursos = []
        for institucion in st.session_state.instituciones:
            todos_recursos.extend(institucion["recursos"])
        
        if todos_recursos:
            from collections import Counter
            recursos_count = Counter(todos_recursos)
            
            col1, col2 = st.columns(2)
            
            with col1:
                fig_recursos = px.bar(
                    x=list(recursos_count.keys()),
                    y=list(recursos_count.values()),
                    title="Recursos Disponibles en la Red",
                    labels={"x": "Recurso", "y": "Cantidad de Instituciones"}
                )
                fig_recursos.update_layout(xaxis_tickangle=-45)
                st.plotly_chart(fig_recursos, use_container_width=True)
            
            with col2:
                # Población objetivo
                todas_poblaciones = []
                for institucion in st.session_state.instituciones:
                    todas_poblaciones.extend(institucion["poblacion_objetivo"])
                
                if todas_poblaciones:
                    poblaciones_count = Counter(todas_poblaciones)
                    fig_poblacion = px.pie(
                        values=list(poblaciones_count.values()),
                        names=list(poblaciones_count.keys()),
                        title="Población Objetivo de la Red"
                    )
                    st.plotly_chart(fig_poblacion, use_container_width=True)
        
        # Recomendaciones para fortalecer la red
        st.markdown("### 🎯 Recomendaciones para Fortalecer la Red")
        
        # Análisis de coordinación
        coordinacion_debil = [i for i in st.session_state.instituciones 
                            if i["informacion"]["nivel_coordinacion"] in ["Débil", "Sin coordinación"]]
        
        if coordinacion_debil:
            st.warning(f"⚠️ **{len(coordinacion_debil)} instituciones** tienen coordinación débil o nula:")
            for institucion in coordinacion_debil:
                st.write(f"• {institucion['nombre']} ({institucion['tipo']})")
        
        # Oportunidades de mejora
        st.markdown("**Oportunidades de mejora identificadas:**")
        
        if st.session_state.instituciones:
            # Verificar si hay instituciones de salud
            instituciones_salud = [i for i in st.session_state.instituciones if i["tipo"] == "Salud"]
            if len(instituciones_salud) < 2:
                st.info("• Fortalecer la red de instituciones de salud")
            
            # Verificar coordinación con educación
            instituciones_educacion = [i for i in st.session_state.instituciones if i["tipo"] == "Educación"]
            if instituciones_educacion:
                st.info("• Desarrollar programas conjuntos con instituciones educativas")
            
            # Verificar organizaciones comunitarias
            org_comunitarias = [i for i in st.session_state.instituciones if i["tipo"] == "Organización Comunitaria"]
            if org_comunitarias:
                st.info("• Potenciar el trabajo con organizaciones comunitarias")
            
            # Verificar servicios sociales
            servicios_sociales = [i for i in st.session_state.instituciones if i["tipo"] == "Servicios Sociales"]
            if servicios_sociales:
                st.info("• Coordinar con servicios sociales para atención integral")
    
    else:
        st.info("📝 No hay instituciones registradas. Registra instituciones usando el formulario de arriba.")
    
    # Botón para limpiar datos
    if st.session_state.instituciones:
        if st.button("🗑️ Limpiar Todas las Instituciones"):
            st.session_state.instituciones = []
            st.success("✅ Todas las instituciones han sido eliminadas")
            st.rerun() 