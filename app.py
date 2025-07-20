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
            "🔍 Diagnóstico", "🌐 Trabajo en Red", "📋 Plan de Intervención", "📊 Evaluación"]
    
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
    elif choice == "📋 Plan de Intervención":
        mostrar_plan_intervencion()
    elif choice == "📊 Evaluación":
        mostrar_evaluacion()

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
        6. **Plan de intervención**: Diseñar estrategias de intervención
        
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
        total_pasos = 7
        pasos_completados = 0
        
        if st.session_state.sectores:
            pasos_completados += 1
        if st.session_state.equipos:
            pasos_completados += 1
        if st.session_state.familias:
            pasos_completados += 1
        if st.session_state.instituciones:
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

if __name__ == "__main__":
    main() 