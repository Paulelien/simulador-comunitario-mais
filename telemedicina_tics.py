import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random

def mostrar_telemedicina_tics():
    st.markdown("""
    <div class="section-header">
        <h2>📱 Telemedicina y TICS</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ### 🏥 ¿Qué es la Telemedicina y TICS?
    
    Las Tecnologías de la Información y Comunicación en Salud (TICS) incluyen teletriage, 
    telemedicina y monitoreo remoto. Estas herramientas son especialmente valiosas para 
    familias en zonas rurales con acceso limitado a servicios de salud.
    """)
    
    # Pestañas para diferentes funcionalidades
    tab1, tab2, tab3, tab4 = st.tabs([
        "🏥 Teletriage", 
        "📊 Monitoreo Remoto", 
        "🌾 Impacto Rural", 
        "📈 Análisis de Resultados"
    ])
    
    with tab1:
        mostrar_teletriage()
    
    with tab2:
        mostrar_monitoreo_remoto()
    
    with tab3:
        mostrar_impacto_rural()
    
    with tab4:
        mostrar_analisis_resultados()

def mostrar_teletriage():
    """Muestra el sistema de teletriage"""
    st.markdown("### 🏥 Sistema de Teletriage")
    
    st.markdown("""
    **Teletriage** es la evaluación remota de pacientes para determinar la urgencia 
    y el nivel de atención requerido. Es especialmente útil en zonas rurales.
    """)
    
    # Formulario de teletriage
    with st.expander("📋 Formulario de Teletriage", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            paciente = st.text_input("Nombre del Paciente", placeholder="Ej: María González")
            edad = st.number_input("Edad", min_value=0, max_value=120, value=45)
            telefono = st.text_input("Teléfono de Contacto", placeholder="+56 9 1234 5678")
            ubicacion = st.selectbox("Ubicación", ["Zona Rural", "Zona Urbana", "Zona Mixta"])
        
        with col2:
            sintoma_principal = st.text_input("Síntoma Principal", placeholder="Ej: Dolor de pecho")
            tiempo_sintomas = st.selectbox("Tiempo de Síntomas", 
                                         ["Menos de 1 hora", "1-6 horas", "6-24 horas", "Más de 24 horas"])
            nivel_dolor = st.slider("Nivel de Dolor (1-10)", 1, 10, 5)
        
        # Síntomas específicos
        st.markdown("**Síntomas Presentes:**")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            fiebre = st.checkbox("Fiebre")
            tos = st.checkbox("Tos")
            dificultad_respirar = st.checkbox("Dificultad para respirar")
        
        with col2:
            dolor_pecho = st.checkbox("Dolor de pecho")
            nauseas = st.checkbox("Náuseas")
            mareos = st.checkbox("Mareos")
        
        with col3:
            perdida_conciencia = st.checkbox("Pérdida de conciencia")
            sangrado = st.checkbox("Sangrado")
            hinchazon = st.checkbox("Hinchazón")
        
        # Factores de riesgo
        st.markdown("**Factores de Riesgo:**")
        col1, col2 = st.columns(2)
        
        with col1:
            diabetes = st.checkbox("Diabetes")
            hipertension = st.checkbox("Hipertensión")
            embarazo = st.checkbox("Embarazo")
        
        with col2:
            edad_avanzada = st.checkbox("Edad avanzada (>65 años)")
            enfermedades_cronicas = st.checkbox("Enfermedades crónicas")
            medicamentos = st.checkbox("Toma medicamentos")
        
        # Evaluación automática
        if st.button("🔍 Evaluar Urgencia", type="primary"):
            if paciente and sintoma_principal:
                urgencia, recomendacion, tiempo_espera = evaluar_urgencia_teletriage(
                    sintoma_principal, nivel_dolor, tiempo_sintomas,
                    fiebre, tos, dificultad_respirar, dolor_pecho,
                    perdida_conciencia, sangrado, diabetes, hipertension,
                    embarazo, edad_avanzada
                )
                
                # Guardar caso de teletriage
                caso_teletriage = {
                    "fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "paciente": paciente,
                    "edad": edad,
                    "telefono": telefono,
                    "ubicacion": ubicacion,
                    "sintoma_principal": sintoma_principal,
                    "urgencia": urgencia,
                    "recomendacion": recomendacion,
                    "tiempo_espera": tiempo_espera,
                    "nivel_dolor": nivel_dolor,
                    "sintomas": {
                        "fiebre": fiebre,
                        "tos": tos,
                        "dificultad_respirar": dificultad_respirar,
                        "dolor_pecho": dolor_pecho,
                        "perdida_conciencia": perdida_conciencia,
                        "sangrado": sangrado
                    },
                    "factores_riesgo": {
                        "diabetes": diabetes,
                        "hipertension": hipertension,
                        "embarazo": embarazo,
                        "edad_avanzada": edad_avanzada
                    }
                }
                
                if 'casos_teletriage' not in st.session_state:
                    st.session_state.casos_teletriage = []
                
                st.session_state.casos_teletriage.append(caso_teletriage)
                
                # Mostrar resultado
                mostrar_resultado_teletriage(urgencia, recomendacion, tiempo_espera, ubicacion)
                
            else:
                st.error("❌ Por favor completa los campos obligatorios")

def evaluar_urgencia_teletriage(sintoma, dolor, tiempo, fiebre, tos, dificultad_respirar, 
                               dolor_pecho, perdida_conciencia, sangrado, diabetes, 
                               hipertension, embarazo, edad_avanzada):
    """Evalúa la urgencia del caso basado en síntomas y factores de riesgo"""
    
    puntaje = 0
    
    # Síntomas críticos
    if perdida_conciencia:
        puntaje += 10
    if dolor_pecho:
        puntaje += 8
    if dificultad_respirar:
        puntaje += 7
    if sangrado:
        puntaje += 6
    
    # Síntomas moderados
    if fiebre:
        puntaje += 3
    if tos:
        puntaje += 2
    
    # Nivel de dolor
    if dolor >= 8:
        puntaje += 4
    elif dolor >= 5:
        puntaje += 2
    
    # Tiempo de síntomas
    if tiempo == "Menos de 1 hora":
        puntaje += 3
    elif tiempo == "1-6 horas":
        puntaje += 2
    
    # Factores de riesgo
    if diabetes:
        puntaje += 2
    if hipertension:
        puntaje += 2
    if embarazo:
        puntaje += 3
    if edad_avanzada:
        puntaje += 2
    
    # Determinar urgencia
    if puntaje >= 15:
        return "CRÍTICA", "Acudir inmediatamente al servicio de urgencias", "Inmediato"
    elif puntaje >= 10:
        return "ALTA", "Acudir al servicio de urgencias en las próximas 2 horas", "2 horas"
    elif puntaje >= 6:
        return "MODERADA", "Acudir al CESFAM en las próximas 24 horas", "24 horas"
    else:
        return "BAJA", "Agendar consulta médica regular", "48-72 horas"

def mostrar_resultado_teletriage(urgencia, recomendacion, tiempo_espera, ubicacion):
    """Muestra el resultado de la evaluación de teletriage"""
    
    # Color según urgencia
    colores = {
        "CRÍTICA": "red",
        "ALTA": "orange", 
        "MODERADA": "yellow",
        "BAJA": "green"
    }
    
    color = colores.get(urgencia, "blue")
    
    st.markdown(f"""
    <div style="padding: 20px; border-radius: 10px; background-color: {color}; color: white;">
        <h3>🎯 Resultado de Evaluación</h3>
        <p><strong>Nivel de Urgencia:</strong> {urgencia}</p>
        <p><strong>Recomendación:</strong> {recomendacion}</p>
        <p><strong>Tiempo de Espera Máximo:</strong> {tiempo_espera}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Beneficios para zona rural
    if ubicacion == "Zona Rural":
        st.info("""
        🌾 **Beneficios del Teletriage en Zona Rural:**
        - Reduce tiempo de traslado innecesario
        - Optimiza recursos de salud
        - Mejora acceso a atención especializada
        - Disminuye costos de transporte
        """)

def mostrar_monitoreo_remoto():
    """Muestra el sistema de monitoreo remoto"""
    st.markdown("### 📊 Monitoreo Remoto de Pacientes")
    
    st.markdown("""
    El **monitoreo remoto** permite seguir la evolución de pacientes crónicos 
    desde sus hogares, especialmente útil en zonas rurales.
    """)
    
    # Tipos de monitoreo
    tipo_monitoreo = st.selectbox(
        "Tipo de Monitoreo",
        ["Presión Arterial", "Glucemia", "Peso", "Oxigenación", "Frecuencia Cardíaca", "Temperatura"]
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        paciente_monitoreo = st.text_input("Paciente", placeholder="Ej: Don Luis")
        fecha_inicio = st.date_input("Fecha de Inicio", value=datetime.now().date())
        frecuencia = st.selectbox("Frecuencia de Medición", ["Diaria", "2 veces al día", "Semanal"])
    
    with col2:
        objetivo = st.text_input("Objetivo del Monitoreo", placeholder="Ej: Control de diabetes")
        umbral_alerta = st.number_input("Umbral de Alerta", min_value=0, value=140)
        responsable = st.text_input("Responsable", placeholder="Ej: TENS Ana")
    
    # Simulación de datos de monitoreo
    if st.button("📈 Simular Datos de Monitoreo", type="primary"):
        if paciente_monitoreo and objetivo:
            datos_monitoreo = generar_datos_monitoreo(tipo_monitoreo, fecha_inicio, 30)
            
            if 'datos_monitoreo' not in st.session_state:
                st.session_state.datos_monitoreo = []
            
            st.session_state.datos_monitoreo.append({
                "paciente": paciente_monitoreo,
                "tipo": tipo_monitoreo,
                "objetivo": objetivo,
                "datos": datos_monitoreo,
                "fecha_inicio": fecha_inicio.strftime("%Y-%m-%d"),
                "frecuencia": frecuencia,
                "umbral_alerta": umbral_alerta,
                "responsable": responsable
            })
            
            # Mostrar gráfico
            mostrar_grafico_monitoreo(datos_monitoreo, tipo_monitoreo, umbral_alerta)
            
            st.success(f"✅ Monitoreo iniciado para {paciente_monitoreo}")

def generar_datos_monitoreo(tipo, fecha_inicio, dias):
    """Genera datos simulados de monitoreo"""
    datos = []
    
    for i in range(dias):
        fecha = fecha_inicio + timedelta(days=i)
        
        if tipo == "Presión Arterial":
            sistolica = random.randint(110, 180)
            diastolica = random.randint(70, 110)
            valor = f"{sistolica}/{diastolica}"
        elif tipo == "Glucemia":
            valor = random.randint(80, 200)
        elif tipo == "Peso":
            valor = random.uniform(60, 90)
        elif tipo == "Oxigenación":
            valor = random.randint(92, 98)
        elif tipo == "Frecuencia Cardíaca":
            valor = random.randint(60, 100)
        elif tipo == "Temperatura":
            valor = round(random.uniform(36.0, 38.5), 1)
        
        datos.append({
            "fecha": fecha.strftime("%Y-%m-%d"),
            "valor": valor,
            "alerta": valor > 140 if isinstance(valor, (int, float)) else False
        })
    
    return datos

def mostrar_grafico_monitoreo(datos, tipo, umbral):
    """Muestra gráfico de monitoreo"""
    
    fechas = [d["fecha"] for d in datos]
    valores = [d["valor"] if isinstance(d["valor"], (int, float)) else d["valor"].split('/')[0] for d in datos]
    alertas = [d["alerta"] for d in datos]
    
    fig = go.Figure()
    
    # Línea de datos
    fig.add_trace(go.Scatter(
        x=fechas,
        y=valores,
        mode='lines+markers',
        name=f'{tipo}',
        line=dict(color='blue', width=2),
        marker=dict(size=6)
    ))
    
    # Línea de umbral
    if isinstance(valores[0], (int, float)):
        fig.add_hline(y=umbral, line_dash="dash", line_color="red", 
                     annotation_text=f"Umbral de Alerta: {umbral}")
    
    fig.update_layout(
        title=f"Monitoreo de {tipo}",
        xaxis_title="Fecha",
        yaxis_title=tipo,
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)

def mostrar_impacto_rural():
    """Muestra el impacto de TICS en zonas rurales"""
    st.markdown("### 🌾 Impacto de TICS en Zonas Rurales")
    
    # Métricas de impacto
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Reducción Tiempo Traslado", "45%", "vs atención tradicional")
    
    with col2:
        st.metric("Mejora Acceso", "78%", "familias rurales")
    
    with col3:
        st.metric("Reducción Costos", "32%", "gastos en salud")
    
    with col4:
        st.metric("Satisfacción", "89%", "usuarios rurales")
    
    # Análisis por tipo de intervención
    st.markdown("### 📊 Análisis de Impacto por Intervención")
    
    intervenciones = ["Teletriage", "Telemedicina", "Monitoreo Remoto", "Educación Digital"]
    impacto_acceso = [85, 72, 68, 45]
    impacto_costo = [40, 35, 28, 15]
    impacto_satisfaccion = [92, 88, 85, 78]
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name='Mejora Acceso (%)',
        x=intervenciones,
        y=impacto_acceso,
        marker_color='green'
    ))
    
    fig.add_trace(go.Bar(
        name='Reducción Costos (%)',
        x=intervenciones,
        y=impacto_costo,
        marker_color='blue'
    ))
    
    fig.add_trace(go.Bar(
        name='Satisfacción (%)',
        x=intervenciones,
        y=impacto_satisfaccion,
        marker_color='orange'
    ))
    
    fig.update_layout(
        title="Impacto de TICS en Zonas Rurales",
        barmode='group',
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Beneficios específicos
    st.markdown("### ✅ Beneficios Específicos para Zonas Rurales")
    
    beneficios = {
        "🏥 Acceso a Especialistas": "Consultas remotas con médicos especialistas",
        "⏰ Reducción de Tiempos": "Menos traslados y esperas",
        "💰 Ahorro de Costos": "Reducción de gastos en transporte y tiempo",
        "📱 Monitoreo Continuo": "Seguimiento de pacientes crónicos",
        "🎓 Educación en Salud": "Capacitación remota para familias",
        "🚨 Respuesta Rápida": "Evaluación inmediata de urgencias"
    }
    
    for beneficio, descripcion in beneficios.items():
        st.markdown(f"**{beneficio}:** {descripcion}")

def mostrar_analisis_resultados():
    """Muestra análisis de resultados de TICS"""
    st.markdown("### 📈 Análisis de Resultados")
    
    if 'casos_teletriage' not in st.session_state or not st.session_state.casos_teletriage:
        st.info("No hay datos de teletriage para analizar. Realiza algunas evaluaciones primero.")
        return
    
    # Análisis de casos de teletriage
    df_teletriage = pd.DataFrame(st.session_state.casos_teletriage)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Distribución por urgencia
        urgencia_counts = df_teletriage['urgencia'].value_counts()
        fig_urgencia = px.pie(
            values=urgencia_counts.values,
            names=urgencia_counts.index,
            title="Distribución por Nivel de Urgencia"
        )
        st.plotly_chart(fig_urgencia, use_container_width=True)
    
    with col2:
        # Distribución por ubicación
        ubicacion_counts = df_teletriage['ubicacion'].value_counts()
        fig_ubicacion = px.bar(
            x=ubicacion_counts.index,
            y=ubicacion_counts.values,
            title="Casos por Ubicación",
            color=ubicacion_counts.values,
            color_continuous_scale='viridis'
        )
        st.plotly_chart(fig_ubicacion, use_container_width=True)
    
    # Análisis de síntomas más comunes
    st.markdown("### 🔍 Análisis de Síntomas")
    
    sintomas_comunes = []
    for caso in st.session_state.casos_teletriage:
        for sintoma, presente in caso['sintomas'].items():
            if presente:
                sintomas_comunes.append(sintoma)
    
    if sintomas_comunes:
        sintoma_counts = pd.Series(sintomas_comunes).value_counts()
        fig_sintomas = px.bar(
            x=sintoma_counts.index,
            y=sintoma_counts.values,
            title="Síntomas Más Frecuentes",
            color=sintoma_counts.values,
            color_continuous_scale='plasma'
        )
        st.plotly_chart(fig_sintomas, use_container_width=True)
    
    # Recomendaciones basadas en datos
    st.markdown("### 💡 Recomendaciones Basadas en Datos")
    
    if len(st.session_state.casos_teletriage) > 0:
        casos_rurales = [c for c in st.session_state.casos_teletriage if c['ubicacion'] == 'Zona Rural']
        casos_urbanos = [c for c in st.session_state.casos_teletriage if c['ubicacion'] == 'Zona Urbana']
        
        if casos_rurales:
            urgencia_rural = [c['urgencia'] for c in casos_rurales]
            alta_urgencia_rural = sum(1 for u in urgencia_rural if u in ['ALTA', 'CRÍTICA'])
            
            st.info(f"""
            🌾 **Zona Rural:** {len(casos_rurales)} casos, {alta_urgencia_rural} de alta urgencia
            - Considerar fortalecer servicios de emergencia rural
            - Implementar más puntos de teletriage
            """)
        
        if casos_urbanos:
            st.info(f"""
            🏙️ **Zona Urbana:** {len(casos_urbanos)} casos
            - Optimizar derivaciones a especialistas
            - Mejorar coordinación entre servicios
            """)
    
    # Exportar datos
    if st.button("📥 Exportar Datos de TICS"):
        if 'casos_teletriage' in st.session_state and st.session_state.casos_teletriage:
            df_export = pd.DataFrame(st.session_state.casos_teletriage)
            csv = df_export.to_csv(index=False)
            
            st.download_button(
                label="📊 Descargar CSV",
                data=csv,
                file_name=f"datos_tics_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
                mime="text/csv"
            ) 