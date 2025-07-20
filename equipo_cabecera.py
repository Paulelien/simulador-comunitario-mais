import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def mostrar_equipo_cabecera():
    st.markdown("""
    <div class="section-header">
        <h2>👥 Equipo de Cabecera</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ### 🏥 ¿Qué es el Equipo de Cabecera?
    
    El equipo de cabecera es el grupo de profesionales de salud que se responsabiliza 
    de la atención integral de las familias asignadas a un sector específico. 
    Incluye médicos, enfermeras, TENS, matronas y otros profesionales según las necesidades.
    """)
    
    # Verificar si hay sectores registrados
    if not st.session_state.sectores:
        st.warning("⚠️ Primero debes registrar sectores en la sección de Sectorización.")
        st.info("Ve a la sección '🗺️ Sectorización' para agregar sectores antes de continuar.")
        return
    
    # Formulario para asignar equipos
    with st.expander("➕ Asignar Equipo a Sector", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            sector_seleccionado = st.selectbox(
                "Seleccionar Sector",
                [s["nombre"] for s in st.session_state.sectores]
            )
            
            # Obtener información del sector seleccionado
            sector_info = next((s for s in st.session_state.sectores if s["nombre"] == sector_seleccionado), None)
            
            if sector_info:
                st.info(f"📊 **Sector:** {sector_info['nombre']}")
                st.info(f"👨‍👩‍👧‍👦 **Familias:** {sector_info['num_familias']}")
                st.info(f"👥 **Población:** {sector_info['poblacion_total']}")
        
        with col2:
            st.markdown("**Composición del Equipo:**")
            
            num_medicos = st.number_input("Médicos", min_value=0, value=1)
            num_enfermeras = st.number_input("Enfermeras", min_value=0, value=2)
            num_tens = st.number_input("TENS", min_value=0, value=3)
            num_matronas = st.number_input("Matronas", min_value=0, value=1)
            num_psicologos = st.number_input("Psicólogos", min_value=0, value=1)
            num_otros = st.number_input("Otros Profesionales", min_value=0, value=0)
        
        # Información adicional del equipo
        st.markdown("**Información del Equipo:**")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            jefe_equipo = st.text_input("Jefe de Equipo", placeholder="Nombre del jefe")
            telefono_contacto = st.text_input("Teléfono de Contacto", placeholder="+56 9 XXXX XXXX")
        
        with col2:
            horario_atencion = st.selectbox(
                "Horario de Atención",
                ["Lunes a Viernes 8:00-17:00", "Lunes a Viernes 8:00-18:00", 
                 "Lunes a Sábado 8:00-17:00", "Turnos rotativos", "Otro"]
            )
            modalidad_trabajo = st.selectbox(
                "Modalidad de Trabajo",
                ["Presencial", "Híbrido", "Telemedicina", "Mixto"]
            )
        
        with col3:
            experiencia_promedio = st.number_input("Experiencia Promedio (años)", min_value=0, value=5)
            capacitacion_mais = st.checkbox("Capacitación en MAIS", value=True)
        
        # Microáreas
        st.markdown("**Organización en Microáreas:**")
        col1, col2 = st.columns(2)
        
        with col1:
            num_microareas = st.number_input("Número de Microáreas", min_value=1, value=4)
            familias_por_microarea = sector_info["num_familias"] // num_microareas if sector_info else 0
            st.info(f"📋 Familias por microárea: ~{familias_por_microarea}")
        
        with col2:
            responsable_microarea = st.selectbox(
                "Responsable por Microárea",
                ["TENS", "Enfermera", "Médico", "Mixto"]
            )
        
        if st.button("💾 Guardar Equipo", type="primary"):
            if jefe_equipo:
                nuevo_equipo = {
                    "sector": sector_seleccionado,
                    "composicion": {
                        "medicos": num_medicos,
                        "enfermeras": num_enfermeras,
                        "tens": num_tens,
                        "matronas": num_matronas,
                        "psicologos": num_psicologos,
                        "otros": num_otros
                    },
                    "informacion": {
                        "jefe_equipo": jefe_equipo,
                        "telefono": telefono_contacto,
                        "horario": horario_atencion,
                        "modalidad": modalidad_trabajo,
                        "experiencia": experiencia_promedio,
                        "capacitacion_mais": capacitacion_mais
                    },
                    "microareas": {
                        "numero": num_microareas,
                        "familias_por_microarea": familias_por_microarea,
                        "responsable": responsable_microarea
                    },
                    "sector_info": sector_info
                }
                
                # Verificar si ya existe un equipo para este sector
                equipo_existente = next((e for e in st.session_state.equipos if e["sector"] == sector_seleccionado), None)
                if equipo_existente:
                    # Actualizar equipo existente
                    index = st.session_state.equipos.index(equipo_existente)
                    st.session_state.equipos[index] = nuevo_equipo
                    st.success(f"✅ Equipo del sector '{sector_seleccionado}' actualizado exitosamente!")
                else:
                    # Agregar nuevo equipo
                    st.session_state.equipos.append(nuevo_equipo)
                    st.success(f"✅ Equipo asignado al sector '{sector_seleccionado}' exitosamente!")
                
                st.rerun()
            else:
                st.error("❌ Por favor ingresa el nombre del jefe de equipo")
    
    # Mostrar equipos existentes
    if st.session_state.equipos:
        st.markdown("### 📊 Equipos Asignados")
        
        # Crear DataFrame para visualización
        equipos_data = []
        for equipo in st.session_state.equipos:
            composicion = equipo["composicion"]
            total_profesionales = sum(composicion.values())
            
            equipos_data.append({
                "Sector": equipo["sector"],
                "Jefe de Equipo": equipo["informacion"]["jefe_equipo"],
                "Total Profesionales": total_profesionales,
                "Médicos": composicion["medicos"],
                "Enfermeras": composicion["enfermeras"],
                "TENS": composicion["tens"],
                "Matronas": composicion["matronas"],
                "Psicólogos": composicion["psicologos"],
                "Otros": composicion["otros"],
                "Microáreas": equipo["microareas"]["numero"],
                "Familias por Microárea": equipo["microareas"]["familias_por_microarea"]
            })
        
        df_equipos = pd.DataFrame(equipos_data)
        
        # Mostrar tabla
        st.dataframe(df_equipos, use_container_width=True)
        
        # Gráficos
        col1, col2 = st.columns(2)
        
        with col1:
            # Gráfico de composición profesional
            fig_composicion = px.bar(
                df_equipos,
                x="Sector",
                y=["Médicos", "Enfermeras", "TENS", "Matronas", "Psicólogos", "Otros"],
                title="Composición Profesional por Sector",
                barmode='stack'
            )
            fig_composicion.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig_composicion, use_container_width=True)
        
        with col2:
            # Gráfico de microáreas
            fig_microareas = px.bar(
                df_equipos,
                x="Sector",
                y="Microáreas",
                title="Número de Microáreas por Sector",
                color="Familias por Microárea",
                color_continuous_scale="viridis"
            )
            fig_microareas.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig_microareas, use_container_width=True)
        
        # Análisis de cobertura
        st.markdown("### 📈 Análisis de Cobertura")
        
        cobertura_data = []
        for equipo in st.session_state.equipos:
            # Obtener información del sector desde los datos de sectorización
            sector_nombre = equipo["sector"]
            sector_info = None
            
            # Buscar información del sector en los datos de sectorización
            if "sectores" in st.session_state:
                for sector in st.session_state.sectores:
                    if sector["nombre"] == sector_nombre:
                        sector_info = sector
                        break
            
            # Si no encontramos información del sector, usar valores por defecto
            if sector_info is None:
                sector_info = {
                    "num_familias": 100,
                    "poblacion_total": 400
                }
            
            composicion = equipo["composicion"]
            total_profesionales = sum(composicion.values())
            
            # Calcular ratios
            ratio_familias_tens = sector_info["num_familias"] / composicion["tens"] if composicion["tens"] > 0 else 0
            ratio_poblacion_medico = sector_info["poblacion_total"] / composicion["medicos"] if composicion["medicos"] > 0 else 0
            
            cobertura_data.append({
                "Sector": equipo["sector"],
                "Familias por TENS": ratio_familias_tens,
                "Población por Médico": ratio_poblacion_medico,
                "Total Profesionales": total_profesionales,
                "Número de Familias": sector_info["num_familias"]
            })
        
        df_cobertura = pd.DataFrame(cobertura_data)
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig_ratio_tens = px.bar(
                df_cobertura,
                x="Sector",
                y="Familias por TENS",
                title="Familias por TENS",
                color="Familias por TENS",
                color_continuous_scale="RdYlGn_r"
            )
            fig_ratio_tens.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig_ratio_tens, use_container_width=True)
        
        with col2:
            fig_ratio_medico = px.bar(
                df_cobertura,
                x="Sector",
                y="Población por Médico",
                title="Población por Médico",
                color="Población por Médico",
                color_continuous_scale="RdYlGn_r"
            )
            fig_ratio_medico.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig_ratio_medico, use_container_width=True)
        
        # Recomendaciones
        st.markdown("### 💡 Recomendaciones")
        
        for equipo in st.session_state.equipos:
            sector = equipo["sector"]
            composicion = equipo["composicion"]
            
            # Obtener información del sector desde los datos de sectorización
            sector_info = None
            if "sectores" in st.session_state:
                for s in st.session_state.sectores:
                    if s["nombre"] == sector:
                        sector_info = s
                        break
            
            # Si no encontramos información del sector, usar valores por defecto
            if sector_info is None:
                sector_info = {
                    "num_familias": 100,
                    "poblacion_total": 400
                }
            
            st.markdown(f"**Sector: {sector}**")
            
            # Evaluar ratios
            familias_por_tens = sector_info["num_familias"] / composicion["tens"] if composicion["tens"] > 0 else 0
            poblacion_por_medico = sector_info["poblacion_total"] / composicion["medicos"] if composicion["medicos"] > 0 else 0
            
            if familias_por_tens > 150:
                st.warning(f"⚠️ Ratio familias/TENS muy alto ({familias_por_tens:.1f}). Considerar aumentar TENS.")
            elif familias_por_tens < 50:
                st.success(f"✅ Ratio familias/TENS óptimo ({familias_por_tens:.1f})")
            else:
                st.info(f"ℹ️ Ratio familias/TENS aceptable ({familias_por_tens:.1f})")
            
            if poblacion_por_medico > 2000:
                st.warning(f"⚠️ Ratio población/médico muy alto ({poblacion_por_medico:.1f}). Considerar aumentar médicos.")
            elif poblacion_por_medico < 1000:
                st.success(f"✅ Ratio población/médico óptimo ({poblacion_por_medico:.1f})")
            else:
                st.info(f"ℹ️ Ratio población/médico aceptable ({poblacion_por_medico:.1f})")
            
            st.markdown("---")
    
    else:
        st.info("📝 No hay equipos asignados. Asigna equipos a los sectores usando el formulario de arriba.")
    
    # Botón para limpiar datos
    if st.session_state.equipos:
        if st.button("🗑️ Limpiar Todos los Equipos"):
            st.session_state.equipos = []
            st.success("✅ Todos los equipos han sido eliminados")
            st.rerun() 