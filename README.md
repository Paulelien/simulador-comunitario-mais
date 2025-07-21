# 🏥 Simulador Comunitario MAIS

**Aplicación educativa desarrollada por Ricardo Delannoy Suazo para formación en diagnóstico comunitario en salud familiar.**

Herramienta de aprendizaje interactiva para estudiantes TENS en el área de Salud Familiar y Comunitaria, basada en el Modelo de Atención Integral en Salud (MAIS).

---

## 📋 Descripción

Aplicación web interactiva desarrollada con Streamlit para estudiantes TENS del curso "Salud Familiar y Comunitaria". El simulador permite practicar el proceso completo de elaboración de un diagnóstico comunitario en APS (Atención Primaria en Salud) siguiendo el enfoque del Modelo de Atención Integral en Salud Familiar (MAIS).

## 🎯 Objetivos

- **Sectorización del territorio**: Organizar y delimitar áreas geográficas
- **Formación de equipos de cabecera**: Asignar profesionales por sector
- **Registro de familias**: Capturar información familiar relevante
- **Identificación de factores de riesgo**: Detectar riesgos sociales y sanitarios
- **Trabajo en red intersectorial**: Coordinar con instituciones comunitarias
- **Plan de intervención**: Diseñar estrategias de intervención integral

## 🚀 Instalación

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar o descargar el proyecto**
   ```bash
   git clone <url-del-repositorio>
   cd simulador_comunitario
   ```

2. **Crear entorno virtual (recomendado)**
   ```bash
   python -m venv venv
   
   # En Windows
   venv\Scripts\activate
   
   # En macOS/Linux
   source venv/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación**
   ```bash
   streamlit run app.py
   ```

5. **Abrir en el navegador**
   La aplicación se abrirá automáticamente en `http://localhost:8501`

## 📖 Cómo Usar el Simulador

### 1. 🏠 Inicio
- Bienvenida y objetivos del simulador
- Información del curso
- Progreso del diagnóstico

### 2. 🗺️ Sectorización
- **Agregar sectores**: Define áreas geográficas con características específicas
- **Características del territorio**: Servicios básicos, problemas identificados
- **Visualización**: Gráficos y mapas esquemáticos de sectores

### 3. 👥 Equipo de Cabecera
- **Asignar equipos**: Composición profesional por sector
- **Microáreas**: Organización territorial
- **Análisis de cobertura**: Ratios y recomendaciones

### 4. 👨‍👩‍👧‍👦 Registro de Familias
- **Registrar familias**: Información demográfica y de salud
- **Cálculo automático de riesgos**: Social y sanitario
- **Análisis de vulnerabilidad**: Identificación de grupos prioritarios

### 5. 🔍 Diagnóstico
- **Análisis de datos**: Interpretación de información recopilada
- **Formulario de diagnóstico**: Preguntas orientadoras
- **Identificación de problemas**: Priorización de intervenciones

### 6. 🌐 Trabajo en Red
- **Registrar instituciones**: Organizaciones comunitarias disponibles
- **Análisis de red**: Fortalezas y oportunidades
- **Coordinación intersectorial**: Mapeo de actores clave

### 7. 📋 Plan de Intervención
- **Crear actividades**: Objetivos, responsables, cronograma
- **Recursos necesarios**: Presupuesto y materiales
- **Indicadores de evaluación**: Medición de resultados

### 8. 📊 Evaluación
- **Autoevaluación**: Reflexión sobre el proceso de aprendizaje
- **Exportación de datos**: PDF, Excel, JSON
- **Recomendaciones finales**: Mejoras y próximos pasos

## 🛠️ Características Técnicas

### Tecnologías Utilizadas
- **Streamlit**: Framework web para la interfaz
- **Pandas**: Manipulación y análisis de datos
- **Plotly**: Visualizaciones interactivas
- **ReportLab**: Generación de PDFs
- **OpenPyXL**: Exportación a Excel

### Funcionalidades Principales
- ✅ Interfaz intuitiva y responsiva
- ✅ Guardado automático de datos (Session State)
- ✅ Cálculo automático de factores de riesgo
- ✅ Visualizaciones interactivas
- ✅ Exportación en múltiples formatos
- ✅ Autoevaluación del proceso
- ✅ Navegación guiada por pasos

## 📊 Estructura de Datos

### Sectores
```json
{
  "nombre": "Sector Norte",
  "poblacion_total": 1000,
  "num_familias": 250,
  "tipo_territorio": "Urbano",
  "nivel_socioeconomico": "Medio",
  "vulnerabilidad": "Media",
  "servicios": {...},
  "problemas": [...]
}
```

### Familias
```json
{
  "sector": "Sector Norte",
  "apellido": "González",
  "num_integrantes": 4,
  "jefe_hogar": {...},
  "vivienda": {...},
  "salud": {...},
  "riesgos": {
    "social": {"nivel": "Alto", "puntaje": 12},
    "sanitario": {"nivel": "Medio", "puntaje": 6}
  }
}
```

### Plan de Intervención
```json
{
  "nombre": "Taller de Prevención",
  "tipo": "Educativa",
  "objetivo_general": "...",
  "responsables": ["TENS", "Enfermera"],
  "cronograma": {...},
  "indicadores": [...]
}
```

## 🎓 Público Objetivo

- **Estudiantes TENS**: Técnicos en Enfermería de Nivel Superior
- **Curso**: Salud Familiar y Comunitaria
- **Nivel**: Sin experiencia previa en plataformas digitales avanzadas
- **Enfoque**: Modelo MAIS - Atención Primaria en Salud

## 📁 Estructura del Proyecto

```
simulador_comunitario/
├── app.py                 # Archivo principal de la aplicación
├── requirements.txt       # Dependencias del proyecto
├── README.md             # Documentación
├── sectorizacion.py      # Módulo de sectorización
├── equipo_cabecera.py    # Módulo de equipos de cabecera
├── registro_familias.py  # Módulo de registro familiar
├── diagnostico.py        # Módulo de diagnóstico
├── trabajo_red.py        # Módulo de trabajo en red
├── plan_intervencion.py  # Módulo de plan de intervención
└── evaluacion.py         # Módulo de evaluación
```

## 🔧 Personalización

### Modificar Estilos CSS
Los estilos se encuentran en el archivo `app.py` dentro de la sección `st.markdown(""<style>...")`.

### Agregar Nuevos Campos
Para agregar nuevos campos a los formularios, modifica los archivos de módulos correspondientes.

### Cambiar Cálculos de Riesgo
Los algoritmos de cálculo de riesgo se encuentran en `registro_familias.py` en las funciones:
- `calcular_riesgo_social()`
- `calcular_riesgo_sanitario()`

## 🐛 Solución de Problemas

### Error de Dependencias
```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

### Puerto Ocupado
```bash
streamlit run app.py --server.port 8502
```

### Problemas de Memoria
```bash
streamlit run app.py --server.maxUploadSize 200
```

## 📞 Soporte

Para reportar problemas o solicitar mejoras:
1. Crear un issue en el repositorio
2. Incluir información del sistema operativo
3. Describir el problema detalladamente
4. Adjuntar capturas de pantalla si es necesario

## 📄 Derechos de Autor

Este proyecto es de autoría propia con todos los derechos reservados.

---

## 👨‍💻 Autor

**Ricardo Delannoy Suazo**

- **Proyecto:** Simulador Comunitario MAIS
- **Año:** 2025
- **Propósito:** Herramienta de aprendizaje para TENS
- **Enfoque:** Modelo MAIS - Atención Primaria en Salud

### 📧 Contacto

Para consultas sobre el proyecto educativo, puedes contactar al autor a través de tu institución educativa.

---

**© 2025. Todos los derechos reservados.**

*Este simulador está diseñado específicamente para uso educativo en el contexto de formación de Técnicos en Enfermería de Nivel Superior (TENS) en Chile.* 