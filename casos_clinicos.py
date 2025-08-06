import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

def mostrar_casos_clinicos():
    st.markdown("""
    <div class="section-header">
        <h2>🏥 Casos Clínicos Comunitarios</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ### 📋 ¿Qué son los Casos Clínicos Comunitarios?
    
    Los casos clínicos comunitarios te permiten analizar situaciones reales que enfrentan los TENS 
    en el trabajo de salud familiar. Cada caso incluye contexto comunitario, factores de riesgo 
    y oportunidades de intervención.
    """)
    
    # Selección de caso
    caso_seleccionado = st.selectbox(
        "Selecciona un caso clínico:",
        ["Caso 1: Don Luis - Diabetes en Comunidad Rural", 
         "Caso 2: Sra. Isabel - Teletriage en Comunidad Rural",
         "Caso 3: Familia Mendoza - Violencia Intrafamiliar",
         "Caso 4: Sra. Rosa - Adulto Mayor Aislado",
         "Caso 5: Adolescente María - Embarazo Precoz",
         "Caso 6: Don Carlos - Monitoreo Remoto de Hipertensión",
         "Caso 7: Sra. Ana - Telemedicina para Control Prenatal"],
        key="caso_clinico"
    )
    
    if caso_seleccionado == "Caso 1: Don Luis - Diabetes en Comunidad Rural":
        mostrar_caso_don_luis()
    elif caso_seleccionado == "Caso 2: Sra. Isabel - Teletriage en Comunidad Rural":
        mostrar_caso_sra_isabel()
    elif caso_seleccionado == "Caso 3: Familia Mendoza - Violencia Intrafamiliar":
        mostrar_caso_familia_mendoza()
    elif caso_seleccionado == "Caso 4: Sra. Rosa - Adulto Mayor Aislado":
        mostrar_caso_sra_rosa()
    elif caso_seleccionado == "Caso 5: Adolescente María - Embarazo Precoz":
        mostrar_caso_adolescente_maria()
    elif caso_seleccionado == "Caso 6: Don Carlos - Monitoreo Remoto de Hipertensión":
        mostrar_caso_don_carlos()
    elif caso_seleccionado == "Caso 7: Sra. Ana - Telemedicina para Control Prenatal":
        mostrar_caso_sra_ana()

def mostrar_caso_don_luis():
    st.header("🏥 Caso Clínico: Don Luis - Diabetes en Comunidad Rural")
    
    # Contexto del caso
    st.subheader("📋 Contexto")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Datos del Paciente:**
        - **Nombre:** Don Luis
        - **Edad:** 65 años
        - **Ocupación:** Agricultor
        - **Lugar de residencia:** Comunidad agrícola remota
        """)
        
        st.markdown("""
        **Contexto Comunitario:**
        - **CESFAM:** A 1 hora de distancia por carretera
        - **PSR (Posta Rural):** En la comunidad
        - **Personal disponible:** TENS diario, médico 1 vez al mes
        - **Acceso a servicios:** Limitado por distancia y transporte
        """)
    
    with col2:
        st.markdown("""
        **Diagnósticos:**
        - Diabetes Mellitus Tipo 2
        - Hipertensión Arterial
        
        **Medicamentos:**
        - Metformina 500mg 2x día
        - Enalapril 10mg 1x día
        """)
        
        st.markdown("""
        **Última evaluación:**
        - **Fecha:** Hace 2 meses
        - **Glicemia:** 180 mg/dL
        - **Presión arterial:** 150/95 mmHg
        - **Peso:** 78 kg
        """)
    
    # Situación clínica actual
    st.subheader("🚨 Situación Clínica Actual")
    
    st.warning("""
    **Síntomas recientes (últimas semanas):**
    - Polidipsia (sed excesiva)
    - Poliuria (orinar frecuentemente)
    - Fatiga
    - Visión borrosa progresiva
    - Parestesias en pies (hormigueo constante)
    """)
    
    st.info("""
    **Evaluación del TENS:**
    Don Luis acude al PSR preocupado por sus síntomas. 
    El TENS sospecha diabetes descontrolada y posible inicio de 
    complicaciones microvasculares y neuropatía diabética.
    """)
    
    # Análisis del caso
    st.subheader("🔍 Análisis del Caso")
    
    # Factores de riesgo identificados
    st.markdown("### ⚠️ Factores de Riesgo Identificados")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Factores de Riesgo Sanitarios:**")
        st.write("• Diabetes mal controlada")
        st.write("• Hipertensión arterial")
        st.write("• Posibles complicaciones microvasculares")
        st.write("• Neuropatía diabética")
        st.write("• Retinopatía diabética")
    
    with col2:
        st.markdown("**Factores de Riesgo Sociales:**")
        st.write("• Acceso limitado a servicios de salud")
        st.write("• Distancia al CESFAM")
        st.write("• Dependencia de transporte")
        st.write("• Posible aislamiento social")
        st.write("• Factores económicos")
    
    # Intervenciones propuestas
    st.subheader("💡 Intervenciones Propuestas")
    
    # Intervenciones inmediatas
    st.markdown("### 🚨 Intervenciones Inmediatas")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Acciones del TENS:**")
        st.write("1. **Evaluación inicial:** Medir glicemia capilar")
        st.write("2. **Control de signos vitales:** PA, frecuencia cardíaca")
        st.write("3. **Evaluación de complicaciones:** Examen de pies")
        st.write("4. **Educación inmediata:** Sobre síntomas de alarma")
        st.write("5. **Coordinación:** Contactar médico del CESFAM")
    
    with col2:
        st.markdown("**Derivación:**")
        st.write("• **Urgente:** Si glicemia > 300 mg/dL")
        st.write("• **Prioritaria:** Si síntomas de descompensación")
        st.write("• **Programada:** Para evaluación oftalmológica")
        st.write("• **Educativa:** Programa de diabetes")
    
    # Intervenciones comunitarias
    st.markdown("### 🏘️ Intervenciones Comunitarias")
    
    intervenciones_comunitarias = [
        "**Programa de educación diabetológica** en la comunidad rural",
        "**Grupo de apoyo** para personas con diabetes",
        "**Control domiciliario** de glicemia y presión arterial",
        "**Coordinación con transporte** para traslados al CESFAM",
        "**Red de apoyo** con familiares y vecinos",
        "**Talleres de cocina saludable** adaptados al contexto rural",
        "**Actividades físicas** apropiadas para adultos mayores",
        "**Seguimiento telefónico** regular por el TENS"
    ]
    
    for intervencion in intervenciones_comunitarias:
        st.write(f"• {intervencion}")
    
    # Análisis FODA del caso
    st.subheader("📊 Análisis FODA del Caso")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Fortalezas:**")
        st.write("✅ Don Luis busca ayuda activamente")
        st.write("✅ TENS disponible en la comunidad")
        st.write("✅ Diagnóstico previo establecido")
        st.write("✅ Medicamentos disponibles")
        
        st.markdown("**Oportunidades:**")
        st.write("🎯 Programa de diabetes en CESFAM")
        st.write("🎯 Posibilidad de educación grupal")
        st.write("🎯 Red de apoyo familiar")
        st.write("🎯 Recursos comunitarios")
    
    with col2:
        st.markdown("**Debilidades:**")
        st.write("❌ Acceso limitado a especialistas")
        st.write("❌ Falta de control regular")
        st.write("❌ Posibles complicaciones")
        st.write("❌ Barreras de transporte")
        
        st.markdown("**Amenazas:**")
        st.write("⚠️ Progresión de complicaciones")
        st.write("⚠️ Descompensación aguda")
        st.write("⚠️ Pérdida de visión")
        st.write("⚠️ Amputación de extremidades")
    
    # Ejercicio de reflexión
    st.subheader("🤔 Ejercicio de Reflexión")
    
    st.markdown("""
    **Preguntas para análisis:**
    
    1. **¿Qué factores comunitarios influyen en el control de la diabetes de Don Luis?**
    2. **¿Cómo podrías mejorar el acceso a servicios de salud en esta comunidad rural?**
    3. **¿Qué intervenciones preventivas implementarías para evitar casos similares?**
    4. **¿Cómo coordinarías el trabajo entre el PSR y el CESFAM?**
    5. **¿Qué indicadores usarías para evaluar el impacto de las intervenciones?**
    """)
    
    # Botón para generar recomendaciones inteligentes
    if st.button("🤖 Generar Recomendaciones Inteligentes", key="recomendaciones_don_luis"):
        st.success("✅ Recomendaciones generadas basadas en el análisis del caso:")
        
        st.markdown("""
        **🎯 Intervenciones Prioritarias:**
        
        1. **Control inmediato:** Medición de glicemia y derivación si es necesario
        2. **Educación individual:** Sobre síntomas de alarma y autocuidado
        3. **Coordinación intersectorial:** Con transporte y CESFAM
        4. **Seguimiento estructurado:** Visitas domiciliarias regulares
        5. **Prevención secundaria:** Evaluación de complicaciones
        
        **📈 Indicadores de Seguimiento:**
        - Control glicémico (HbA1c < 7%)
        - Control de presión arterial (< 140/90)
        - Adherencia al tratamiento
        - Frecuencia de complicaciones
        - Satisfacción del usuario
        """)
    
    # Footer
    st.markdown("---")
    st.markdown("*Caso clínico desarrollado para formación en diagnóstico comunitario en salud familiar. © 2025. Todos los derechos reservados.*")

def mostrar_caso_sra_isabel():
    st.header("🏥 Caso Clínico: Sra. Isabel - Teletriage en Comunidad Rural")
    
    # Contexto del caso
    st.subheader("📋 Antecedentes")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Datos del Paciente:**
        - **Nombre:** Sra. Isabel
        - **Edad:** 78 años
        - **Lugar de residencia:** Comunidad rural
        - **Movilidad:** Dificultad para movilizarse independientemente
        - **Condición:** Artrosis de rodilla
        """)
        
        st.markdown("""
        **Diagnósticos:**
        - Diabetes Mellitus Tipo 2 (controlada)
        - Hipertensión Arterial (controlada)
        - Artrosis de rodilla
        
        **Medicamentos:**
        - Metformina 500mg 2x día
        - Enalapril 10mg 1x día
        - Paracetamol según necesidad
        """)
    
    with col2:
        st.markdown("""
        **Contexto Comunitario:**
        - **CESFAM:** Con sistema de teletriage recientemente implementado
        - **Acceso:** Dificultad para traslados presenciales
        - **Apoyo familiar:** Nieta disponible para apoyo tecnológico
        - **Monitoreo:** Control de glicemia capilar en casa
        """)
        
        st.markdown("""
        **Última evaluación:**
        - **Fecha:** Hace 2 semanas
        - **Glicemia:** 140 mg/dL (controlada)
        - **Presión arterial:** 135/85 mmHg
        - **Estado general:** Estable
        """)
    
    # Situación clínica actual
    st.subheader("🚨 Situación Clínica Actual")
    
    st.warning("""
    **Síntomas presentados (una mañana):**
    - Fatiga inusual
    - Dolor de cabeza leve
    - Náuseas leves
    - Glicemia capilar: 180 mg/dL (elevada, pero no crítica)
    """)
    
    st.info("""
    **Preocupación de la paciente:**
    La Sra. Isabel está preocupada por estos síntomas inespecíficos, 
    pero sabe lo difícil que sería trasladarse al CESFAM sin necesidad urgente. 
    Su nieta le sugiere utilizar la nueva plataforma de teletriage.
    """)
    
    # Aplicación del Teletriage
    st.subheader("💻 Aplicación del Teletriage")
    
    # Paso 1: Solicitud Online
    st.markdown("### 1️⃣ Solicitud Online")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Proceso:**")
        st.write("• Nieta accede a plataforma online del CESFAM")
        st.write("• Completa formulario digital detallado")
        st.write("• Describe síntomas y valores de glicemia")
        st.write("• Incluye historial médico relevante")
        st.write("• Envía solicitud durante la mañana")
    
    with col2:
        st.markdown("**Información enviada:**")
        st.write("• Síntomas: fatiga, dolor de cabeza, náuseas")
        st.write("• Glicemia: 180 mg/dL")
        st.write("• Presión arterial reciente")
        st.write("• Adherencia a medicación")
        st.write("• Hábitos alimenticios")
    
    # Paso 2: Proceso de Triage Remoto
    st.markdown("### 2️⃣ Proceso de Triage Remoto")
    
    st.success("""
    **Evaluación del Triagista (Enfermera capacitada):**
    
    **Análisis realizado:**
    - Revisa solicitud completa de Sra. Isabel
    - Evalúa gravedad de síntomas (leves, no críticos)
    - Analiza valores de glicemia (elevados, pero no de urgencia)
    - Considera dificultades de movilidad
    
    **Decisión tomada:**
    - **NO es emergencia** que requiera asistencia presencial inmediata
    - **SÍ necesita evaluación oportuna** por riesgo
    - **Priorización:** Atención telefónica en menos de 24 horas
    """)
    
    # Paso 3: Resolución de la Atención
    st.markdown("### 3️⃣ Resolución de la Atención")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Decisión del Triagista:**")
        st.write("✅ Situación resoluble mediante teleconsulta telefónica")
        st.write("✅ Respuesta en menos de 24 horas")
        st.write("✅ Enfermera del equipo de cabecera la contacta")
        st.write("✅ Evita traslado innecesario al CESFAM")
    
    with col2:
        st.markdown("**Beneficios inmediatos:**")
        st.write("• Atención oportuna sin movilización")
        st.write("• Evaluación profesional desde casa")
        st.write("• Continuidad del cuidado")
        st.write("• Optimización de recursos del CESFAM")
    
    # Paso 4: Teleconsulta y Planificación
    st.markdown("### 4️⃣ Teleconsulta y Planificación")
    
    st.markdown("**Evaluación durante la teleconsulta:**")
    
    evaluacion_items = [
        "Evaluación detallada de síntomas",
        "Verificación de adherencia a medicación",
        "Revisión de hábitos alimenticios recientes",
        "Instrucciones sobre ajustes dietéticos",
        "Recomendaciones de hidratación",
        "Coordinación de entrega de insumos",
        "Agenda de control presencial posterior"
    ]
    
    for item in evaluacion_items:
        st.write(f"• {item}")
    
    st.markdown("**Plan de seguimiento:**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Inmediato:**")
        st.write("• Ajustes dietéticos")
        st.write("• Hidratación adecuada")
        st.write("• Monitoreo de glicemia")
        st.write("• Entrega de insumos a domicilio")
    
    with col2:
        st.markdown("**A corto plazo:**")
        st.write("• Control presencial con médico")
        st.write("• Evaluación física completa")
        st.write("• Exámenes de laboratorio")
        st.write("• Ajuste de medicación si es necesario")
    
    # Beneficios demostrados
    st.subheader("✅ Beneficios Demostrados")
    
    beneficios = [
        "**Atención oportuna y segura** sin traslado físico inmediato",
        "**Priorización inteligente** de necesidades de salud",
        "**Optimización de recursos** del centro de salud",
        "**Mejora de accesibilidad** para adultos mayores",
        "**Continuidad del cuidado** con seguimiento estructurado",
        "**Reducción de barreras** geográficas y de movilidad",
        "**Empoderamiento familiar** en el cuidado de la salud",
        "**Prevención de complicaciones** mediante atención temprana"
    ]
    
    for beneficio in beneficios:
        st.write(f"• {beneficio}")
    
    # Análisis del caso
    st.subheader("🔍 Análisis del Caso")
    
    # Factores de éxito
    st.markdown("### 🎯 Factores de Éxito")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Tecnológicos:**")
        st.write("• Plataforma de teletriage disponible")
        st.write("• Formulario digital completo")
        st.write("• Comunicación telefónica efectiva")
        st.write("• Sistema de seguimiento integrado")
    
    with col2:
        st.markdown("**Organizacionales:**")
        st.write("• Triagista capacitado")
        st.write("• Respuesta en menos de 24 horas")
        st.write("• Coordinación entre equipos")
        st.write("• Continuidad de la atención")
    
    # Lecciones aprendidas
    st.markdown("### 📚 Lecciones Aprendidas")
    
    lecciones = [
        "**La tecnología puede democratizar el acceso a la salud** en comunidades rurales",
        "**El teletriage optimiza recursos** evitando consultas presenciales innecesarias",
        "**La capacitación del personal** es clave para el éxito del sistema",
        "**La participación familiar** facilita la implementación de tecnologías",
        "**La continuidad del cuidado** se mantiene con seguimiento estructurado",
        "**Los adultos mayores pueden beneficiarse** significativamente de estas innovaciones"
    ]
    
    for leccion in lecciones:
        st.write(f"• {leccion}")
    
    # Intervenciones propuestas
    st.subheader("💡 Intervenciones Propuestas")
    
    st.markdown("### 🚀 Intervenciones Inmediatas")
    
    intervenciones_inmediatas = [
        "**Capacitación del equipo:** En uso de plataforma de teletriage",
        "**Educación comunitaria:** Sobre disponibilidad del servicio",
        "**Apoyo tecnológico:** Para familias con dificultades de acceso",
        "**Protocolos claros:** Para diferentes tipos de consultas",
        "**Seguimiento estructurado:** De casos atendidos por teletriage"
    ]
    
    for intervencion in intervenciones_inmediatas:
        st.write(f"• {intervencion}")
    
    st.markdown("### 🏘️ Intervenciones Comunitarias")
    
    intervenciones_comunitarias = [
        "**Campaña de difusión** sobre servicios de teletriage",
        "**Talleres de alfabetización digital** para adultos mayores",
        "**Red de apoyo tecnológico** con jóvenes de la comunidad",
        "**Evaluación de satisfacción** de usuarios del teletriage",
        "**Mejora continua** basada en feedback de la comunidad"
    ]
    
    for intervencion in intervenciones_comunitarias:
        st.write(f"• {intervencion}")
    
    # Ejercicio de reflexión
    st.subheader("🤔 Ejercicio de Reflexión")
    
    st.markdown("""
    **Preguntas para análisis:**
    
    1. **¿Qué ventajas tiene el teletriage para comunidades rurales como la de la Sra. Isabel?**
    2. **¿Cómo podrías implementar un sistema similar en tu comunidad?**
    3. **¿Qué barreras tecnológicas podrían existir y cómo las superarías?**
    4. **¿Cómo evaluarías la efectividad del teletriage en tu contexto?**
    5. **¿Qué otros grupos poblacionales podrían beneficiarse de esta tecnología?**
    6. **¿Cómo integrarías el teletriage con el modelo MAIS?**
    """)
    
    # Botón para generar recomendaciones inteligentes
    if st.button("🤖 Generar Recomendaciones Inteligentes", key="recomendaciones_sra_isabel"):
        st.success("✅ Recomendaciones generadas basadas en el análisis del caso:")
        
        st.markdown("""
        **🎯 Intervenciones Prioritarias:**
        
        1. **Implementación de teletriage:** Capacitación del equipo y difusión comunitaria
        2. **Alfabetización digital:** Talleres para adultos mayores y familias
        3. **Red de apoyo tecnológico:** Involucrar jóvenes de la comunidad
        4. **Protocolos de atención:** Establecer guías claras para diferentes situaciones
        5. **Evaluación continua:** Medir satisfacción y efectividad del servicio
        
        **📈 Indicadores de Seguimiento:**
        - Tiempo de respuesta del teletriage
        - Satisfacción del usuario
        - Reducción de consultas presenciales innecesarias
        - Mejora en accesibilidad a servicios de salud
        - Adherencia al tratamiento post-teletriage
        """)
    
    # Footer
    st.markdown("---")
    st.markdown("*Caso clínico desarrollado para formación en diagnóstico comunitario en salud familiar. © 2025. Todos los derechos reservados.*")

def mostrar_caso_familia_mendoza():
    st.header("🏥 Caso Clínico: Familia Mendoza - Violencia Intrafamiliar")
    
    st.subheader("📋 Contexto")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Datos de la Familia:**
        - **Jefa de hogar:** Patricia Mendoza (35 años)
        - **Integrantes:** 6 personas
        - **Vivienda:** Mediagua en Sector Sur
        - **Situación:** Hacinamiento alto
        """)
        
        st.markdown("""
        **Factores de Riesgo:**
        - Violencia intrafamiliar
        - Consumo de drogas
        - Desempleo
        - Embarazo adolescente
        - Red de apoyo débil
        """)
    
    with col2:
        st.markdown("""
        **Contexto Comunitario:**
        - Sector de alta vulnerabilidad
        - Servicios básicos limitados
        - Alta prevalencia de violencia
        - Recursos comunitarios escasos
        """)
    
    st.subheader("🚨 Situación Actual")
    
    st.error("""
    **Problemas identificados:**
    - Violencia física y psicológica hacia Patricia
    - Consumo de drogas por parte del padre
    - Embarazo de hija adolescente (15 años)
    - Desempleo crónico
    - Hacinamiento crítico
    """)
    
    st.subheader("💡 Intervenciones Propuestas")
    
    st.markdown("**Intervenciones Inmediatas:**")
    st.write("1. **Protección:** Protocolo de derivación a Centro de la Mujer")
    st.write("2. **Apoyo psicosocial:** Atención psicológica urgente")
    st.write("3. **Vivienda:** Gestión de subsidio habitacional")
    st.write("4. **Empleo:** Programa de inserción laboral")
    st.write("5. **Salud:** Control prenatal para adolescente")
    
    st.markdown("**Intervenciones Comunitarias:**")
    st.write("• Talleres de prevención de violencia")
    st.write("• Grupos de apoyo para mujeres")
    st.write("• Programa de rehabilitación de drogas")
    st.write("• Educación sexual para adolescentes")
    st.write("• Fortalecimiento de redes sociales")

def mostrar_caso_sra_rosa():
    st.header("🏥 Caso Clínico: Sra. Rosa - Adulto Mayor Aislado")
    
    st.subheader("📋 Contexto")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Datos del Paciente:**
        - **Nombre:** Rosa Díaz (67 años)
        - **Vivienda:** Casa propia en Sector Norte
        - **Estado civil:** Viuda
        - **Hijos:** 2 (viven en otra ciudad)
        """)
        
        st.markdown("""
        **Diagnósticos:**
        - Artritis
        - Hipertensión arterial
        - Depresión leve
        """)
    
    with col2:
        st.markdown("""
        **Situación Social:**
        - Vive sola
        - Movilidad reducida
        - Red de apoyo limitada
        - Participación social baja
        """)
    
    st.subheader("🚨 Problemas Identificados")
    
    st.warning("""
    **Riesgos identificados:**
    - Aislamiento social
    - Dependencia funcional
    - Depresión
    - Caídas
    - Mala adherencia al tratamiento
    """)
    
    st.subheader("💡 Intervenciones Propuestas")
    
    st.markdown("**Intervenciones Individuales:**")
    st.write("1. **Evaluación funcional:** Capacidad de autocuidado")
    st.write("2. **Control médico:** Artritis e hipertensión")
    st.write("3. **Apoyo psicológico:** Manejo de la depresión")
    st.write("4. **Adaptación del hogar:** Prevención de caídas")
    
    st.markdown("**Intervenciones Comunitarias:**")
    st.write("• Programa de adultos mayores")
    st.write("• Actividades de socialización")
    st.write("• Visitas domiciliarias regulares")
    st.write("• Red de apoyo vecinal")
    st.write("• Transporte comunitario")

def mostrar_caso_adolescente_maria():
    st.header("🏥 Caso Clínico: Adolescente María - Embarazo Precoz")
    
    st.subheader("📋 Contexto")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Datos de la Paciente:**
        - **Nombre:** María (15 años)
        - **Escolaridad:** 2° medio
        - **Estado civil:** Soltera
        - **Familia:** Monoparental
        """)
        
        st.markdown("""
        **Situación:**
        - Embarazo de 12 semanas
        - Sin control prenatal
        - Baja escolaridad
        - Familia en situación vulnerable
        """)
    
    with col2:
        st.markdown("""
        **Contexto:**
        - Sector de alta vulnerabilidad
        - Alta prevalencia de embarazos adolescentes
        - Acceso limitado a educación sexual
        - Falta de proyectos de vida
        """)
    
    st.subheader("🚨 Problemas Identificados")
    
    st.error("""
    **Riesgos identificados:**
    - Embarazo sin control prenatal
    - Abandono escolar
    - Pobreza intergeneracional
    - Riesgo de complicaciones obstétricas
    - Falta de apoyo familiar
    """)
    
    st.subheader("💡 Intervenciones Propuestas")
    
    st.markdown("**Intervenciones Inmediatas:**")
    st.write("1. **Control prenatal:** Derivación urgente a matrona")
    st.write("2. **Apoyo psicosocial:** Acompañamiento individual")
    st.write("3. **Educación:** Continuidad escolar")
    st.write("4. **Apoyo familiar:** Orientación a la madre")
    
    st.markdown("**Intervenciones Comunitarias:**")
    st.write("• Programa de educación sexual integral")
    st.write("• Talleres de proyecto de vida")
    st.write("• Acceso a métodos anticonceptivos")
    st.write("• Apoyo a madres adolescentes")
    st.write("• Prevención en colegios")
    
    st.markdown("---")
    st.markdown("### 📚 Recursos Adicionales")
    st.markdown("""
    - **Protocolos de atención:** Consulta los protocolos vigentes del MINSAL
    - **Redes de apoyo:** Identifica organizaciones comunitarias disponibles
    - **Educación continua:** Participa en capacitaciones sobre salud familiar
    - **Supervisión:** Mantén comunicación regular con tu supervisor
    """)

def mostrar_caso_don_carlos():
    st.header("🏥 Caso Clínico: Don Carlos - Monitoreo Remoto de Hipertensión")
    
    # Contexto del caso
    st.subheader("📋 Contexto")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Datos del Paciente:**
        - **Nombre:** Don Carlos
        - **Edad:** 58 años
        - **Ocupación:** Minero jubilado
        - **Lugar de residencia:** Pueblo minero aislado
        """)
        
        st.markdown("""
        **Contexto Comunitario:**
        - **CESFAM:** A 2 horas de distancia
        - **PSR:** Solo TENS 3 veces por semana
        - **Acceso a internet:** Limitado (solo en centro del pueblo)
        - **Transporte:** Escaso, especialmente en invierno
        """)
    
    with col2:
        st.markdown("""
        **Diagnósticos:**
        - Hipertensión Arterial
        - Diabetes Mellitus Tipo 2
        - Obesidad
        
        **Medicamentos:**
        - Losartán 50mg 1x día
        - Metformina 850mg 2x día
        """)
        
        st.markdown("""
        **Última evaluación:**
        - **Fecha:** Hace 3 meses
        - **Presión arterial:** 160/100 mmHg
        - **Glicemia:** 145 mg/dL
        - **Peso:** 85 kg
        """)
    
    # Situación clínica actual
    st.subheader("📱 Implementación de Monitoreo Remoto")
    
    st.info("""
    **Intervención TICS propuesta:**
    - **Dispositivo:** Tensiómetro digital con conectividad
    - **Frecuencia:** Medición diaria de presión arterial
    - **Plataforma:** Aplicación móvil para registro
    - **Alerta:** Notificación automática si PA > 140/90
    """)
    
    # Beneficios del monitoreo remoto
    st.subheader("✅ Beneficios del Monitoreo Remoto")
    
    beneficios = {
        "🏥 Control Continuo": "Mediciones diarias sin traslados",
        "🚨 Detección Temprana": "Alertas automáticas de valores elevados",
        "💰 Ahorro de Costos": "Menos traslados al CESFAM",
        "📊 Datos Precisos": "Registro automático sin errores humanos",
        "👨‍⚕️ Seguimiento Médico": "Datos disponibles para el médico",
        "🎯 Adherencia": "Recordatorios automáticos de medicación"
    }
    
    for beneficio, descripcion in beneficios.items():
        st.markdown(f"**{beneficio}:** {descripcion}")
    
    # Plan de implementación
    st.subheader("📋 Plan de Implementación")
    
    pasos = [
        "1. **Capacitación:** Enseñar uso del tensiómetro digital",
        "2. **Instalación:** Configurar aplicación móvil",
        "3. **Prueba piloto:** 2 semanas de monitoreo",
        "4. **Evaluación:** Revisar datos y ajustar",
        "5. **Implementación completa:** Monitoreo continuo"
    ]
    
    for paso in pasos:
        st.markdown(paso)
    
    # Análisis de impacto
    st.subheader("📈 Análisis de Impacto Esperado")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Reducción Traslados", "70%", "vs atención tradicional")
        st.metric("Mejora Control PA", "85%", "valores en rango normal")
    
    with col2:
        st.metric("Ahorro Costos", "60%", "gastos en transporte")
        st.metric("Satisfacción", "90%", "paciente y familia")
    
    # Preguntas de reflexión
    st.subheader("🤔 Preguntas de Reflexión")
    
    preguntas = [
        "¿Cómo podrías adaptar esta intervención para otras condiciones crónicas?",
        "¿Qué barreras tecnológicas podrías encontrar en zonas rurales?",
        "¿Cómo involucrarías a la familia en el monitoreo remoto?",
        "¿Qué indicadores usarías para medir el éxito de la intervención?"
    ]
    
    for i, pregunta in enumerate(preguntas, 1):
        st.markdown(f"**{i}.** {pregunta}")

def mostrar_caso_sra_ana():
    st.header("🏥 Caso Clínico: Sra. Ana - Telemedicina para Control Prenatal")
    
    # Contexto del caso
    st.subheader("📋 Contexto")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Datos de la Paciente:**
        - **Nombre:** Sra. Ana
        - **Edad:** 28 años
        - **Ocupación:** Dueña de casa
        - **Lugar de residencia:** Comunidad costera aislada
        """)
        
        st.markdown("""
        **Contexto Comunitario:**
        - **CESFAM:** A 1.5 horas por camino de tierra
        - **Hospital:** A 3 horas de distancia
        - **Acceso a servicios:** Limitado por malas condiciones del camino
        - **Clima:** Lluvioso en invierno, dificulta traslados
        """)
    
    with col2:
        st.markdown("""
        **Datos del Embarazo:**
        - **Semanas de gestación:** 24 semanas
        - **Embarazo:** Primigesta
        - **Complicaciones:** Ninguna hasta el momento
        - **Grupo sanguíneo:** O+
        """)
        
        st.markdown("""
        **Último control:**
        - **Fecha:** Hace 2 semanas
        - **Peso:** 65 kg (+3 kg desde inicio)
        - **Presión arterial:** 110/70 mmHg
        - **Movimientos fetales:** Normales
        """)
    
    # Situación actual
    st.subheader("🤰 Situación Actual")
    
    st.warning("""
    **Síntomas recientes:**
    - Náuseas ocasionales
    - Fatiga
    - Dolor lumbar leve
    - Inquietud sobre el desarrollo del bebé
    """)
    
    # Implementación de telemedicina
    st.subheader("📱 Implementación de Telemedicina")
    
    st.info("""
    **Intervención TICS propuesta:**
    - **Plataforma:** Videollamada con matrona/obstetra
    - **Frecuencia:** Control prenatal semanal
    - **Equipamiento:** Estetoscopio digital, ecógrafo portátil
    - **Apoyo:** TENS presente durante consulta
    """)
    
    # Beneficios específicos
    st.subheader("✅ Beneficios de la Telemedicina Prenatal")
    
    beneficios = {
        "🏥 Control Regular": "Consultas semanales sin traslados",
        "👶 Monitoreo Fetal": "Ecografía y auscultación remota",
        "📚 Educación": "Charlas sobre embarazo y parto",
        "🚨 Detección Precoz": "Identificación temprana de complicaciones",
        "👨‍👩‍👧‍👦 Familia": "Participación del padre en controles",
        "💰 Ahorro": "Reducción de gastos en transporte"
    }
    
    for beneficio, descripcion in beneficios.items():
        st.markdown(f"**{beneficio}:** {descripcion}")
    
    # Plan de atención
    st.subheader("📋 Plan de Atención Telemedicina")
    
    controles = [
        "**Semana 24-28:** Control general, ecografía de crecimiento",
        "**Semana 28-32:** Control de movimientos fetales, educación",
        "**Semana 32-36:** Preparación para el parto, plan de traslado",
        "**Semana 36-40:** Control final, indicaciones de parto"
    ]
    
    for control in controles:
        st.markdown(control)
    
    # Indicadores de seguimiento
    st.subheader("📊 Indicadores de Seguimiento")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Controles Realizados", "95%", "vs 60% tradicional")
        st.metric("Detección Precoz", "80%", "complicaciones identificadas")
    
    with col2:
        st.metric("Satisfacción", "92%", "paciente y familia")
        st.metric("Ahorro Tiempo", "75%", "vs traslados tradicionales")
    
    # Preguntas de reflexión
    st.subheader("🤔 Preguntas de Reflexión")
    
    preguntas = [
        "¿Cómo manejarías una emergencia obstétrica en telemedicina?",
        "¿Qué equipamiento mínimo necesitarías para telemedicina prenatal?",
        "¿Cómo involucrarías a la familia en el control prenatal remoto?",
        "¿Qué protocolos de derivación establecerías para casos complejos?"
    ]
    
    for i, pregunta in enumerate(preguntas, 1):
        st.markdown(f"**{i}.** {pregunta}") 