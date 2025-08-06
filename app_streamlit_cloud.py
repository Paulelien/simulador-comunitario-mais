import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json
import os

# Configuración de la página
st.set_page_config(
    page_title="Simulador Comunitario - Salud Familiar y Comunitaria",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #1f77b4, #ff7f0e);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #1f77b4;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Inicialización del estado de la sesión
if 'sectores' not in st.session_state:
    st.session_state.sectores = []
if 'equipos' not in st.session_state:
    st.session_state.equipos = []
if 'familias' not in st.session_state:
    st.session_state.familias = []
if 'instituciones' not in st.session_state:
    st.session_state.instituciones = []
if 'plan_intervencion' not in st.session_state:
    st.session_state.plan_intervencion = []
if 'educacion_promocion_salud' not in st.session_state:
    st.session_state.educacion_promocion_salud = {
        'objetivos_smart': [],
        'intervenciones_educativas': [],
        'evaluacion_creencias': [],
        'programas_ciclo_vida': [],
        'indicadores_educacion': []
    }

def main():
    # Header principal
    st.markdown("""
    <div class="main-header">
        <h1>🏥 Simulador Comunitario</h1>
        <h3>Salud Familiar y Comunitaria - Curso TENS</h3>
        <p>Diagnóstico Comunitario en APS - Modelo MAIS</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Menú de navegación simplificado
    menu = ["🏠 Inicio", "📚 Educación y Promoción de Salud", "📊 Dashboard"]
    
    choice = st.sidebar.selectbox("Navegación", menu)
    
    if choice == "🏠 Inicio":
        mostrar_inicio()
    elif choice == "📚 Educación y Promoción de Salud":
        mostrar_educacion_promocion_salud()
    elif choice == "📊 Dashboard":
        mostrar_dashboard()
    
    # Footer global
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 15px; background-color: #f0f2f6; border-radius: 8px; margin-top: 20px;">
        <p style="color: #666; font-size: 12px; margin: 0;">
            Aplicación educativa desarrollada por Ricardo Delannoy Suazo para formación en diagnóstico comunitario en salud familiar.<br>
            © 2025. Todos los derechos reservados.
        </p>
    </div>
    """, unsafe_allow_html=True)

def mostrar_inicio():
    st.markdown("""
    <div class="section-header">
        <h2>Bienvenido al Simulador Comunitario</h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### 🎯 Objetivo del Simulador
        
        Esta aplicación te permitirá practicar el proceso completo de elaboración de un 
        **diagnóstico comunitario en Atención Primaria en Salud (APS)** siguiendo el 
        **Modelo de Atención Integral en Salud Familiar (MAIS)**.
        
        ### 📋 ¿Qué aprenderás?
        
        1. **Educación para la Salud** → Objetivos SMART, Modelo de Creencias, Ciclo de Vida
        2. **Promoción de la Salud** → Estrategias educativas y preventivas
        3. **Diagnóstico Comunitario** → Análisis de problemas de salud
        4. **Intervenciones Educativas** → Diseño e implementación
        5. **Evaluación de Programas** → Indicadores y seguimiento
        
        ### 🚀 Cómo usar el simulador
        
        Utiliza el menú lateral para navegar por cada etapa del proceso. 
        Los datos que ingreses se guardarán automáticamente y podrás 
        exportarlos al final del proceso.
        """)
    
    with col2:
        st.markdown("""
        ### 📊 Estado de la Aplicación
        """)
        
        # Mostrar estado de los módulos
        st.write(f"📚 Educación y Promoción: {'✅ Activo' if st.session_state.educacion_promocion_salud else '⏳ Pendiente'}")
        st.write(f"📊 Dashboard: ✅ Disponible")
        
        # Botón para cargar datos de ejemplo
        if st.button("📥 Cargar Datos de Ejemplo"):
            st.success("✅ Datos de ejemplo cargados correctamente")

def mostrar_educacion_promocion_salud():
    """Módulo simplificado de Educación para la Salud"""
    
    st.title("📚 Educación para la Salud y Promoción de la Salud")
    st.markdown("### Estrategias Educativas y Promocionales en APS - Enfoque TENS")
    
    # Pestañas principales
    tab1, tab2, tab3 = st.tabs([
        "🎯 Objetivos SMART", 
        "📖 Intervenciones Educativas",
        "🧠 Modelo de Creencias"
    ])
    
    with tab1:
        st.header("🎯 Formulación de Objetivos SMART")
        st.markdown("**Específicos, Medibles, Alcanzables, Relevantes y con Tiempo definido**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📋 Nuevo Objetivo SMART")
            
            titulo = st.text_input("Título del Objetivo:", key="smart_titulo")
            especifico = st.text_area("**S - Específico:** ¿Qué se quiere lograr exactamente?", key="smart_especifico")
            medible = st.text_area("**M - Medible:** ¿Cómo se medirá el progreso?", key="smart_medible")
            alcanzable = st.text_area("**A - Alcanzable:** ¿Es realista con los recursos disponibles?", key="smart_alcanzable")
            relevante = st.text_area("**R - Relevante:** ¿Por qué es importante este objetivo?", key="smart_relevante")
            tiempo = st.text_area("**T - Tiempo:** ¿Cuándo se logrará?", key="smart_tiempo")
            
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
                        'fecha_creacion': datetime.now().strftime("%Y-%m-%d %H:%M"),
                        'estado': 'En Progreso'
                    }
                    
                    st.session_state.educacion_promocion_salud['objetivos_smart'].append(objetivo)
                    st.success("✅ Objetivo SMART guardado exitosamente")
                    st.rerun()
                else:
                    st.error("❌ Por favor completa todos los campos obligatorios")
        
        with col2:
            st.subheader("📊 Objetivos SMART Registrados")
            
            if st.session_state.educacion_promocion_salud['objetivos_smart']:
                for objetivo in st.session_state.educacion_promocion_salud['objetivos_smart']:
                    with st.expander(f"🎯 {objetivo['titulo']}", expanded=False):
                        st.write(f"**Específico:** {objetivo['especifico']}")
                        st.write(f"**Medible:** {objetivo['medible']}")
                        st.write(f"**Alcanzable:** {objetivo['alcanzable']}")
                        st.write(f"**Relevante:** {objetivo['relevante']}")
                        st.write(f"**Tiempo:** {objetivo['tiempo']}")
                        st.write(f"**Estado:** {objetivo['estado']}")
                        st.write(f"**Fecha:** {objetivo['fecha_creacion']}")
            else:
                st.info("📝 No hay objetivos SMART registrados. Crea el primero en el panel izquierdo.")
    
    with tab2:
        st.header("📖 Intervenciones Educativas")
        st.markdown("**Diseño e implementación de estrategias educativas**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🎨 Nueva Intervención Educativa")
            
            nombre = st.text_input("Nombre de la Intervención:", key="interv_nombre")
            tipo_intervencion = st.selectbox(
                "Tipo de Intervención:",
                ["Educación Individual", "Educación Grupal", "Talleres Comunitarios", "Material Educativo"],
                key="interv_tipo"
            )
            contenido = st.text_area("Contenido Educativo:", key="interv_contenido")
            objetivos = st.text_area("Objetivos de Aprendizaje:", key="interv_objetivos")
            
            if st.button("💾 Guardar Intervención", key="guardar_intervencion"):
                if nombre and contenido and objetivos:
                    intervencion = {
                        'id': len(st.session_state.educacion_promocion_salud['intervenciones_educativas']) + 1,
                        'nombre': nombre,
                        'tipo': tipo_intervencion,
                        'contenido': contenido,
                        'objetivos': objetivos,
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
                        st.write(f"**Objetivos:** {interv['objetivos']}")
                        st.write(f"**Contenido:** {interv['contenido']}")
                        st.write(f"**Estado:** {interv['estado']}")
            else:
                st.info("📝 No hay intervenciones registradas. Crea la primera en el panel izquierdo.")
    
    with tab3:
        st.header("🧠 Modelo de Creencias en Salud")
        st.markdown("**Evaluación de susceptibilidad, severidad, beneficios y barreras**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🔍 Evaluación de Creencias")
            
            problema_salud = st.text_input("Problema de Salud:", key="creencias_problema")
            poblacion = st.selectbox(
                "Población a Evaluar:",
                ["Familias con niños pequeños", "Adultos con enfermedades crónicas", "Mujeres embarazadas"],
                key="creencias_poblacion"
            )
            
            susceptibilidad = st.slider("**Susceptibilidad Percibida:**", 1, 10, 5, key="creencias_susceptibilidad")
            severidad = st.slider("**Severidad Percibida:**", 1, 10, 5, key="creencias_severidad")
            beneficios = st.slider("**Beneficios Percibidos:**", 1, 10, 5, key="creencias_beneficios")
            barreras = st.slider("**Barreras Percibidas:**", 1, 10, 5, key="creencias_barreras")
            
            if st.button("💾 Guardar Evaluación", key="guardar_creencias"):
                if problema_salud:
                    evaluacion = {
                        'id': len(st.session_state.educacion_promocion_salud['evaluacion_creencias']) + 1,
                        'poblacion': poblacion,
                        'problema_salud': problema_salud,
                        'susceptibilidad': susceptibilidad,
                        'severidad': severidad,
                        'beneficios': beneficios,
                        'barreras': barreras,
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
                       ultima_eval['beneficios'], ultima_eval['barreras']],
                    theta=['Susceptibilidad', 'Severidad', 'Beneficios', 'Barreras'],
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
            else:
                st.info("📝 No hay evaluaciones de creencias registradas. Realiza la primera en el panel izquierdo.")

def mostrar_dashboard():
    """Dashboard simplificado"""
    
    st.title("📊 Dashboard - Simulador Comunitario")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Objetivos SMART", len(st.session_state.educacion_promocion_salud['objetivos_smart']))
    
    with col2:
        st.metric("Intervenciones", len(st.session_state.educacion_promocion_salud['intervenciones_educativas']))
    
    with col3:
        st.metric("Evaluaciones", len(st.session_state.educacion_promocion_salud['evaluacion_creencias']))
    
    # Gráfico de progreso
    if st.session_state.educacion_promocion_salud['objetivos_smart']:
        st.subheader("📈 Progreso de Objetivos SMART")
        
        estados = {}
        for objetivo in st.session_state.educacion_promocion_salud['objetivos_smart']:
            estado = objetivo['estado']
            estados[estado] = estados.get(estado, 0) + 1
        
        if estados:
            fig = px.pie(
                values=list(estados.values()),
                names=list(estados.keys()),
                title="Distribución de Estados de Objetivos SMART"
            )
            st.plotly_chart(fig, use_container_width=True)
    
    # Exportar datos
    if st.button("📤 Exportar Datos"):
        st.json(st.session_state.educacion_promocion_salud)

if __name__ == "__main__":
    main() 