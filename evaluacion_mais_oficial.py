import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

def mostrar_evaluacion_mais_oficial():
    """
    Módulo de evaluación basado en el instrumento oficial del MAIS
    Estructura: Componentes x Principios
    """
    
    st.markdown("# 📊 Evaluación Oficial del Modelo MAIS")
    st.markdown("### Instrumento de Evaluación del Desarrollo del Modelo")
    
    # Estructura del instrumento oficial
    st.markdown("---")
    st.markdown("### 🎯 Estructura del Instrumento")
    
    # Tabla de estructura
    estructura_data = {
        "Componentes": ["Comunidad", "Personas y familias", "Equipos de salud"],
        "Centrado en la persona": [3, 11, 2],
        "Integralidad": [2, 2, 6],
        "Continuidad": [3, 3, 6],
        "Total": [8, 16, 14],
        "Porcentaje": ["21.1%", "42.1%", "36.8%"]
    }
    
    df_estructura = pd.DataFrame(estructura_data)
    st.dataframe(df_estructura, use_container_width=True)
    
    st.markdown("**Puntaje máximo del instrumento: 38 puntos**")
    
    # Formulario de evaluación
    st.markdown("---")
    st.markdown("### 📝 Formulario de Evaluación")
    
    with st.expander("🔍 Evaluación por Componentes y Principios", expanded=True):
        
        # 1. COMUNIDAD
        st.markdown("#### 🏘️ 1. COMUNIDAD (8 puntos máximo)")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("**Centrado en la persona (3 puntos)**")
            comunidad_centrado = st.slider(
                "Participación comunitaria en decisiones de salud",
                min_value=0, max_value=3, value=1,
                help="0=No existe, 1=Básico, 2=Desarrollado, 3=Excelente"
            )
        
        with col2:
            st.markdown("**Integralidad (2 puntos)**")
            comunidad_integralidad = st.slider(
                "Coordinación intersectorial",
                min_value=0, max_value=2, value=1,
                help="0=No existe, 1=Básico, 2=Desarrollado"
            )
        
        with col3:
            st.markdown("**Continuidad (3 puntos)**")
            comunidad_continuidad = st.slider(
                "Seguimiento de programas comunitarios",
                min_value=0, max_value=3, value=1,
                help="0=No existe, 1=Básico, 2=Desarrollado, 3=Excelente"
            )
        
        # 2. PERSONAS Y FAMILIAS
        st.markdown("#### 👨‍👩‍👧‍👦 2. PERSONAS Y FAMILIAS (16 puntos máximo)")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("**Centrado en la persona (11 puntos)**")
            familias_centrado_1 = st.slider(
                "Atención personalizada",
                min_value=0, max_value=3, value=1,
                help="0=No existe, 1=Básico, 2=Desarrollado, 3=Excelente"
            )
            familias_centrado_2 = st.slider(
                "Respeto a la autonomía",
                min_value=0, max_value=3, value=1,
                help="0=No existe, 1=Básico, 2=Desarrollado, 3=Excelente"
            )
            familias_centrado_3 = st.slider(
                "Participación en decisiones de salud",
                min_value=0, max_value=3, value=1,
                help="0=No existe, 1=Básico, 2=Desarrollado, 3=Excelente"
            )
            familias_centrado_4 = st.slider(
                "Atención culturalmente apropiada",
                min_value=0, max_value=2, value=1,
                help="0=No existe, 1=Básico, 2=Desarrollado"
            )
        
        with col2:
            st.markdown("**Integralidad (2 puntos)**")
            familias_integralidad = st.slider(
                "Atención integral de la familia",
                min_value=0, max_value=2, value=1,
                help="0=No existe, 1=Básico, 2=Desarrollado"
            )
        
        with col3:
            st.markdown("**Continuidad (3 puntos)**")
            familias_continuidad = st.slider(
                "Seguimiento longitudinal",
                min_value=0, max_value=3, value=1,
                help="0=No existe, 1=Básico, 2=Desarrollado, 3=Excelente"
            )
        
        # 3. EQUIPOS DE SALUD
        st.markdown("#### 👥 3. EQUIPOS DE SALUD (14 puntos máximo)")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("**Centrado en la persona (2 puntos)**")
            equipos_centrado = st.slider(
                "Capacitación en atención centrada en la persona",
                min_value=0, max_value=2, value=1,
                help="0=No existe, 1=Básico, 2=Desarrollado"
            )
        
        with col2:
            st.markdown("**Integralidad (6 puntos)**")
            equipos_integralidad_1 = st.slider(
                "Trabajo en equipo multidisciplinario",
                min_value=0, max_value=3, value=1,
                help="0=No existe, 1=Básico, 2=Desarrollado, 3=Excelente"
            )
            equipos_integralidad_2 = st.slider(
                "Coordinación entre niveles de atención",
                min_value=0, max_value=3, value=1,
                help="0=No existe, 1=Básico, 2=Desarrollado, 3=Excelente"
            )
        
        with col3:
            st.markdown("**Continuidad (6 puntos)**")
            equipos_continuidad_1 = st.slider(
                "Sistemas de información integrados",
                min_value=0, max_value=3, value=1,
                help="0=No existe, 1=Básico, 2=Desarrollado, 3=Excelente"
            )
            equipos_continuidad_2 = st.slider(
                "Protocolos de seguimiento",
                min_value=0, max_value=3, value=1,
                help="0=No existe, 1=Básico, 2=Desarrollado, 3=Excelente"
            )
    
    # Calcular puntajes
    if st.button("📊 Calcular Puntaje Total", type="primary"):
        
        # Puntajes por componente
        puntaje_comunidad = comunidad_centrado + comunidad_integralidad + comunidad_continuidad
        puntaje_familias = (familias_centrado_1 + familias_centrado_2 + familias_centrado_3 + 
                           familias_centrado_4 + familias_integralidad + familias_continuidad)
        puntaje_equipos = (equipos_centrado + equipos_integralidad_1 + equipos_integralidad_2 + 
                          equipos_continuidad_1 + equipos_continuidad_2)
        
        # Puntajes por principio
        puntaje_centrado = (comunidad_centrado + familias_centrado_1 + familias_centrado_2 + 
                           familias_centrado_3 + familias_centrado_4 + equipos_centrado)
        puntaje_integralidad = (comunidad_integralidad + familias_integralidad + 
                               equipos_integralidad_1 + equipos_integralidad_2)
        puntaje_continuidad = (comunidad_continuidad + familias_continuidad + 
                              equipos_continuidad_1 + equipos_continuidad_2)
        
        # Puntaje total
        puntaje_total = puntaje_comunidad + puntaje_familias + puntaje_equipos
        
        # Mostrar resultados
        st.markdown("---")
        st.markdown("### 📈 Resultados de la Evaluación")
        
        # Tabla de resultados
        resultados_data = {
            "Componentes": ["Comunidad", "Personas y familias", "Equipos de salud", "**TOTAL**"],
            "Centrado en la persona": [comunidad_centrado, puntaje_familias - familias_integralidad - familias_continuidad, equipos_centrado, puntaje_centrado],
            "Integralidad": [comunidad_integralidad, familias_integralidad, equipos_integralidad_1 + equipos_integralidad_2, puntaje_integralidad],
            "Continuidad": [comunidad_continuidad, familias_continuidad, equipos_continuidad_1 + equipos_continuidad_2, puntaje_continuidad],
            "Total": [puntaje_comunidad, puntaje_familias, puntaje_equipos, puntaje_total],
            "Porcentaje": [f"{(puntaje_comunidad/8)*100:.1f}%", f"{(puntaje_familias/16)*100:.1f}%", f"{(puntaje_equipos/14)*100:.1f}%", f"{(puntaje_total/38)*100:.1f}%"]
        }
        
        df_resultados = pd.DataFrame(resultados_data)
        st.dataframe(df_resultados, use_container_width=True)
        
        # Gráfico de radar
        categorias = ["Comunidad", "Personas y familias", "Equipos de salud"]
        valores = [puntaje_comunidad/8*100, puntaje_familias/16*100, puntaje_equipos/14*100]
        
        fig_radar = go.Figure()
        fig_radar.add_trace(go.Scatterpolar(
            r=valores,
            theta=categorias,
            fill='toself',
            name='Puntaje Obtenido',
            line_color='blue'
        ))
        
        fig_radar.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100]
                )),
            showlegend=True,
            title="Evaluación por Componentes (%)"
        )
        
        st.plotly_chart(fig_radar, use_container_width=True)
        
        # Interpretación
        st.markdown("### 🎯 Interpretación del Resultado")
        
        porcentaje_total = (puntaje_total / 38) * 100
        
        if porcentaje_total >= 90:
            st.success(f"🎉 **EXCELENTE** - Puntaje: {puntaje_total}/38 ({porcentaje_total:.1f}%)")
            st.info("El modelo MAIS está muy bien implementado. Mantén las buenas prácticas.")
        elif porcentaje_total >= 75:
            st.success(f"✅ **BUENO** - Puntaje: {puntaje_total}/38 ({porcentaje_total:.1f}%)")
            st.info("El modelo MAIS está bien implementado. Identifica áreas de mejora.")
        elif porcentaje_total >= 60:
            st.warning(f"⚠️ **REGULAR** - Puntaje: {puntaje_total}/38 ({porcentaje_total:.1f}%)")
            st.info("El modelo MAIS necesita mejoras. Prioriza las áreas con menor puntaje.")
        else:
            st.error(f"❌ **INSUFICIENTE** - Puntaje: {puntaje_total}/38 ({porcentaje_total:.1f}%)")
            st.info("El modelo MAIS requiere implementación urgente. Revisa todos los componentes.")
        
        # Guardar evaluación
        evaluacion_mais = {
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "puntaje_total": puntaje_total,
            "porcentaje_total": porcentaje_total,
            "componentes": {
                "comunidad": puntaje_comunidad,
                "familias": puntaje_familias,
                "equipos": puntaje_equipos
            },
            "principios": {
                "centrado": puntaje_centrado,
                "integralidad": puntaje_integralidad,
                "continuidad": puntaje_continuidad
            }
        }
        
        st.session_state.evaluacion_mais = evaluacion_mais
        
        if st.button("💾 Guardar Evaluación MAIS"):
            st.success("✅ Evaluación MAIS guardada exitosamente!")
    
    # Footer con información de autoría
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 15px; background-color: #f0f2f6; border-radius: 8px; margin-top: 20px;">
        <p style="color: #666; font-size: 12px; margin: 0;">
            Aplicación educativa desarrollada por Ricardo Delannoy Suazo para formación en diagnóstico comunitario en salud familiar.<br>
            © 2025. Todos los derechos reservados.
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    mostrar_evaluacion_mais_oficial() 