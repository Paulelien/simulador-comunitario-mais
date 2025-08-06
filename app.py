import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json
import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
import io
import base64

# Importar módulos
from sectorizacion import mostrar_sectorizacion
from equipo_cabecera import mostrar_equipo_cabecera
from registro_familias import mostrar_registro_familias
from diagnostico import mostrar_diagnostico
from trabajo_red import mostrar_trabajo_red
from plan_intervencion import mostrar_plan_intervencion
from evaluacion import mostrar_evaluacion
from participacion_comunitaria import mostrar_participacion_comunitaria
from epidemiologia import mostrar_epidemiologia
from sistema_inteligente import generar_recomendaciones_personalizadas
from casos_clinicos import mostrar_casos_clinicos
from telemedicina_tics import mostrar_telemedicina_tics
from salud_mental_comunitaria import mostrar_salud_mental_comunitaria
from gestion_clinica_aps import mostrar_gestion_clinica_aps
from educacion_promocion_salud import mostrar_educacion_promocion_salud

from datos_ejemplo import cargar_datos_ejemplo

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
    .risk-high { color: #d62728; font-weight: bold; }
    .risk-medium { color: #ff7f0e; font-weight: bold; }
    .risk-low { color: #2ca02c; font-weight: bold; }
    .success-box {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .info-box {
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
        border-radius: 5px;
        padding: 1rem;
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
    
    # Menú de navegación
    menu = ["🏠 Inicio", "🗺️ Sectorización", "👥 Equipo de Cabecera", "👨‍👩‍👧‍👦 Registro de Familias", 
            "🔍 Diagnóstico", "🌐 Trabajo en Red", "🏘️ Participación Comunitaria", "🦠 Epidemiología", "🧠 Salud Mental Comunitaria", "🏥 Gestión Clínica APS", "📚 Educación y Promoción de Salud", "📋 Plan de Intervención", "🏥 Casos Clínicos", "📱 Telemedicina y TICS", "📊 Evaluación"]
    
    choice = st.sidebar.selectbox("Navegación", menu)
    
    if choice == "🏠 Inicio":
        mostrar_inicio()
    elif choice == "🗺️ Sectorización":
        mostrar_sectorizacion()
    elif choice == "👥 Equipo de Cabecera":
        mostrar_equipo_cabecera()
    elif choice == "👨‍👩‍👧‍👦 Registro de Familias":
        mostrar_registro_familias()
    elif choice == "🔍 Diagnóstico":
        mostrar_diagnostico()
    elif choice == "🌐 Trabajo en Red":
        mostrar_trabajo_red()
    elif choice == "🏘️ Participación Comunitaria":
        mostrar_participacion_comunitaria()
    elif choice == "🦠 Epidemiología":
        mostrar_epidemiologia()
    elif choice == "🧠 Salud Mental Comunitaria":
        mostrar_salud_mental_comunitaria()
    elif choice == "🏥 Gestión Clínica APS":
        mostrar_gestion_clinica_aps()
    elif choice == "📚 Educación y Promoción de Salud":
        mostrar_educacion_promocion_salud()
    elif choice == "📋 Plan de Intervención":
        mostrar_plan_intervencion()
    elif choice == "🏥 Casos Clínicos":
        mostrar_casos_clinicos()
    elif choice == "📱 Telemedicina y TICS":
        mostrar_telemedicina_tics()
    elif choice == "📊 Evaluación":
        submenu = st.sidebar.selectbox(
            "Tipo de Evaluación",
            ["🎓 Autoevaluación General", "📋 Evaluación MAIS Oficial"]
        )
        if submenu == "🎓 Autoevaluación General":
            mostrar_evaluacion()
        else:
            from evaluacion_mais_oficial import mostrar_evaluacion_mais_oficial
            mostrar_evaluacion_mais_oficial()

    
    # Footer global con información de autoría
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
        
        1. **Sectorización del territorio**: Organizar y delimitar áreas geográficas
        2. **Formación de equipos**: Asignar profesionales por sector
        3. **Registro de familias**: Capturar información familiar relevante
        4. **Identificación de riesgos**: Detectar factores de riesgo y protectores
        5. **Trabajo en red**: Coordinar con instituciones comunitarias
        6. **Participación comunitaria**: Encuestas, grupos focales y análisis FODA
        7. **Epidemiología**: Indicadores, patologías prioritarias y vigilancia
        8. **Plan de intervención**: Diseñar estrategias de intervención
        9. **Casos clínicos**: Analizar situaciones reales de la práctica
        10. **Telemedicina y TICS**: Implementar tecnologías para mejorar acceso en zonas rurales
        
        ### 🚀 Cómo usar el simulador
        
        Utiliza el menú lateral para navegar por cada etapa del proceso. 
        Los datos que ingreses se guardarán automáticamente y podrás 
        exportarlos al final del proceso.
        """)
    
    with col2:
        st.markdown("""
        ### 📊 Progreso del Diagnóstico
        """)
        
        # Mostrar progreso
        total_pasos = 13
        pasos_completados = 0
        
        if st.session_state.sectores:
            pasos_completados += 1
        if st.session_state.equipos:
            pasos_completados += 1
        if st.session_state.familias:
            pasos_completados += 1
        if st.session_state.instituciones:
            pasos_completados += 1
        if 'participacion_comunitaria' in st.session_state and st.session_state.participacion_comunitaria['encuestas']:
            pasos_completados += 1
        if 'epidemiologia' in st.session_state and st.session_state.epidemiologia['indicadores_basicos']:
            pasos_completados += 1
        if st.session_state.plan_intervencion:
            pasos_completados += 1
        
        progreso = pasos_completados / total_pasos
        st.progress(progreso)
        st.write(f"**{pasos_completados}/{total_pasos}** pasos completados")
        
        if progreso == 1.0:
            st.success("¡Diagnóstico completo! Puedes exportar tus resultados.")
    
    # Información del curso
    st.markdown("""
    <div class="info-box">
        <h4>📚 Información del Curso</h4>
        <p><strong>Curso:</strong> Salud Familiar y Comunitaria</p>
        <p><strong>Público objetivo:</strong> Estudiantes TENS</p>
        <p><strong>Enfoque:</strong> Modelo MAIS - Atención Primaria en Salud</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Botón para cargar datos de ejemplo
    st.markdown("### 🎯 ¿Quieres ver un ejemplo completo?")
    cargar_datos_ejemplo()
    
    # Asistente Virtual Inteligente
    st.markdown("---")
    st.markdown("### 🤖 Asistente Virtual Inteligente")
    
    # Verificar progreso del usuario
    pasos_completados = 0
    total_pasos = 15  # Actualizado para incluir el nuevo módulo
    
    if st.session_state.sectores:
        pasos_completados += 1
    if st.session_state.equipos:
        pasos_completados += 1
    if st.session_state.familias:
        pasos_completados += 1
    if hasattr(st.session_state, 'diagnostico') and st.session_state.diagnostico:
        pasos_completados += 1
    if st.session_state.instituciones:
        pasos_completados += 1
    if hasattr(st.session_state, 'plan_intervencion') and st.session_state.plan_intervencion:
        pasos_completados += 1
    if hasattr(st.session_state, 'participacion_comunitaria') and st.session_state.participacion_comunitaria:
        pasos_completados += 1
    if hasattr(st.session_state, 'epidemiologia') and st.session_state.epidemiologia:
        pasos_completados += 1
    if hasattr(st.session_state, 'casos_clinicos') and st.session_state.casos_clinicos:
        pasos_completados += 1
    if hasattr(st.session_state, 'telemedicina_tics') and st.session_state.telemedicina_tics:
        pasos_completados += 1
    if hasattr(st.session_state, 'salud_mental_comunitaria') and st.session_state.salud_mental_comunitaria:
        pasos_completados += 1
    if hasattr(st.session_state, 'gestion_clinica_aps') and st.session_state.gestion_clinica_aps:
        pasos_completados += 1
    if hasattr(st.session_state, 'educacion_promocion_salud') and st.session_state.educacion_promocion_salud:
        pasos_completados += 1

    
    progreso = (pasos_completados / total_pasos) * 100
    
    st.progress(progreso / 100)
    st.write(f"**Progreso:** {pasos_completados}/{total_pasos} módulos completados ({progreso:.1f}%)")
    
    # Sugerencias del asistente
    if progreso < 30:
        st.info("🎯 **Sugerencia del Asistente:** Comienza con la sectorización del territorio para definir los límites de tu comunidad.")
    elif progreso < 50:
        st.info("👥 **Sugerencia del Asistente:** Ahora registra las familias para obtener datos que te permitan hacer un diagnóstico preciso.")
    elif progreso < 70:
        st.info("🔍 **Sugerencia del Asistente:** Realiza el diagnóstico comunitario para identificar problemas prioritarios.")
    elif progreso < 90:
        st.info("🤝 **Sugerencia del Asistente:** Trabaja en la red intersectoral y participación comunitaria para fortalecer las intervenciones.")
    else:
        st.success("🎉 **¡Excelente trabajo!** Has completado la mayoría de los módulos. Revisa el plan de intervención y la evaluación.")
    
    # Análisis inteligente rápido
    if st.button("🔍 Análisis Rápido Inteligente", key="analisis_rapido"):
        if st.session_state.familias:
            with st.spinner("Analizando datos..."):
                recomendaciones = generar_recomendaciones_personalizadas()
                
                if recomendaciones['diagnostico']['problemas_prioritarios']:
                    st.warning("🚨 **Problemas identificados:**")
                    for problema in recomendaciones['diagnostico']['problemas_prioritarios'][:3]:  # Solo mostrar los 3 primeros
                        st.write(f"• {problema['problema'].title()}: {problema['porcentaje']:.1f}% de las familias")
                    
                    st.info("💡 **Recomendación:** Usa el módulo 'Plan Anual' para generar intervenciones específicas.")
                else:
                    st.success("✅ **Situación estable:** No se identificaron problemas prioritarios.")
        else:
            st.warning("⚠️ Necesitas registrar familias primero para realizar el análisis.")
    
    # Guía contextual
    st.markdown("### 📚 Guía Contextual")
    
    with st.expander("❓ ¿Por dónde empezar?", expanded=False):
        st.markdown("""
        1. **Sectorización** → Define los límites de tu comunidad
        2. **Equipo Cabecera** → Asigna profesionales por sector
        3. **Registro Familias** → Recopila datos de las familias
        4. **Diagnóstico** → Analiza los problemas identificados
        5. **Red Intersectoral** → Identifica aliados comunitarios
        6. **Participación Comunitaria** → Involucra a la comunidad
        7. **Epidemiología** → Analiza datos de salud poblacional
        8. **Salud Mental Comunitaria** → Diagnóstico e intervención comunitaria
        9. **Gestión Clínica APS** → Control de pacientes crónicos y educación en salud
        10. **Educación y Promoción de Salud** → Objetivos SMART, Modelo de Creencias, Ciclo de Vida
        11. **Plan Intervención** → Diseña tu plan de acción
        12. **Casos Clínicos** → Analiza situaciones reales
        13. **Telemedicina y TICS** → Implementa tecnologías para zonas rurales
        14. **Evaluación** → Evalúa el proceso y resultados
        """)
    
    with st.expander("💡 Consejos para TENS", expanded=False):
        st.markdown("""
        • **Enfoque en prevención:** Prioriza intervenciones preventivas
        • **Trabajo en equipo:** Coordina con otros profesionales
        • **Participación comunitaria:** Involucra a las familias en las decisiones
        • **Seguimiento:** Mantén un registro de las intervenciones
        • **Evaluación continua:** Mide el impacto de tus acciones
        """)
    
    with st.expander("🚨 Alertas importantes", expanded=False):
        st.markdown("""
        • **Confidencialidad:** Protege siempre la información de las familias
        • **Derivación:** Identifica casos que requieren atención especializada
        • **Documentación:** Registra todas las intervenciones realizadas
        • **Redes de apoyo:** Fortalece las redes sociales de las familias
        • **Autocuidado:** No olvides tu propio bienestar
        """)

if __name__ == "__main__":
    main() 