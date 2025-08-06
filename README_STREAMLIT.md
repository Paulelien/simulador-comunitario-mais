# 🏥 Simulador Comunitario - Streamlit Cloud

## 📋 Descripción

Aplicación educativa para formación en diagnóstico comunitario en salud familiar, específicamente diseñada para Técnicos en Enfermería (TENS). Incluye módulos de educación para la salud, promoción de la salud, objetivos SMART y modelo de creencias en salud.

## 🚀 Despliegue en Streamlit Cloud

### Archivo Principal
- **Main file path:** `app_streamlit_cloud.py`

### Dependencias
- **Requirements file:** `requirements.txt`
- **Packages file:** `packages.txt`

### Configuración
- **Python version:** 3.9+
- **Streamlit version:** 1.47.1

## 📚 Módulos Disponibles

### 1. 🎯 Objetivos SMART
- Formulación de objetivos específicos, medibles, alcanzables, relevantes y con tiempo definido
- Categorización por tipo de prevención
- Seguimiento del estado de cumplimiento

### 2. 📖 Intervenciones Educativas
- Diseño de estrategias educativas individuales y grupales
- Metodologías educativas (role playing, casos clínicos, etc.)
- Planificación de recursos y duración

### 3. 🧠 Modelo de Creencias en Salud
- Evaluación de susceptibilidad, severidad, beneficios y barreras
- Gráficos de radar para visualizar percepciones
- Recomendaciones basadas en el análisis

### 4. 📊 Dashboard
- Métricas de progreso
- Gráficos de distribución
- Exportación de datos

## 🛠️ Instalación Local

```bash
# Clonar repositorio
git clone https://github.com/Paulelien/simulador-comunitario-mais.git

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación
streamlit run app_streamlit_cloud.py
```

## 📁 Estructura del Proyecto

```
simulador-comunitario-mais/
├── app_streamlit_cloud.py      # Archivo principal para Streamlit Cloud
├── requirements.txt            # Dependencias de Python
├── packages.txt               # Paquetes del sistema
├── .streamlit/
│   └── config.toml           # Configuración de Streamlit
└── README_STREAMLIT.md       # Este archivo
```

## 🔧 Configuración de Streamlit Cloud

1. **Accede a:** https://share.streamlit.io/
2. **Conecta tu repositorio:** `Paulelien/simulador-comunitario-mais`
3. **Main file path:** `app_streamlit_cloud.py`
4. **Requirements file:** `requirements.txt`
5. **Deploy!**

## 📊 Características Técnicas

- **Framework:** Streamlit 1.47.1
- **Visualización:** Plotly 5.17.0
- **Análisis de datos:** Pandas 2.0.3
- **Generación de reportes:** ReportLab 4.0.4
- **Cálculos numéricos:** NumPy 1.24.3

## 🎯 Enfoque TENS

La aplicación está específicamente diseñada para Técnicos en Enfermería, incluyendo:

- **Educación para la salud** con enfoque comunitario
- **Promoción de la salud** en APS
- **Objetivos SMART** para intervenciones
- **Modelo de creencias en salud** para evaluación
- **Dashboard** para seguimiento de programas

## 📞 Soporte

Para problemas técnicos o consultas sobre el despliegue, revisa:

1. **Logs de Streamlit Cloud** en el dashboard
2. **Dependencias** en `requirements.txt`
3. **Configuración** en `.streamlit/config.toml`

## 📄 Licencia

© 2025 Ricardo Delannoy Suazo. Todos los derechos reservados. 