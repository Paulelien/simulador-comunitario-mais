import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def mostrar_sectorizacion():
    st.markdown("""
    <div class="section-header">
        <h2>🗺️ Sectorización del Territorio</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ### 📍 ¿Qué es la Sectorización?
    
    La sectorización es el proceso de dividir el territorio en áreas geográficas más pequeñas 
    para facilitar la atención de salud. Cada sector debe tener características similares 
    en términos de población, recursos y necesidades.
    """)
    
    # Formulario para agregar sectores
    with st.expander("➕ Agregar Nuevo Sector", expanded=True):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            nombre_sector = st.text_input("Nombre del Sector", placeholder="Ej: Sector Norte")
            poblacion_total = st.number_input("Población Total", min_value=1, value=1000)
        
        with col2:
            num_familias = st.number_input("Número de Familias", min_value=1, value=250)
            tipo_territorio = st.selectbox(
                "Tipo de Territorio",
                ["Urbano", "Rural", "Mixto", "Indígena", "Costero"]
            )
        
        with col3:
            nivel_socioeconomico = st.selectbox(
                "Nivel Socioeconómico",
                ["Alto", "Medio-Alto", "Medio", "Medio-Bajo", "Bajo"]
            )
            vulnerabilidad = st.selectbox(
                "Nivel de Vulnerabilidad",
                ["Baja", "Media", "Alta", "Crítica"]
            )
        
        # Características adicionales
        st.markdown("**Características del Territorio:**")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            tiene_agua_potable = st.checkbox("Agua Potable", value=True)
            tiene_electricidad = st.checkbox("Electricidad", value=True)
        
        with col2:
            tiene_alcantarillado = st.checkbox("Alcantarillado", value=True)
            tiene_transporte = st.checkbox("Transporte Público", value=True)
        
        with col3:
            tiene_escuela = st.checkbox("Escuela", value=True)
            tiene_cesfam = st.checkbox("CESFAM", value=False)
        
        with col4:
            tiene_organizaciones = st.checkbox("Organizaciones Comunitarias", value=True)
            tiene_areas_verdes = st.checkbox("Áreas Verdes", value=True)
        
        # Problemas identificados
        problemas = st.multiselect(
            "Problemas Identificados en el Sector",
            ["Hacinamiento", "Contaminación", "Inseguridad", "Falta de servicios básicos", 
             "Desempleo", "Violencia intrafamiliar", "Consumo de drogas", "Embarazo adolescente",
             "Obesidad", "Diabetes", "Hipertensión", "Otros"],
            default=[]
        )
        
        if st.button("💾 Guardar Sector", type="primary"):
            if nombre_sector:
                nuevo_sector = {
                    "nombre": nombre_sector,
                    "poblacion_total": poblacion_total,
                    "num_familias": num_familias,
                    "tipo_territorio": tipo_territorio,
                    "nivel_socioeconomico": nivel_socioeconomico,
                    "vulnerabilidad": vulnerabilidad,
                    "servicios": {
                        "agua_potable": tiene_agua_potable,
                        "electricidad": tiene_electricidad,
                        "alcantarillado": tiene_alcantarillado,
                        "transporte": tiene_transporte,
                        "escuela": tiene_escuela,
                        "cesfam": tiene_cesfam,
                        "organizaciones": tiene_organizaciones,
                        "areas_verdes": tiene_areas_verdes
                    },
                    "problemas": problemas
                }
                
                st.session_state.sectores.append(nuevo_sector)
                

                
                st.success(f"✅ Sector '{nombre_sector}' agregado exitosamente!")
                st.rerun()
            else:
                st.error("❌ Por favor ingresa el nombre del sector")
    
    # Mostrar sectores existentes
    if st.session_state.sectores:
        st.markdown("### 📊 Sectores Registrados")
        
        # Crear DataFrame para visualización
        df_sectores = pd.DataFrame(st.session_state.sectores)
        
        # Mostrar tabla
        st.dataframe(
            df_sectores[["nombre", "poblacion_total", "num_familias", "tipo_territorio", 
                        "nivel_socioeconomico", "vulnerabilidad"]],
            use_container_width=True
        )
        
        # Gráficos
        col1, col2 = st.columns(2)
        
        with col1:
            # Gráfico de población por sector
            fig_poblacion = px.bar(
                df_sectores, 
                x="nombre", 
                y="poblacion_total",
                title="Población por Sector",
                labels={"nombre": "Sector", "poblacion_total": "Población"}
            )
            fig_poblacion.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig_poblacion, use_container_width=True)
        
        with col2:
            # Gráfico de vulnerabilidad
            fig_vulnerabilidad = px.pie(
                df_sectores, 
                names="vulnerabilidad",
                title="Distribución por Nivel de Vulnerabilidad"
            )
            st.plotly_chart(fig_vulnerabilidad, use_container_width=True)
        
        # Mapa esquemático (simulado)
        st.markdown("### 🗺️ Mapa Esquemático de Sectores")
        
        # Crear un mapa simple con plotly
        fig_mapa = go.Figure()
        
        # Simular posiciones de sectores
        for i, sector in enumerate(st.session_state.sectores):
            x = i * 2
            y = 0
            
            # Color según vulnerabilidad
            color_map = {"Baja": "green", "Media": "yellow", "Alta": "orange", "Crítica": "red"}
            color = color_map.get(sector["vulnerabilidad"], "blue")
            
            fig_mapa.add_trace(go.Scatter(
                x=[x], y=[y],
                mode='markers+text',
                marker=dict(size=20, color=color),
                text=sector["nombre"],
                textposition="top center",
                name=sector["nombre"],
                hovertemplate=f"<b>{sector['nombre']}</b><br>" +
                             f"Población: {sector['poblacion_total']}<br>" +
                             f"Familias: {sector['num_familias']}<br>" +
                             f"Vulnerabilidad: {sector['vulnerabilidad']}<extra></extra>"
            ))
        
        fig_mapa.update_layout(
            title="Distribución Geográfica de Sectores",
            xaxis_title="",
            yaxis_title="",
            showlegend=False,
            height=400
        )
        
        st.plotly_chart(fig_mapa, use_container_width=True)
        
        # Resumen estadístico
        st.markdown("### 📈 Resumen Estadístico")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total de Sectores", len(st.session_state.sectores))
        
        with col2:
            total_poblacion = sum(s["poblacion_total"] for s in st.session_state.sectores)
            st.metric("Población Total", f"{total_poblacion:,}")
        
        with col3:
            total_familias = sum(s["num_familias"] for s in st.session_state.sectores)
            st.metric("Total Familias", f"{total_familias:,}")
        
        with col4:
            promedio_familias = total_familias / len(st.session_state.sectores) if st.session_state.sectores else 0
            st.metric("Promedio Familias/Sector", f"{promedio_familias:.1f}")
    
    else:
        st.info("📝 No hay sectores registrados. Agrega tu primer sector usando el formulario de arriba.")
    
    # Botón para limpiar datos
    if st.session_state.sectores:
        if st.button("🗑️ Limpiar Todos los Sectores"):
            st.session_state.sectores = []
            st.success("✅ Todos los sectores han sido eliminados")
            st.rerun() 