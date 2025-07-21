import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime
import hashlib

class SistemaUsuarios:
    def __init__(self):
        self.directorio_usuarios = "datos_usuarios"
        self.crear_directorio_usuarios()
    
    def crear_directorio_usuarios(self):
        """Crea el directorio para almacenar datos de usuarios"""
        if not os.path.exists(self.directorio_usuarios):
            os.makedirs(self.directorio_usuarios)
    
    def generar_id_usuario(self, nombre, email):
        """Genera un ID único para cada usuario"""
        texto = f"{nombre}_{email}_{datetime.now().strftime('%Y%m%d')}"
        return hashlib.md5(texto.encode()).hexdigest()[:8]
    
    def registrar_usuario(self, nombre, email, curso):
        """Registra un nuevo usuario"""
        user_id = self.generar_id_usuario(nombre, email)
        
        datos_usuario = {
            "user_id": user_id,
            "nombre": nombre,
            "email": email,
            "curso": curso,
            "fecha_registro": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "datos": {
                "sectores": [],
                "equipos": [],
                "familias": [],
                "instituciones": [],
                "plan_intervencion": [],
                "diagnostico": None,
                "autoevaluacion": None,
                "evaluacion_mais": None
            }
        }
        
        # Guardar datos del usuario
        archivo_usuario = f"{self.directorio_usuarios}/{user_id}.json"
        with open(archivo_usuario, 'w', encoding='utf-8') as f:
            json.dump(datos_usuario, f, indent=2, ensure_ascii=False)
        
        return user_id
    
    def cargar_datos_usuario(self, user_id):
        """Carga los datos de un usuario específico"""
        archivo_usuario = f"{self.directorio_usuarios}/{user_id}.json"
        
        if os.path.exists(archivo_usuario):
            with open(archivo_usuario, 'r', encoding='utf-8') as f:
                datos_usuario = json.load(f)
            
            # Cargar datos en session state
            st.session_state.user_id = user_id
            st.session_state.nombre_usuario = datos_usuario["nombre"]
            st.session_state.email_usuario = datos_usuario["email"]
            st.session_state.curso_usuario = datos_usuario["curso"]
            
            # Cargar datos del proyecto
            datos = datos_usuario["datos"]
            st.session_state.sectores = datos.get("sectores", [])
            st.session_state.equipos = datos.get("equipos", [])
            st.session_state.familias = datos.get("familias", [])
            st.session_state.instituciones = datos.get("instituciones", [])
            st.session_state.plan_intervencion = datos.get("plan_intervencion", [])
            st.session_state.diagnostico = datos.get("diagnostico")
            st.session_state.autoevaluacion = datos.get("autoevaluacion")
            st.session_state.evaluacion_mais = datos.get("evaluacion_mais")
            
            return True
        return False
    
    def guardar_datos_usuario(self, user_id):
        """Guarda los datos actuales del usuario"""
        archivo_usuario = f"{self.directorio_usuarios}/{user_id}.json"
        
        if os.path.exists(archivo_usuario):
            with open(archivo_usuario, 'r', encoding='utf-8') as f:
                datos_usuario = json.load(f)
            
            # Actualizar datos del proyecto
            datos_usuario["datos"] = {
                "sectores": st.session_state.get("sectores", []),
                "equipos": st.session_state.get("equipos", []),
                "familias": st.session_state.get("familias", []),
                "instituciones": st.session_state.get("instituciones", []),
                "plan_intervencion": st.session_state.get("plan_intervencion", []),
                "diagnostico": st.session_state.get("diagnostico"),
                "autoevaluacion": st.session_state.get("autoevaluacion"),
                "evaluacion_mais": st.session_state.get("evaluacion_mais")
            }
            
            # Guardar archivo actualizado
            with open(archivo_usuario, 'w', encoding='utf-8') as f:
                json.dump(datos_usuario, f, indent=2, ensure_ascii=False)
    
    def listar_usuarios(self):
        """Lista todos los usuarios registrados"""
        usuarios = []
        for archivo in os.listdir(self.directorio_usuarios):
            if archivo.endswith('.json'):
                with open(f"{self.directorio_usuarios}/{archivo}", 'r', encoding='utf-8') as f:
                    datos_usuario = json.load(f)
                    usuarios.append({
                        "user_id": datos_usuario["user_id"],
                        "nombre": datos_usuario["nombre"],
                        "email": datos_usuario["email"],
                        "curso": datos_usuario["curso"],
                        "fecha_registro": datos_usuario["fecha_registro"]
                    })
        return usuarios

def mostrar_login():
    """Interfaz de login/registro"""
    st.markdown("## 👤 Sistema de Usuarios")
    
    # Información de autoría
    st.markdown("""
    <div style="text-align: center; padding: 10px; background-color: #f0f2f6; border-radius: 5px; margin-bottom: 20px;">
        <p style="color: #666; font-size: 12px; margin: 0;">
            Aplicación educativa desarrollada por Ricardo Delannoy Suazo para formación en diagnóstico comunitario en salud familiar.<br>
            © 2025. Todos los derechos reservados.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    sistema = SistemaUsuarios()
    
    # Verificar si ya hay un usuario logueado
    if "user_id" in st.session_state:
        st.success(f"✅ Conectado como: **{st.session_state.nombre_usuario}**")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("💾 Guardar Progreso"):
                sistema.guardar_datos_usuario(st.session_state.user_id)
                st.success("✅ Progreso guardado exitosamente!")
        
        with col2:
            if st.button("🚪 Cerrar Sesión"):
                # Limpiar session state
                for key in list(st.session_state.keys()):
                    del st.session_state[key]
                st.rerun()
        
        return True
    
    # Formulario de login/registro
    tab1, tab2 = st.tabs(["🔐 Iniciar Sesión", "📝 Registrarse"])
    
    with tab1:
        st.markdown("### Iniciar Sesión")
        
        email_login = st.text_input("Email:")
        user_id_login = st.text_input("ID de Usuario (8 caracteres):")
        
        if st.button("🔑 Iniciar Sesión"):
            if email_login and user_id_login:
                if sistema.cargar_datos_usuario(user_id_login):
                    st.success("✅ Sesión iniciada exitosamente!")
                    st.rerun()
                else:
                    st.error("❌ Usuario no encontrado. Verifica el ID.")
            else:
                st.warning("⚠️ Completa todos los campos.")
    
    with tab2:
        st.markdown("### Registrarse")
        
        nombre_registro = st.text_input("Nombre completo:")
        email_registro = st.text_input("Email:", key="email_reg")
        curso_registro = st.selectbox(
            "Curso:",
            ["TENS - Salud Familiar y Comunitaria", "Otro curso"]
        )
        
        if st.button("📝 Crear Cuenta"):
            if nombre_registro and email_registro:
                user_id = sistema.registrar_usuario(nombre_registro, email_registro, curso_registro)
                st.success(f"✅ Cuenta creada exitosamente!")
                st.info(f"**Tu ID de usuario es: {user_id}**")
                st.warning("⚠️ **Guarda este ID, lo necesitarás para iniciar sesión.**")
                
                # Iniciar sesión automáticamente
                sistema.cargar_datos_usuario(user_id)
                st.rerun()
            else:
                st.warning("⚠️ Completa todos los campos.")
    
    return False

def mostrar_admin():
    """Panel de administración para profesores"""
    st.markdown("## 👨‍🏫 Panel de Administración")
    
    sistema = SistemaUsuarios()
    usuarios = sistema.listar_usuarios()
    
    if usuarios:
        st.markdown("### 📊 Usuarios Registrados")
        
        df_usuarios = pd.DataFrame(usuarios)
        st.dataframe(df_usuarios, use_container_width=True)
        
        # Estadísticas
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Usuarios", len(usuarios))
        with col2:
            cursos_unicos = df_usuarios["curso"].nunique()
            st.metric("Cursos", cursos_unicos)
        with col3:
            fecha_mas_reciente = max(usuarios, key=lambda x: x["fecha_registro"])
            st.metric("Último Registro", str(fecha_mas_reciente["fecha_registro"][:10]))
        
        # Exportar datos
        if st.button("📤 Exportar Datos de Usuarios"):
            csv_data = df_usuarios.to_csv(index=False)
            st.download_button(
                label="💾 Descargar CSV",
                data=csv_data,
                file_name=f"usuarios_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv"
            )
    else:
        st.info("📝 No hay usuarios registrados aún.")

if __name__ == "__main__":
    mostrar_login() 