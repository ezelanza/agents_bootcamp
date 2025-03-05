# 🎉 Planificador de Fiestas Multi-Agente

Un sistema de planificación de fiestas que utiliza múltiples agentes inteligentes que colaboran entre sí para crear el plan perfecto para tu fiesta.

## 🤖 Agentes

El sistema utiliza tres agentes especializados que trabajan juntos:

- **👨‍🍳 Chef**: Experto en crear menús temáticos que se adaptan a tu presupuesto y número de invitados
- **🎧 DJ**: Maestro musical que selecciona la banda sonora perfecta basada en la temática y las recomendaciones del Chef
- **🎨 Decorador**: Artista creativo que diseña el ambiente perfecto coordinando con las sugerencias del Chef y DJ

## 🚀 Características

- Planificación interactiva de fiestas
- Temas predefinidos (80s, Halloween, Navidad, Medieval, Superhéroes)
- Recomendaciones personalizadas basadas en presupuesto y número de invitados
- Colaboración inteligente entre agentes
- Almacenamiento de planes anteriores para referencia
- Interfaz web amigable con Streamlit

## 📋 Requisitos

```bash
pip install -r requirements.txt
```

## 🎮 Uso

### Aplicación Web (Streamlit)
```bash
streamlit run planificador_fiestas_app.py
```

### Jupyter Notebook
```bash
jupyter notebook agents.ipynb
```

## 🗂️ Estructura del Proyecto

- `planificador_fiestas_app.py`: Aplicación principal con Streamlit
- `agentes_fiesta.py`: Implementación de los agentes
- `gestor_base_datos.py`: Gestión de la base de datos
- `agents.ipynb`: Notebook con ejemplos de uso
- `requirements.txt`: Dependencias del proyecto

## 🎯 Temas Disponibles

- **80s**: Viaje en el tiempo con música retro y decoración neón
- **Halloween**: Ambiente terroríficamente divertido
- **Navidad**: Espíritu festivo y tradicional
- **Medieval**: Banquete de estilo medieval
- **Superhéroes**: Ambiente de cómic y acción
- Y más temas personalizables...

## 🤝 Interacción entre Agentes

Los agentes colaboran de la siguiente manera:

1. El Chef propone el menú basado en el tema y presupuesto
2. El DJ adapta la música considerando las sugerencias del Chef
3. El Decorador coordina el ambiente basándose en las propuestas del Chef y DJ

## 📊 Base de Datos

El sistema almacena los planes de fiesta para:
- Consultar planes anteriores
- Obtener estadísticas
- Inspirarse en fiestas similares

## 🛠️ Desarrollo

Para contribuir al proyecto:

1. Fork el repositorio
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Crea un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. 