import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import json
import io
import base64
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors

def generar_pdf():
    """Genera un PDF con el resumen completo del diagnóstico comunitario"""
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []
    
    # Título
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=16,
        spaceAfter=30,
        alignment=1
    )
    story.append(Paragraph("DIAGNÓSTICO COMUNITARIO EN APS", title_style))
    story.append(Paragraph("Modelo MAIS - Salud Familiar y Comunitaria", styles['Heading2']))
    story.append(Spacer(1, 20))
    
    # Información general
    story.append(Paragraph("INFORMACIÓN GENERAL", styles['Heading2']))
    story.append(Spacer(1, 12))
    
    if st.session_state.sectores:
        story.append(Paragraph(f"Total de Sectores: {len(st.session_state.sectores)}", styles['Normal']))
        total_poblacion = sum(s["poblacion_total"] for s in st.session_state.sectores)
        story.append(Paragraph(f"Población Total: {total_poblacion:,}", styles['Normal']))
        total_familias = sum(s["num_familias"] for s in st.session_state.sectores)
        story.append(Paragraph(f"Total de Familias: {total_familias:,}", styles['Normal']))
    
    if st.session_state.familias:
        story.append(Paragraph(f"Familias Registradas: {len(st.session_state.familias)}", styles['Normal']))
        familias_alto_riesgo = sum(1 for f in st.session_state.familias 
                                 if f["riesgos"]["social"]["nivel"] == "Alto" or 
                                 f["riesgos"]["sanitario"]["nivel"] == "Alto")
        story.append(Paragraph(f"Familias en Alto Riesgo: {familias_alto_riesgo}", styles['Normal']))
    
    story.append(Spacer(1, 20))
    
    # Diagnóstico
    if hasattr(st.session_state, 'diagnostico') and st.session_state.diagnostico:
        story.append(Paragraph("DIAGNÓSTICO COMUNITARIO", styles['Heading2']))
        story.append(Spacer(1, 12))
        
        diagnostico = st.session_state.diagnostico
        story.append(Paragraph(f"Problema Principal: {diagnostico['problema_principal']}", styles['Normal']))
        story.append(Paragraph(f"Grupo Prioritario: {diagnostico['grupo_prioritario']}", styles['Normal']))
        story.append(Paragraph(f"Enfoque de Intervención: {diagnostico['enfoque_intervencion']}", styles['Normal']))
        
        story.append(Spacer(1, 12))
        story.append(Paragraph("Estrategias Propuestas:", styles['Normal']))
        for estrategia in diagnostico['estrategias_propuestas']:
            story.append(Paragraph(f"• {estrategia}", styles['Normal']))
    
    story.append(Spacer(1, 20))
    
    # Plan de intervención
    if st.session_state.plan_intervencion:
        story.append(Paragraph("PLAN DE INTERVENCIÓN", styles['Heading2']))
        story.append(Spacer(1, 12))
        
        story.append(Paragraph(f"Total de Actividades: {len(st.session_state.plan_intervencion)}", styles['Normal']))
        total_presupuesto = sum(a["presupuesto_estimado"] for a in st.session_state.plan_intervencion)
        story.append(Paragraph(f"Presupuesto Total: ${total_presupuesto:,}", styles['Normal']))
        
        story.append(Spacer(1, 12))
        story.append(Paragraph("Actividades Planificadas:", styles['Normal']))
        for actividad in st.session_state.plan_intervencion:
            story.append(Paragraph(f"• {actividad['nombre']} ({actividad['tipo']})", styles['Normal']))
            story.append(Paragraph(f"  Objetivo: {actividad['objetivo_general']}", styles['Normal']))
            story.append(Paragraph(f"  Responsables: {', '.join(actividad['responsables'])}", styles['Normal']))
            story.append(Spacer(1, 6))
    
    # Fecha de generación
    story.append(Spacer(1, 20))
    story.append(Paragraph(f"Fecha de generación: {datetime.now().strftime('%Y-%m-%d %H:%M')}", styles['Normal']))
    
    doc.build(story)
    buffer.seek(0)
    return buffer

def mostrar_evaluacion():
    st.markdown("""
    <div class="section-header">
        <h2>📊 Evaluación del Proceso</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ### 🎓 Evaluación del Diagnóstico Comunitario
    
    Esta sección te permite evaluar el proceso completo de diagnóstico comunitario 
    y exportar los resultados para tu portafolio académico.
    
    **💡 Tip:** También puedes usar la "Evaluación MAIS Oficial" para aplicar 
    las métricas estándar del Modelo de Atención Integral en Salud.
    """)
    
    # Verificar completitud del proceso
    st.markdown("### ✅ Verificación de Completitud")
    
    pasos_completados = []
    pasos_pendientes = []
    
    # Verificar cada paso
    if st.session_state.sectores:
        pasos_completados.append("🗺️ Sectorización del territorio")
    else:
        pasos_pendientes.append("🗺️ Sectorización del territorio")
    
    if st.session_state.equipos:
        pasos_completados.append("👥 Formación de equipos de cabecera")
    else:
        pasos_pendientes.append("👥 Formación de equipos de cabecera")
    
    if st.session_state.familias:
        pasos_completados.append("👨‍👩‍👧‍👦 Registro de familias")
    else:
        pasos_pendientes.append("👨‍👩‍👧‍👦 Registro de familias")
    
    if hasattr(st.session_state, 'diagnostico') and st.session_state.diagnostico:
        pasos_completados.append("🔍 Diagnóstico comunitario")
    else:
        pasos_pendientes.append("🔍 Diagnóstico comunitario")
    
    if st.session_state.instituciones:
        pasos_completados.append("🌐 Trabajo en red intersectorial")
    else:
        pasos_pendientes.append("🌐 Trabajo en red intersectorial")
    
    if st.session_state.plan_intervencion:
        pasos_completados.append("📋 Plan de intervención")
    else:
        pasos_pendientes.append("📋 Plan de intervención")
    
    # Mostrar progreso
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Pasos Completados:**")
        for paso in pasos_completados:
            st.success(f"✅ {paso}")
    
    with col2:
        st.markdown("**Pasos Pendientes:**")
        for paso in pasos_pendientes:
            st.error(f"❌ {paso}")
    
    # Calcular porcentaje de completitud
    total_pasos = 6
    porcentaje_completitud = (len(pasos_completados) / total_pasos) * 100
    
    st.markdown(f"### 📈 Progreso General: {porcentaje_completitud:.1f}%")
    st.progress(porcentaje_completitud / 100)
    
    if porcentaje_completitud == 100:
        st.success("🎉 ¡Felicitaciones! Has completado todo el proceso de diagnóstico comunitario.")
    elif porcentaje_completitud >= 80:
        st.warning("⚠️ Casi completo. Revisa los pasos pendientes para finalizar el proceso.")
    else:
        st.error("❌ Proceso incompleto. Completa los pasos pendientes para continuar.")
    
    # Resumen ejecutivo
    if st.session_state.sectores or st.session_state.familias:
        st.markdown("### 📊 Resumen Ejecutivo")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            if st.session_state.sectores:
                total_sectores = len(st.session_state.sectores)
                st.metric("Sectores", total_sectores)
            else:
                st.metric("Sectores", 0)
        
        with col2:
            if st.session_state.familias:
                total_familias = len(st.session_state.familias)
                st.metric("Familias", total_familias)
            else:
                st.metric("Familias", 0)
        
        with col3:
            if st.session_state.familias:
                familias_alto_riesgo = sum(1 for f in st.session_state.familias 
                                         if f["riesgos"]["social"]["nivel"] == "Alto" or 
                                         f["riesgos"]["sanitario"]["nivel"] == "Alto")
                st.metric("Alto Riesgo", familias_alto_riesgo)
            else:
                st.metric("Alto Riesgo", 0)
        
        with col4:
            if st.session_state.plan_intervencion:
                total_actividades = len(st.session_state.plan_intervencion)
                st.metric("Actividades", total_actividades)
            else:
                st.metric("Actividades", 0)
    
    # Análisis de calidad
    st.markdown("### 🔍 Análisis de Calidad del Diagnóstico")
    
    calidad_puntos = 0
    max_puntos = 0
    
    # Evaluar sectorización (Métricas MAIS - Comunidad)
    if st.session_state.sectores:
        max_puntos += 20
        if len(st.session_state.sectores) >= 2:
            calidad_puntos += 10  # Participación comunitaria
        if any(s["vulnerabilidad"] in ["Alta", "Crítica"] for s in st.session_state.sectores):
            calidad_puntos += 10  # Coordinación intersectorial
    
    # Evaluar registro de familias
    if st.session_state.familias:
        max_puntos += 30
        if len(st.session_state.familias) >= 5:
            calidad_puntos += 15
        if any(f["riesgos"]["social"]["nivel"] == "Alto" or f["riesgos"]["sanitario"]["nivel"] == "Alto" 
               for f in st.session_state.familias):
            calidad_puntos += 15
    
    # Evaluar diagnóstico
    if hasattr(st.session_state, 'diagnostico') and st.session_state.diagnostico:
        max_puntos += 25
        diagnostico = st.session_state.diagnostico
        if diagnostico["problema_principal"]:
            calidad_puntos += 10
        if diagnostico["estrategias_propuestas"]:
            calidad_puntos += 10
        if diagnostico["indicadores_evaluacion"]:
            calidad_puntos += 5
    
    # Evaluar plan de intervención
    if st.session_state.plan_intervencion:
        max_puntos += 25
        if len(st.session_state.plan_intervencion) >= 2:
            calidad_puntos += 10
        if any("TENS" in a["responsables"] for a in st.session_state.plan_intervencion):
            calidad_puntos += 10
        if any(a["presupuesto_estimado"] > 0 for a in st.session_state.plan_intervencion):
            calidad_puntos += 5
    
    # Calcular puntaje final
    if max_puntos > 0:
        puntaje_final = (calidad_puntos / max_puntos) * 100
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"**Puntaje de Calidad: {puntaje_final:.1f}/100**")
            st.progress(puntaje_final / 100)
        
        with col2:
            if puntaje_final >= 90:
                st.success("🏆 **Excelente** - Diagnóstico de alta calidad")
            elif puntaje_final >= 75:
                st.success("👍 **Muy Bueno** - Diagnóstico de buena calidad")
            elif puntaje_final >= 60:
                st.warning("⚠️ **Bueno** - Diagnóstico aceptable")
            else:
                st.error("❌ **Necesita Mejora** - Revisa y completa el diagnóstico")
    
    # Autoevaluación
    st.markdown("### 🤔 Autoevaluación del Proceso")
    
    with st.expander("📝 Formulario de Autoevaluación", expanded=True):
        st.markdown("**Evalúa tu desempeño en cada aspecto del proceso:**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            comprension_conceptos = st.slider(
                "Comprensión de conceptos MAIS",
                min_value=1, max_value=5, value=3,
                help="1=Muy baja, 5=Excelente"
            )
            
            aplicacion_metodologia = st.slider(
                "Aplicación de metodología",
                min_value=1, max_value=5, value=3,
                help="1=Muy baja, 5=Excelente"
            )
            
            analisis_datos = st.slider(
                "Análisis de datos",
                min_value=1, max_value=5, value=3,
                help="1=Muy baja, 5=Excelente"
            )
        
        with col2:
            formulacion_diagnostico = st.slider(
                "Formulación del diagnóstico",
                min_value=1, max_value=5, value=3,
                help="1=Muy baja, 5=Excelente"
            )
            
            planificacion_intervencion = st.slider(
                "Planificación de intervención",
                min_value=1, max_value=5, value=3,
                help="1=Muy baja, 5=Excelente"
            )
            
            trabajo_equipo = st.slider(
                "Trabajo en equipo",
                min_value=1, max_value=5, value=3,
                help="1=Muy baja, 5=Excelente"
            )
        
        # Reflexión personal
        reflexion_personal = st.text_area(
            "Reflexión personal sobre el proceso de aprendizaje",
            placeholder="¿Qué aprendiste? ¿Qué fue lo más desafiante? ¿Cómo aplicarías esto en la práctica?"
        )
        
        # Fortalezas y áreas de mejora
        col1, col2 = st.columns(2)
        
        with col1:
            fortalezas = st.text_area(
                "Mis fortalezas en este proceso",
                placeholder="Identifica tus fortalezas..."
            )
        
        with col2:
            areas_mejora = st.text_area(
                "Áreas de mejora",
                placeholder="Identifica áreas donde puedes mejorar..."
            )
        
        # Guardar autoevaluación
        if st.button("💾 Guardar Autoevaluación", type="primary"):
            autoevaluacion = {
                "comprension_conceptos": comprension_conceptos,
                "aplicacion_metodologia": aplicacion_metodologia,
                "analisis_datos": analisis_datos,
                "formulacion_diagnostico": formulacion_diagnostico,
                "planificacion_intervencion": planificacion_intervencion,
                "trabajo_equipo": trabajo_equipo,
                "reflexion_personal": reflexion_personal,
                "fortalezas": fortalezas,
                "areas_mejora": areas_mejora,
                "fecha_evaluacion": datetime.now().strftime("%Y-%m-%d %H:%M")
            }
            
            st.session_state.autoevaluacion = autoevaluacion
            st.success("✅ Autoevaluación guardada exitosamente!")
    
    # Mostrar autoevaluación guardada
    if hasattr(st.session_state, 'autoevaluacion') and st.session_state.autoevaluacion:
        st.markdown("### 📋 Autoevaluación Guardada")
        
        autoevaluacion = st.session_state.autoevaluacion
        
        # Gráfico de radar
        categorias = ["Comprensión", "Metodología", "Análisis", "Diagnóstico", "Planificación", "Equipo"]
        valores = [
            autoevaluacion["comprension_conceptos"],
            autoevaluacion["aplicacion_metodologia"],
            autoevaluacion["analisis_datos"],
            autoevaluacion["formulacion_diagnostico"],
            autoevaluacion["planificacion_intervencion"],
            autoevaluacion["trabajo_equipo"]
        ]
        
        fig_radar = go.Figure()
        fig_radar.add_trace(go.Scatterpolar(
            r=valores,
            theta=categorias,
            fill='toself',
            name='Autoevaluación'
        ))
        
        fig_radar.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 5]
                )),
            showlegend=False,
            title="Perfil de Competencias"
        )
        
        st.plotly_chart(fig_radar, use_container_width=True)
        
        # Mostrar reflexión
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Reflexión Personal:**")
            st.info(autoevaluacion["reflexion_personal"])
        
        with col2:
            st.markdown("**Fortalezas:**")
            st.success(autoevaluacion["fortalezas"])
        
        st.markdown("**Áreas de Mejora:**")
        st.warning(autoevaluacion["areas_mejora"])
    
    # Exportación de datos
    st.markdown("### 📤 Exportación de Datos")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Exportar a Excel
        if st.session_state.sectores or st.session_state.familias:
            # Crear Excel con múltiples hojas
            output = io.BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                # Hoja de sectores
                if st.session_state.sectores:
                    df_sectores = pd.DataFrame(st.session_state.sectores)
                    df_sectores.to_excel(writer, sheet_name='Sectores', index=False)
                
                # Hoja de familias
                if st.session_state.familias:
                    familias_data = []
                    for familia in st.session_state.familias:
                        familias_data.append({
                            "Sector": familia["sector"],
                            "Apellido": familia["apellido"],
                            "Integrantes": familia["num_integrantes"],
                            "Riesgo Social": familia["riesgos"]["social"]["nivel"],
                            "Riesgo Sanitario": familia["riesgos"]["sanitario"]["nivel"],
                            "Hacinamiento": familia["vivienda"]["hacinamiento"],
                            "Violencia Intrafamiliar": familia["salud"]["violencia_intrafamiliar"],
                            "Consumo Drogas": familia["salud"]["consumo_drogas"]
                        })
                    df_familias = pd.DataFrame(familias_data)
                    df_familias.to_excel(writer, sheet_name='Familias', index=False)
                
                # Hoja de plan de intervención
                if st.session_state.plan_intervencion:
                    plan_data = []
                    for actividad in st.session_state.plan_intervencion:
                        plan_data.append({
                            "Actividad": actividad["nombre"],
                            "Tipo": actividad["tipo"],
                            "Objetivo": actividad["objetivo_general"],
                            "Responsables": ", ".join(actividad["responsables"]),
                            "Presupuesto": actividad["presupuesto_estimado"],
                            "Fecha Inicio": actividad["cronograma"]["fecha_inicio"],
                            "Fecha Fin": actividad["cronograma"]["fecha_fin"]
                        })
                    df_plan = pd.DataFrame(plan_data)
                    df_plan.to_excel(writer, sheet_name='Plan_Intervencion', index=False)
            
            output.seek(0)
            st.download_button(
                label="📊 Descargar Excel",
                data=output.getvalue(),
                file_name=f"diagnostico_comunitario_{datetime.now().strftime('%Y%m%d')}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
    
    with col2:
        # Exportar a PDF
        if st.session_state.sectores or st.session_state.familias:
            pdf_buffer = generar_pdf()
            st.download_button(
                label="📄 Descargar PDF",
                data=pdf_buffer.getvalue(),
                file_name=f"diagnostico_comunitario_{datetime.now().strftime('%Y%m%d')}.pdf",
                mime="application/pdf"
            )
    
    # Exportar datos JSON
    if st.session_state.sectores or st.session_state.familias:
        datos_completos = {
            "sectores": st.session_state.sectores,
            "equipos": st.session_state.equipos,
            "familias": st.session_state.familias,
            "instituciones": st.session_state.instituciones,
            "plan_intervencion": st.session_state.plan_intervencion,
            "diagnostico": st.session_state.diagnostico if hasattr(st.session_state, 'diagnostico') else None,
            "autoevaluacion": st.session_state.autoevaluacion if hasattr(st.session_state, 'autoevaluacion') else None,
            "fecha_exportacion": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        
        json_data = json.dumps(datos_completos, indent=2, ensure_ascii=False)
        st.download_button(
            label="💾 Descargar JSON",
            data=json_data,
            file_name=f"datos_completos_{datetime.now().strftime('%Y%m%d')}.json",
            mime="application/json"
        )
    
    # Recomendaciones finales
    st.markdown("### 🎯 Recomendaciones Finales")
    
    if porcentaje_completitud < 100:
        st.warning("**Para completar el proceso:**")
        for paso in pasos_pendientes:
            st.write(f"• {paso}")
    
    if st.session_state.familias:
        familias_alto_riesgo = sum(1 for f in st.session_state.familias 
                                 if f["riesgos"]["social"]["nivel"] == "Alto" or 
                                 f["riesgos"]["sanitario"]["nivel"] == "Alto")
        
        if familias_alto_riesgo > 0:
            st.info(f"• Priorizar la atención de {familias_alto_riesgo} familias en alto riesgo")
        
        if sum(1 for f in st.session_state.familias if f["salud"]["violencia_intrafamiliar"]) > 0:
            st.error("• Implementar protocolos de detección y derivación de violencia intrafamiliar")
    
    if st.session_state.plan_intervencion:
        if len(st.session_state.plan_intervencion) < 3:
            st.warning("• Considerar agregar más actividades al plan de intervención")
        
        if not any("TENS" in a["responsables"] for a in st.session_state.plan_intervencion):
            st.info("• Incluir TENS como responsables en las actividades")
    
    st.success("🎓 **¡Has completado exitosamente el simulador de diagnóstico comunitario!**")
    st.info("Este proceso te ha preparado para realizar diagnósticos comunitarios reales en el contexto de APS.") 
    
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