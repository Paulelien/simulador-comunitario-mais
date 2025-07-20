import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, date

def calcular_riesgo_social(familia):
    """Calcula el riesgo social basado en factores familiares"""
    puntaje = 0
    
    # Factores de riesgo social
    if familia["hacinamiento"] == "Alto":
        puntaje += 3
    elif familia["hacinamiento"] == "Medio":
        puntaje += 2
    elif familia["hacinamiento"] == "Bajo":
        puntaje += 1
    
    if familia["red_apoyo"] == "Débil":
        puntaje += 3
    elif familia["red_apoyo"] == "Regular":
        puntaje += 2
    elif familia["red_apoyo"] == "Fuerte":
        puntaje += 1
    
    if familia["participacion_social"] == "Nula":
        puntaje += 3
    elif familia["participacion_social"] == "Baja":
        puntaje += 2
    elif familia["participacion_social"] == "Alta":
        puntaje += 1
    
    if familia["acceso_aps"] == "Difícil":
        puntaje += 3
    elif familia["acceso_aps"] == "Regular":
        puntaje += 2
    elif familia["acceso_aps"] == "Fácil":
        puntaje += 1
    
    # Determinar nivel de riesgo
    if puntaje >= 10:
        return "Alto", puntaje
    elif puntaje >= 6:
        return "Medio", puntaje
    else:
        return "Bajo", puntaje

def calcular_riesgo_sanitario(familia):
    """Calcula el riesgo sanitario basado en condiciones de salud"""
    puntaje = 0
    
    # Enfermedades crónicas
    enfermedades = familia["enfermedades_cronicas"]
    if "Diabetes" in enfermedades:
        puntaje += 2
    if "Hipertensión" in enfermedades:
        puntaje += 2
    if "Obesidad" in enfermedades:
        puntaje += 1
    if "Enfermedad pulmonar" in enfermedades:
        puntaje += 2
    if "Enfermedad cardíaca" in enfermedades:
        puntaje += 3
    
    # Factores adicionales
    if familia["embarazo_adolescente"]:
        puntaje += 2
    if familia["violencia_intrafamiliar"]:
        puntaje += 3
    if familia["consumo_drogas"]:
        puntaje += 3
    if familia["desempleo"]:
        puntaje += 1
    
    # Determinar nivel de riesgo
    if puntaje >= 8:
        return "Alto", puntaje
    elif puntaje >= 4:
        return "Medio", puntaje
    else:
        return "Bajo", puntaje

def mostrar_registro_familias():
    st.markdown("""
    <div class="section-header">
        <h2>👨‍👩‍👧‍👦 Registro de Familias</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ### 🏠 ¿Qué es el Registro Familiar?
    
    El registro familiar es la base del trabajo en salud familiar. Permite identificar 
    las características, necesidades y factores de riesgo de cada familia para 
    planificar intervenciones personalizadas.
    """)
    
    # Verificar si hay sectores registrados
    if not st.session_state.sectores:
        st.warning("⚠️ Primero debes registrar sectores en la sección de Sectorización.")
        st.info("Ve a la sección '🗺️ Sectorización' para agregar sectores antes de continuar.")
        return
    
    # Formulario para registrar familias
    with st.expander("➕ Registrar Nueva Familia", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            sector_familia = st.selectbox(
                "Sector",
                [s["nombre"] for s in st.session_state.sectores]
            )
            
            apellido_familia = st.text_input("Apellido de la Familia", placeholder="Ej: González")
            num_integrantes = st.number_input("Número de Integrantes", min_value=1, max_value=20, value=4)
            
            # Información del jefe de hogar
            st.markdown("**Jefe de Hogar:**")
            nombre_jefe = st.text_input("Nombre", placeholder="Nombre del jefe de hogar")
            edad_jefe = st.number_input("Edad", min_value=18, max_value=100, value=35)
            ocupacion_jefe = st.selectbox(
                "Ocupación",
                ["Empleado", "Desempleado", "Jubilado", "Estudiante", "Dueña de casa", "Otro"]
            )
        
        with col2:
            # Características de la vivienda
            st.markdown("**Características de la Vivienda:**")
            tipo_vivienda = st.selectbox(
                "Tipo de Vivienda",
                ["Casa", "Departamento", "Mediagua", "Rancho", "Otro"]
            )
            
            hacinamiento = st.selectbox(
                "Nivel de Hacinamiento",
                ["Bajo", "Medio", "Alto"]
            )
            
            red_apoyo = st.selectbox(
                "Red de Apoyo",
                ["Fuerte", "Regular", "Débil"]
            )
            
            participacion_social = st.selectbox(
                "Participación Social",
                ["Alta", "Baja", "Nula"]
            )
        
        # Información de salud
        st.markdown("**Información de Salud:**")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            enfermedades_cronicas = st.multiselect(
                "Enfermedades Crónicas",
                ["Diabetes", "Hipertensión", "Obesidad", "Enfermedad pulmonar", 
                 "Enfermedad cardíaca", "Artritis", "Depresión", "Ansiedad", "Ninguna"]
            )
            
            acceso_aps = st.selectbox(
                "Acceso a APS",
                ["Fácil", "Regular", "Difícil"]
            )
        
        with col2:
            embarazo_adolescente = st.checkbox("Embarazo Adolescente")
            violencia_intrafamiliar = st.checkbox("Violencia Intrafamiliar")
            consumo_drogas = st.checkbox("Consumo de Drogas")
        
        with col3:
            desempleo = st.checkbox("Desempleo")
            discapacidad = st.checkbox("Persona con Discapacidad")
            adulto_mayor = st.checkbox("Adulto Mayor")
        
        # Información adicional
        st.markdown("**Información Adicional:**")
        col1, col2 = st.columns(2)
        
        with col1:
            observaciones = st.text_area("Observaciones", placeholder="Observaciones importantes sobre la familia...")
        
        with col2:
            fecha_registro = st.date_input("Fecha de Registro", value=date.today())
            responsable_registro = st.text_input("Responsable del Registro", placeholder="Nombre del TENS")
        
        if st.button("💾 Guardar Familia", type="primary"):
            if apellido_familia and nombre_jefe and responsable_registro:
                # Calcular riesgos
                riesgo_social, puntaje_social = calcular_riesgo_social({
                    "hacinamiento": hacinamiento,
                    "red_apoyo": red_apoyo,
                    "participacion_social": participacion_social,
                    "acceso_aps": acceso_aps
                })
                
                riesgo_sanitario, puntaje_sanitario = calcular_riesgo_sanitario({
                    "enfermedades_cronicas": enfermedades_cronicas,
                    "embarazo_adolescente": embarazo_adolescente,
                    "violencia_intrafamiliar": violencia_intrafamiliar,
                    "consumo_drogas": consumo_drogas,
                    "desempleo": desempleo
                })
                
                nueva_familia = {
                    "sector": sector_familia,
                    "apellido": apellido_familia,
                    "num_integrantes": num_integrantes,
                    "jefe_hogar": {
                        "nombre": nombre_jefe,
                        "edad": edad_jefe,
                        "ocupacion": ocupacion_jefe
                    },
                    "vivienda": {
                        "tipo": tipo_vivienda,
                        "hacinamiento": hacinamiento,
                        "red_apoyo": red_apoyo,
                        "participacion_social": participacion_social,
                        "acceso_aps": acceso_aps
                    },
                    "salud": {
                        "enfermedades_cronicas": enfermedades_cronicas,
                        "embarazo_adolescente": embarazo_adolescente,
                        "violencia_intrafamiliar": violencia_intrafamiliar,
                        "consumo_drogas": consumo_drogas,
                        "desempleo": desempleo,
                        "discapacidad": discapacidad,
                        "adulto_mayor": adulto_mayor
                    },
                    "riesgos": {
                        "social": {
                            "nivel": riesgo_social,
                            "puntaje": puntaje_social
                        },
                        "sanitario": {
                            "nivel": riesgo_sanitario,
                            "puntaje": puntaje_sanitario
                        }
                    },
                    "observaciones": observaciones,
                    "fecha_registro": fecha_registro.strftime("%Y-%m-%d"),
                    "responsable": responsable_registro
                }
                
                st.session_state.familias.append(nueva_familia)
                st.success(f"✅ Familia '{apellido_familia}' registrada exitosamente!")
                st.rerun()
            else:
                st.error("❌ Por favor completa los campos obligatorios (apellido, nombre del jefe y responsable)")
    
    # Mostrar familias registradas
    if st.session_state.familias:
        st.markdown("### 📊 Familias Registradas")
        
        # Crear DataFrame para visualización
        familias_data = []
        for familia in st.session_state.familias:
            familias_data.append({
                "Sector": familia["sector"],
                "Apellido": familia["apellido"],
                "Integrantes": familia["num_integrantes"],
                "Jefe de Hogar": familia["jefe_hogar"]["nombre"],
                "Edad Jefe": familia["jefe_hogar"]["edad"],
                "Ocupación": familia["jefe_hogar"]["ocupacion"],
                "Tipo Vivienda": familia["vivienda"]["tipo"],
                "Hacinamiento": familia["vivienda"]["hacinamiento"],
                "Riesgo Social": familia["riesgos"]["social"]["nivel"],
                "Riesgo Sanitario": familia["riesgos"]["sanitario"]["nivel"],
                "Puntaje Social": familia["riesgos"]["social"]["puntaje"],
                "Puntaje Sanitario": familia["riesgos"]["sanitario"]["puntaje"],
                "Fecha Registro": familia["fecha_registro"],
                "Responsable": familia["responsable"]
            })
        
        df_familias = pd.DataFrame(familias_data)
        
        # Filtros
        col1, col2, col3 = st.columns(3)
        
        with col1:
            sector_filtro = st.selectbox(
                "Filtrar por Sector",
                ["Todos"] + list(df_familias["Sector"].unique())
            )
        
        with col2:
            riesgo_filtro = st.selectbox(
                "Filtrar por Riesgo",
                ["Todos", "Alto", "Medio", "Bajo"]
            )
        
        with col3:
            hacinamiento_filtro = st.selectbox(
                "Filtrar por Hacinamiento",
                ["Todos", "Alto", "Medio", "Bajo"]
            )
        
        # Aplicar filtros
        df_filtrado = df_familias.copy()
        
        if sector_filtro != "Todos":
            df_filtrado = df_filtrado[df_filtrado["Sector"] == sector_filtro]
        
        if riesgo_filtro != "Todos":
            df_filtrado = df_filtrado[
                (df_filtrado["Riesgo Social"] == riesgo_filtro) | 
                (df_filtrado["Riesgo Sanitario"] == riesgo_filtro)
            ]
        
        if hacinamiento_filtro != "Todos":
            df_filtrado = df_filtrado[df_filtrado["Hacinamiento"] == hacinamiento_filtro]
        
        # Mostrar tabla filtrada
        st.dataframe(
            df_filtrado[["Sector", "Apellido", "Integrantes", "Jefe de Hogar", 
                        "Riesgo Social", "Riesgo Sanitario", "Hacinamiento"]],
            use_container_width=True
        )
        
        # Gráficos
        col1, col2 = st.columns(2)
        
        with col1:
            # Gráfico de distribución de riesgos
            fig_riesgos = px.bar(
                df_familias,
                x="Sector",
                color="Riesgo Social",
                title="Distribución de Riesgo Social por Sector",
                color_discrete_map={"Alto": "red", "Medio": "orange", "Bajo": "green"}
            )
            fig_riesgos.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig_riesgos, use_container_width=True)
        
        with col2:
            # Gráfico de riesgo sanitario
            fig_riesgo_sanitario = px.bar(
                df_familias,
                x="Sector",
                color="Riesgo Sanitario",
                title="Distribución de Riesgo Sanitario por Sector",
                color_discrete_map={"Alto": "red", "Medio": "orange", "Bajo": "green"}
            )
            fig_riesgo_sanitario.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig_riesgo_sanitario, use_container_width=True)
        
        # Análisis de vulnerabilidad
        st.markdown("### 🚨 Análisis de Vulnerabilidad")
        
        # Calcular estadísticas por sector
        vulnerabilidad_data = []
        for sector in df_familias["Sector"].unique():
            df_sector = df_familias[df_familias["Sector"] == sector]
            
            total_familias = len(df_sector)
            familias_alto_riesgo = len(df_sector[
                (df_sector["Riesgo Social"] == "Alto") | 
                (df_sector["Riesgo Sanitario"] == "Alto")
            ])
            porcentaje_alto_riesgo = (familias_alto_riesgo / total_familias) * 100 if total_familias > 0 else 0
            
            vulnerabilidad_data.append({
                "Sector": sector,
                "Total Familias": total_familias,
                "Familias Alto Riesgo": familias_alto_riesgo,
                "Porcentaje Alto Riesgo": porcentaje_alto_riesgo
            })
        
        df_vulnerabilidad = pd.DataFrame(vulnerabilidad_data)
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig_vulnerabilidad = px.bar(
                df_vulnerabilidad,
                x="Sector",
                y="Porcentaje Alto Riesgo",
                title="Porcentaje de Familias en Alto Riesgo por Sector",
                color="Porcentaje Alto Riesgo",
                color_continuous_scale="RdYlGn_r"
            )
            fig_vulnerabilidad.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig_vulnerabilidad, use_container_width=True)
        
        with col2:
            # Gráfico de hacinamiento
            fig_hacinamiento = px.pie(
                df_familias,
                names="Hacinamiento",
                title="Distribución por Nivel de Hacinamiento",
                color_discrete_map={"Alto": "red", "Medio": "orange", "Bajo": "green"}
            )
            st.plotly_chart(fig_hacinamiento, use_container_width=True)
        
        # Alertas y recomendaciones
        st.markdown("### ⚠️ Alertas y Recomendaciones")
        
        for sector in df_familias["Sector"].unique():
            df_sector = df_familias[df_familias["Sector"] == sector]
            
            st.markdown(f"**Sector: {sector}**")
            
            # Familias en alto riesgo
            alto_riesgo = len(df_sector[
                (df_sector["Riesgo Social"] == "Alto") | 
                (df_sector["Riesgo Sanitario"] == "Alto")
            ])
            
            if alto_riesgo > 0:
                st.warning(f"🚨 {alto_riesgo} familias en alto riesgo requieren intervención prioritaria")
            
            # Hacinamiento alto
            hacinamiento_alto = len(df_sector[df_sector["Hacinamiento"] == "Alto"])
            if hacinamiento_alto > 0:
                st.warning(f"🏠 {hacinamiento_alto} familias con hacinamiento alto")
            
            # Violencia intrafamiliar
            violencia_count = sum(1 for f in st.session_state.familias 
                                if f["sector"] == sector and f["salud"]["violencia_intrafamiliar"])
            if violencia_count > 0:
                st.error(f"🚨 {violencia_count} casos de violencia intrafamiliar detectados")
            
            st.markdown("---")
    
    else:
        st.info("📝 No hay familias registradas. Registra familias usando el formulario de arriba.")
    
    # Botón para limpiar datos
    if st.session_state.familias:
        if st.button("🗑️ Limpiar Todas las Familias"):
            st.session_state.familias = []
            st.success("✅ Todas las familias han sido eliminadas")
            st.rerun() 