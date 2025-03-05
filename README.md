# 🤖 Agents Bootcamp

Este repositorio contiene material educativo sobre agentes inteligentes y un ejemplo práctico de implementación.

## 📚 Contenido

### 1. Jupyter Notebook Explicativo (`agents.ipynb`)
Un notebook interactivo que explica:
- Conceptos fundamentales de agentes inteligentes
- Tipos de agentes y sus características
- Comunicación entre agentes
- Patrones de diseño para sistemas multi-agente
- Ejemplos prácticos y ejercicios

### 2. Ejemplo Práctico: Planificador de Fiestas Multi-Agente 🎉

Una implementación práctica que demuestra los conceptos aprendidos, donde múltiples agentes colaboran para planificar una fiesta perfecta.

#### Agentes Implementados

El sistema utiliza tres agentes especializados que trabajan juntos:

- **👨‍🍳 Chef**: Experto en crear menús temáticos que se adaptan a tu presupuesto y número de invitados
- **🎧 DJ**: Maestro musical que selecciona la banda sonora perfecta basada en la temática y las recomendaciones del Chef
- **🎨 Decorador**: Artista creativo que diseña el ambiente perfecto coordinando con las sugerencias del Chef y DJ

#### Características del Ejemplo

- Planificación interactiva de fiestas
- Temas predefinidos (80s, Halloween, Navidad, Medieval, Superhéroes)
- Recomendaciones personalizadas basadas en presupuesto y número de invitados
- Colaboración inteligente entre agentes
- Almacenamiento de planes anteriores para referencia
- Interfaz web amigable con Streamlit

## 🚀 Comenzando

### Requisitos Previos

```bash
pip install -r requirements.txt
```

### Uso

1. **Estudio de Agentes**:
```bash
jupyter notebook agents.ipynb
```
Este notebook te guiará a través de los conceptos fundamentales de agentes inteligentes con ejemplos interactivos.

2. **Ejemplo Práctico (Planificador de Fiestas)**:
```bash
streamlit run planificador_fiestas_app.py
```
Prueba la implementación práctica de un sistema multi-agente.

## 🗂️ Estructura del Proyecto

### Material Educativo
- `agents.ipynb`: Notebook principal con explicaciones y ejemplos
- `agents/`: Directorio con módulos de soporte y ejemplos adicionales

### Implementación de Ejemplo (Planificador de Fiestas)
- `planificador_fiestas_app.py`: Aplicación Streamlit
- `agentes_fiesta.py`: Implementación de los agentes
- `gestor_base_datos.py`: Gestión de la base de datos

## 🤝 Interacción entre Agentes en el Ejemplo

El planificador de fiestas demuestra la colaboración entre agentes:

1. El Chef propone el menú basado en el tema y presupuesto
2. El DJ adapta la música considerando las sugerencias del Chef
3. El Decorador coordina el ambiente basándose en las propuestas del Chef y DJ

## 📊 Persistencia de Datos

El sistema incluye una base de datos SQLite para:
- Almacenar planes anteriores
- Consultar estadísticas
- Proporcionar inspiración basada en experiencias previas

## 🛠️ Desarrollo

Para contribuir al proyecto:

1. Fork el repositorio
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Crea un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia Apache 2.0.

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Puedes ayudar:
- Agregando más ejemplos educativos
- Mejorando la documentación
- Expandiendo la funcionalidad del planificador de fiestas
- Reportando bugs
- Sugiriendo mejoras 