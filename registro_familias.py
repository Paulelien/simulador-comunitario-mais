import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, date
import numpy as np

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

def mostrar_dashboard_familias():
    """Muestra un dashboard interactivo con estadísticas de las familias"""
    if not st.session_state.familias:
        return
    
    st.markdown("### 📊 Dashboard de Familias")
    
    # Crear DataFrame para análisis
    df_familias = pd.DataFrame(st.session_state.familias)
    
    # Métricas principales
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Familias", len(df_familias))
    
    with col2:
        total_integrantes = df_familias['num_integrantes'].sum()
        st.metric("Total Integrantes", total_integrantes)
    
    with col3:
        riesgo_alto = len(df_familias[df_familias['riesgos'].apply(lambda x: x['social']['nivel'] == 'Alto')])
        st.metric("Riesgo Social Alto", riesgo_alto)
    
    with col4:
        riesgo_sanitario_alto = len(df_familias[df_familias['riesgos'].apply(lambda x: x['sanitario']['nivel'] == 'Alto')])
        st.metric("Riesgo Sanitario Alto", riesgo_sanitario_alto)
    
    # Gráficos interactivos
    col1, col2 = st.columns(2)
    
    with col1:
        # Distribución por sector
        sector_counts = df_familias['sector'].value_counts()
        fig_sector = px.pie(
            values=sector_counts.values, 
            names=sector_counts.index,
            title="Distribución por Sector",
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        fig_sector.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig_sector, use_container_width=True)
    
    with col2:
        # Distribución de riesgo social
        riesgo_social = [f['riesgos']['social']['nivel'] for f in st.session_state.familias]
        riesgo_counts = pd.Series(riesgo_social).value_counts()
        fig_riesgo = px.bar(
            x=riesgo_counts.index,
            y=riesgo_counts.values,
            title="Distribución de Riesgo Social",
            color=riesgo_counts.values,
            color_continuous_scale='RdYlGn_r'
        )
        fig_riesgo.update_layout(xaxis_title="Nivel de Riesgo", yaxis_title="Número de Familias")
        st.plotly_chart(fig_riesgo, use_container_width=True)
    
    # Gráfico de correlación entre riesgos
    riesgo_social_puntajes = [f['riesgos']['social']['puntaje'] for f in st.session_state.familias]
    riesgo_sanitario_puntajes = [f['riesgos']['sanitario']['puntaje'] for f in st.session_state.familias]
    
    fig_correlacion = px.scatter(
        x=riesgo_social_puntajes,
        y=riesgo_sanitario_puntajes,
        title="Correlación Riesgo Social vs Sanitario",
        labels={'x': 'Puntaje Riesgo Social', 'y': 'Puntaje Riesgo Sanitario'},
        color=riesgo_social_puntajes,
        size=riesgo_sanitario_puntajes,
        hover_data=[df_familias['apellido']]
    )
    st.plotly_chart(fig_correlacion, use_container_width=True)

def mostrar_filtros_avanzados():
    """Muestra filtros avanzados para buscar familias"""
    if not st.session_state.familias:
        return
    
    st.markdown("### 🔍 Filtros y Búsqueda Avanzada")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Filtro por sector
        sectores = list(set([f['sector'] for f in st.session_state.familias]))
        sector_filtro = st.selectbox("Filtrar por Sector", ["Todos"] + sectores)
        
        # Filtro por riesgo social
        riesgo_social_filtro = st.selectbox("Filtrar por Riesgo Social", ["Todos", "Bajo", "Medio", "Alto", "Crítico"])
    
    with col2:
        # Filtro por número de integrantes
        min_integrantes = st.number_input("Mínimo integrantes", min_value=1, max_value=10, value=1)
        max_integrantes = st.number_input("Máximo integrantes", min_value=1, max_value=10, value=10)
        
        # Filtro por enfermedades crónicas
        enfermedades_opciones = ["Diabetes", "Hipertensión", "Obesidad", "Enfermedad pulmonar", "Enfermedad cardíaca"]
        enfermedad_filtro = st.multiselect("Filtrar por Enfermedad", enfermedades_opciones)
    
    with col3:
        # Filtro por factores de riesgo
        factores_riesgo = st.multiselect(
            "Filtrar por Factores de Riesgo",
            ["Embarazo adolescente", "Violencia intrafamiliar", "Consumo drogas", "Desempleo", "Discapacidad", "Adulto mayor"]
        )
        
        # Búsqueda por apellido
        busqueda_apellido = st.text_input("Buscar por apellido", placeholder="Ej: González")
    
    # Aplicar filtros
    familias_filtradas = st.session_state.familias.copy()
    
    if sector_filtro != "Todos":
        familias_filtradas = [f for f in familias_filtradas if f['sector'] == sector_filtro]
    
    if riesgo_social_filtro != "Todos":
        familias_filtradas = [f for f in familias_filtradas if f['riesgos']['social']['nivel'] == riesgo_social_filtro]
    
    familias_filtradas = [f for f in familias_filtradas if min_integrantes <= f['num_integrantes'] <= max_integrantes]
    
    if enfermedad_filtro:
        familias_filtradas = [f for f in familias_filtradas if any(enfermedad in f['enfermedades_cronicas'] for enfermedad in enfermedad_filtro)]
    
    if factores_riesgo:
        for factor in factores_riesgo:
            if factor == "Embarazo adolescente":
                familias_filtradas = [f for f in familias_filtradas if f['embarazo_adolescente']]
            elif factor == "Violencia intrafamiliar":
                familias_filtradas = [f for f in familias_filtradas if f['violencia_intrafamiliar']]
            elif factor == "Consumo drogas":
                familias_filtradas = [f for f in familias_filtradas if f['consumo_drogas']]
            elif factor == "Desempleo":
                familias_filtradas = [f for f in familias_filtradas if f['desempleo']]
            elif factor == "Discapacidad":
                familias_filtradas = [f for f in familias_filtradas if f['discapacidad']]
            elif factor == "Adulto mayor":
                familias_filtradas = [f for f in familias_filtradas if f['adulto_mayor']]
    
    if busqueda_apellido:
        familias_filtradas = [f for f in familias_filtradas if busqueda_apellido.lower() in f['apellido'].lower()]
    
    # Mostrar resultados
    st.markdown(f"**Resultados encontrados: {len(familias_filtradas)} familias**")
    
    if familias_filtradas:
        # Crear tabla interactiva
        datos_tabla = []
        for familia in familias_filtradas:
            datos_tabla.append({
                "Apellido": familia['apellido'],
                "Sector": familia['sector'],
                "Integrantes": familia['num_integrantes'],
                "Riesgo Social": familia['riesgos']['social']['nivel'],
                "Riesgo Sanitario": familia['riesgos']['sanitario']['nivel'],
                "Enfermedades": ", ".join(familia.get('enfermedades_cronicas', [])) if familia.get('enfermedades_cronicas') else "Ninguna",
                "Observaciones": familia['observaciones'][:50] + "..." if len(familia['observaciones']) > 50 else familia['observaciones']
            })
        
        df_resultados = pd.DataFrame(datos_tabla)
        st.dataframe(df_resultados, use_container_width=True)
    else:
        st.info("No se encontraron familias con los filtros aplicados.")

def validar_datos_familia(familia_data):
    """Valida los datos ingresados y retorna sugerencias"""
    sugerencias = []
    alertas = []
    
    # Validaciones básicas
    if familia_data['num_integrantes'] > 10:
        alertas.append("⚠️ Número de integrantes muy alto. Verificar datos.")
    
    if familia_data['jefe_hogar']['edad'] < 18:
        alertas.append("⚠️ Edad del jefe de hogar muy baja. Verificar datos.")
    
    if familia_data['jefe_hogar']['edad'] > 100:
        alertas.append("⚠️ Edad del jefe de hogar muy alta. Verificar datos.")
    
    # Validaciones de riesgo
    riesgo_social, puntaje_social = calcular_riesgo_social(familia_data)
    riesgo_sanitario, puntaje_sanitario = calcular_riesgo_sanitario(familia_data)
    
    if riesgo_social == "Alto":
        sugerencias.append("🔴 **Alto riesgo social detectado:** Considerar intervención prioritaria")
    
    if riesgo_sanitario == "Alto":
        sugerencias.append("🔴 **Alto riesgo sanitario detectado:** Requiere seguimiento médico")
    
    if familia_data['violencia_intrafamiliar']:
        alertas.append("🚨 **Violencia intrafamiliar:** Derivar a especialista inmediatamente")
    
    if familia_data['embarazo_adolescente']:
        sugerencias.append("👶 **Embarazo adolescente:** Requiere apoyo especializado")
    
    if familia_data['hacinamiento'] == "Alto":
        sugerencias.append("🏠 **Hacinamiento alto:** Considerar apoyo habitacional")
    
    return sugerencias, alertas

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
        st.info("Ve a la sección '🗺️ Sectorización' para crear sectores antes de registrar familias.")
        return
    
    # Dashboard en tiempo real
    if st.session_state.familias:
        mostrar_dashboard_familias()
        st.markdown("---")
    
    # Pestañas para diferentes funcionalidades
    tab1, tab2, tab3 = st.tabs(["📝 Registrar Familia", "🔍 Buscar Familias", "📊 Análisis Avanzado"])
    
    with tab1:
        mostrar_formulario_registro()
    
    with tab2:
        mostrar_filtros_avanzados()
    
    with tab3:
        mostrar_analisis_avanzado()

def mostrar_formulario_registro():
    """Muestra el formulario de registro con validación inteligente"""
    st.markdown("### 📝 Registrar Nueva Familia")
    
    with st.form("registro_familia", clear_on_submit=True):
        # Información básica
        col1, col2 = st.columns(2)
        
        with col1:
            sector = st.selectbox("Sector", [s["nombre"] for s in st.session_state.sectores])
            apellido_familia = st.text_input("Apellido de la Familia", placeholder="Ej: González")
            num_integrantes = st.number_input("Número de Integrantes", min_value=1, max_value=15, value=3)
        
        with col2:
            nombre_jefe = st.text_input("Nombre del Jefe de Hogar", placeholder="Ej: Roberto González")
            edad_jefe = st.number_input("Edad del Jefe de Hogar", min_value=18, max_value=100, value=35)
            ocupacion_jefe = st.selectbox("Ocupación del Jefe de Hogar", 
                                        ["Empleado", "Obrero", "Profesional", "Dueño de casa", "Jubilado", "Desempleado", "Estudiante", "Otro"])
        
        # Información de vivienda
        st.markdown("**🏠 Información de Vivienda**")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            tipo_vivienda = st.selectbox("Tipo de Vivienda", ["Casa", "Departamento", "Mediagua", "Otro"])
            hacinamiento = st.selectbox("Nivel de Hacinamiento", ["Bajo", "Medio", "Alto", "Crítico"])
        
        with col2:
            red_apoyo = st.selectbox("Red de Apoyo", ["Fuerte", "Regular", "Débil"])
            participacion_social = st.selectbox("Participación Social", ["Alta", "Media", "Baja", "Nula"])
        
        with col3:
            acceso_aps = st.selectbox("Acceso a APS", ["Fácil", "Regular", "Difícil", "Muy difícil"])
        
        # Información de salud
        st.markdown("**🏥 Información de Salud**")
        col1, col2 = st.columns(2)
        
        with col1:
            enfermedades_cronicas = st.multiselect("Enfermedades Crónicas", 
                                                 ["Diabetes", "Hipertensión", "Obesidad", "Enfermedad pulmonar", "Enfermedad cardíaca", "Artritis", "Asma", "Tuberculosis"])
            embarazo_adolescente = st.checkbox("Embarazo Adolescente")
            violencia_intrafamiliar = st.checkbox("Violencia Intrafamiliar")
        
        with col2:
            consumo_drogas = st.checkbox("Consumo de Drogas")
            desempleo = st.checkbox("Desempleo")
            discapacidad = st.checkbox("Discapacidad")
            adulto_mayor = st.checkbox("Adulto Mayor")
        
        # Información adicional
        observaciones = st.text_area("Observaciones", placeholder="Observaciones importantes sobre la familia...")
        responsable = st.text_input("Responsable del Registro", placeholder="Ej: TENS Ana Martínez")
        
        # Botón de envío
        submitted = st.form_submit_button("💾 Registrar Familia", type="primary")
        
        if submitted:
            if apellido_familia and nombre_jefe:
                # Crear diccionario con datos de la familia
                familia_data = {
                    "sector": sector,
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
                    "observaciones": observaciones,
                    "fecha_registro": datetime.now().strftime("%Y-%m-%d"),
                    "responsable": responsable
                }
                
                # Calcular riesgos
                riesgo_social, puntaje_social = calcular_riesgo_social(familia_data)
                riesgo_sanitario, puntaje_sanitario = calcular_riesgo_sanitario(familia_data)
                
                familia_data["riesgos"] = {
                    "social": {"nivel": riesgo_social, "puntaje": puntaje_social},
                    "sanitario": {"nivel": riesgo_sanitario, "puntaje": puntaje_sanitario}
                }
                
                # Validación inteligente
                sugerencias, alertas = validar_datos_familia(familia_data)
                
                # Mostrar alertas y sugerencias
                if alertas:
                    for alerta in alertas:
                        st.warning(alerta)
                
                if sugerencias:
                    for sugerencia in sugerencias:
                        st.info(sugerencia)
                
                # Guardar familia
                st.session_state.familias.append(familia_data)
                st.success(f"✅ Familia {apellido_familia} registrada exitosamente!")
                
                # Mostrar resumen de riesgos
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Riesgo Social", riesgo_social, delta=f"Puntaje: {puntaje_social}")
                with col2:
                    st.metric("Riesgo Sanitario", riesgo_sanitario, delta=f"Puntaje: {puntaje_sanitario}")
                
            else:
                st.error("❌ Por favor completa los campos obligatorios (apellido y nombre del jefe de hogar)")

def mostrar_analisis_avanzado():
    """Muestra análisis avanzado de las familias registradas"""
    if not st.session_state.familias:
        st.info("No hay familias registradas para analizar.")
        return
    
    st.markdown("### 📊 Análisis Avanzado")
    
    # Análisis de correlaciones
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**🔗 Correlaciones de Riesgo**")
        
        # Crear matriz de correlación
        df_analisis = pd.DataFrame([
            {
                'Riesgo_Social': f['riesgos']['social']['puntaje'],
                'Riesgo_Sanitario': f['riesgos']['sanitario']['puntaje'],
                'Integrantes': f['num_integrantes'],
                'Edad_Jefe': f['jefe_hogar']['edad']
            }
            for f in st.session_state.familias
        ])
        
        correlacion = df_analisis.corr()
        
        fig_corr = px.imshow(
            correlacion,
            title="Matriz de Correlación",
            color_continuous_scale='RdBu',
            aspect="auto"
        )
        st.plotly_chart(fig_corr, use_container_width=True)
    
    with col2:
        st.markdown("**📈 Distribución de Edades**")
        
        edades = [f['jefe_hogar']['edad'] for f in st.session_state.familias]
        fig_edades = px.histogram(
            x=edades,
            title="Distribución de Edades del Jefe de Hogar",
            nbins=10,
            color_discrete_sequence=['#1f77b4']
        )
        fig_edades.update_layout(xaxis_title="Edad", yaxis_title="Frecuencia")
        st.plotly_chart(fig_edades, use_container_width=True)
    
    # Análisis de vulnerabilidad por sector
    st.markdown("**🎯 Análisis de Vulnerabilidad por Sector**")
    
    vulnerabilidad_sector = {}
    for familia in st.session_state.familias:
        sector = familia['sector']
        if sector not in vulnerabilidad_sector:
            vulnerabilidad_sector[sector] = {
                'total_familias': 0,
                'riesgo_alto_social': 0,
                'riesgo_alto_sanitario': 0,
                'violencia': 0,
                'embarazo_adolescente': 0
            }
        
        vulnerabilidad_sector[sector]['total_familias'] += 1
        
        if familia['riesgos']['social']['nivel'] == 'Alto':
            vulnerabilidad_sector[sector]['riesgo_alto_social'] += 1
        
        if familia['riesgos']['sanitario']['nivel'] == 'Alto':
            vulnerabilidad_sector[sector]['riesgo_alto_sanitario'] += 1
        
        if familia['violencia_intrafamiliar']:
            vulnerabilidad_sector[sector]['violencia'] += 1
        
        if familia['embarazo_adolescente']:
            vulnerabilidad_sector[sector]['embarazo_adolescente'] += 1
    
    # Crear gráfico de vulnerabilidad
    sectores = list(vulnerabilidad_sector.keys())
    riesgo_social_porcentaje = [vulnerabilidad_sector[s]['riesgo_alto_social'] / vulnerabilidad_sector[s]['total_familias'] * 100 for s in sectores]
    riesgo_sanitario_porcentaje = [vulnerabilidad_sector[s]['riesgo_alto_sanitario'] / vulnerabilidad_sector[s]['total_familias'] * 100 for s in sectores]
    
    fig_vulnerabilidad = go.Figure()
    fig_vulnerabilidad.add_trace(go.Bar(
        name='Riesgo Social Alto (%)',
        x=sectores,
        y=riesgo_social_porcentaje,
        marker_color='red'
    ))
    fig_vulnerabilidad.add_trace(go.Bar(
        name='Riesgo Sanitario Alto (%)',
        x=sectores,
        y=riesgo_sanitario_porcentaje,
        marker_color='orange'
    ))
    
    fig_vulnerabilidad.update_layout(
        title="Porcentaje de Familias en Alto Riesgo por Sector",
        barmode='group',
        xaxis_title="Sector",
        yaxis_title="Porcentaje (%)"
    )
    
    st.plotly_chart(fig_vulnerabilidad, use_container_width=True)
    
    # Recomendaciones automáticas
    st.markdown("### 💡 Recomendaciones Automáticas")
    
    # Identificar sector más vulnerable
    sector_mas_vulnerable = max(vulnerabilidad_sector.keys(), 
                              key=lambda s: vulnerabilidad_sector[s]['riesgo_alto_social'] + vulnerabilidad_sector[s]['riesgo_alto_sanitario'])
    
    st.info(f"🎯 **Sector más vulnerable:** {sector_mas_vulnerable}")
    
    # Recomendaciones específicas
    if vulnerabilidad_sector[sector_mas_vulnerable]['violencia'] > 0:
        st.warning(f"🚨 **Violencia intrafamiliar detectada en {sector_mas_vulnerable}:** Implementar programa de prevención y derivación")
    
    if vulnerabilidad_sector[sector_mas_vulnerable]['embarazo_adolescente'] > 0:
        st.warning(f"👶 **Embarazo adolescente en {sector_mas_vulnerable}:** Fortalecer programa de salud sexual y reproductiva")
    
    # Exportar datos
    if st.button("📥 Exportar Análisis"):
        # Crear DataFrame para exportación
        datos_export = []
        for familia in st.session_state.familias:
            datos_export.append({
                'Apellido': familia['apellido'],
                'Sector': familia['sector'],
                'Integrantes': familia['num_integrantes'],
                'Edad_Jefe': familia['jefe_hogar']['edad'],
                'Ocupacion_Jefe': familia['jefe_hogar']['ocupacion'],
                'Riesgo_Social': familia['riesgos']['social']['nivel'],
                'Puntaje_Social': familia['riesgos']['social']['puntaje'],
                'Riesgo_Sanitario': familia['riesgos']['sanitario']['nivel'],
                'Puntaje_Sanitario': familia['riesgos']['sanitario']['puntaje'],
                'Enfermedades_Cronicas': ', '.join(familia['enfermedades_cronicas']),
                'Violencia_Intrafamiliar': familia['violencia_intrafamiliar'],
                'Embarazo_Adolescente': familia['embarazo_adolescente'],
                'Fecha_Registro': familia['fecha_registro']
            })
        
        df_export = pd.DataFrame(datos_export)
        csv = df_export.to_csv(index=False)
        
        st.download_button(
            label="📊 Descargar CSV",
            data=csv,
            file_name=f"analisis_familias_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
            mime="text/csv"
        ) 