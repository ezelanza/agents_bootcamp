import streamlit as st
from agentes_fiesta import CoordinadorFiesta
import pandas as pd
import time

# Configuración de página
st.set_page_config(
    page_title="Planificador de Fiestas Multi-Agente",
    page_icon="🎉",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados
st.markdown("""
<style>
    .agent-box {
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 15px;
    }
    .chef-box {
        background-color: #ffeeee;
        border-left: 5px solid #ff6b6b;
    }
    .dj-box {
        background-color: #eef6ff;
        border-left: 5px solid #4dabf7;
    }
    .decorator-box {
        background-color: #f4f9f0;
        border-left: 5px solid #69db7c;
    }
    .interaction {
        background-color: #fff8e6;
        border-left: 5px solid #ffd43b;
        padding: 10px;
        border-radius: 5px;
        margin-top: 5px;
        font-style: italic;
    }
    .main-title {
        font-size: 3rem !important;
        color: #333;
        text-align: center;
        margin-bottom: 30px !important;
    }
    .emoji-big {
        font-size: 2.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Título
st.markdown("<h1 class='main-title'>🎉 Planificador de Fiestas Multi-Agente 🎉</h1>", unsafe_allow_html=True)

# Inicializar coordinador
@st.cache_resource
def obtener_coordinador():
    return CoordinadorFiesta()

coordinador = obtener_coordinador()

# Sidebar para estadísticas y opciones
with st.sidebar:
    st.header("📊 Estadísticas")
    stats = coordinador.gestor_db.obtener_estadisticas_fiesta()
    st.metric("Total de fiestas planificadas", stats['total_parties'])
    st.metric("Presupuesto promedio", f"${stats['average_budget']}")
    st.metric("Promedio de invitados", stats['average_guests'])
    
    st.divider()
    
    st.header("🔍 Ver fiesta anterior")
    plan_id = st.number_input("ID de la fiesta", min_value=1, step=1)
    if st.button("Buscar"):
        plan = coordinador.gestor_db.obtener_plan_fiesta(plan_id)
        if plan:
            st.success(f"Fiesta #{plan['id']} encontrada!")
            st.write(f"**Tema**: {plan['theme']}")
            st.write(f"**Invitados**: {plan['guests']}")
            st.write(f"**Presupuesto**: ${plan['budget']}")
            with st.expander("Ver detalles completos"):
                st.write("**Comida:**")
                st.write(plan['food_plan'])
                st.write("**Música:**")
                st.write(plan['music_plan'])
                st.write("**Decoración:**")
                st.write(plan['decoration_plan'])
        else:
            st.error("No se encontró una fiesta con ese ID.")

# Formulario para nueva fiesta
st.header("📝 Planear nueva fiesta")
with st.form("party_form"):
    tema = st.text_input("¿Cuál es el tema de tu fiesta?", placeholder="Ejemplo: Halloween, Años 80, Superhéroes")
    col1, col2 = st.columns(2)
    with col1:
        invitados = st.number_input("¿Cuántos invitados tendrás?", min_value=1, max_value=1000, value=50)
    with col2:
        presupuesto = st.number_input("Presupuesto (USD)", min_value=100, max_value=100000, value=1000, step=100)
    
    submit = st.form_submit_button("¡Planear mi fiesta!")

# Procesar el formulario
if submit:
    with st.spinner("🧠 Consultando a nuestros expertos..."):
        # Mostrar proceso de planificación
        progress_container = st.empty()
        progress_bar = st.progress(0)
        
        # Etapa 1: Consultar experiencias previas
        progress_container.info("🔍 Consultando experiencias previas...")
        progress_bar.progress(10)
        time.sleep(0.5)
        
        # Etapa 2: Consultar al Chef
        progress_container.info("👨‍🍳 Consultando al Chef para el menú perfecto...")
        progress_bar.progress(30)
        pregunta_comida = f"Necesito un menú divertido para una fiesta {tema} con {invitados} invitados y presupuesto de ${presupuesto}."
        respuesta_comida = coordinador.chef({
            "context": f"Fiesta {tema}",
            "question": pregunta_comida
        })
        time.sleep(0.5)
        
        # Etapa 3: Consultar al DJ
        progress_container.info("🎧 Consultando al DJ para la música ideal...")
        progress_bar.progress(60)
        pregunta_musica = f"¿Qué música recomiendas para una fiesta {tema}? Necesito crear un ambiente increíble."
        respuesta_musica = coordinador.dj({
            "context": f"Fiesta {tema}",
            "question": pregunta_musica,
            "food_response": respuesta_comida
        })
        time.sleep(0.5)
        
        # Etapa 4: Consultar al Decorador
        progress_container.info("🎨 Consultando al Decorador para el ambiente perfecto...")
        progress_bar.progress(90)
        pregunta_decoracion = f"¿Cómo decorarías un espacio para una fiesta {tema} con {invitados} invitados?"
        respuesta_decoracion = coordinador.decorador({
            "context": f"Fiesta {tema}",
            "question": pregunta_decoracion,
            "food_response": respuesta_comida,
            "music_response": respuesta_musica
        })
        
        # Guardar en la base de datos
        id_plan = coordinador.gestor_db.guardar_plan_fiesta(
            tema=tema,
            invitados=invitados,
            presupuesto=presupuesto,
            plan_comida=respuesta_comida,
            plan_musica=respuesta_musica,
            plan_decoracion=respuesta_decoracion
        )
        
        # Completar
        progress_bar.progress(100)
        progress_container.success("✅ ¡Plan completado!")
        time.sleep(0.5)
    
    # Limpiar contenedores de progreso
    progress_container.empty()
    progress_bar.empty()
    
    # Mostrar resultados
    st.header(f"🎉 Tu Plan para la Fiesta de {tema} 🎉")
    st.subheader(f"Presupuesto: ${presupuesto} | Invitados: {invitados} | ID: {id_plan}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Mostrar respuesta del Chef
        st.markdown(f"""
        <div class="agent-box chef-box">
            <h3>👨‍🍳 Menú recomendado</h3>
            <p>{respuesta_comida.replace('\n', '<br>')}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Mostrar respuesta del Decorador
        st.markdown(f"""
        <div class="agent-box decorator-box">
            <h3>🎨 Decoración</h3>
            <p>{respuesta_decoracion.replace('\n', '<br>')}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Mostrar respuesta del DJ
        st.markdown(f"""
        <div class="agent-box dj-box">
            <h3>🎧 Música y ambiente</h3>
            <p>{respuesta_musica.replace('\n', '<br>')}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Mostrar sección de interacción entre agentes
    st.subheader("🤝 Colaboración entre agentes")
    
    # Extraer y mostrar comentarios de interacción
    chef_dj_interaction = ""
    if "👨‍🍳➡️🎧" in respuesta_musica:
        chef_dj_interaction = respuesta_musica.split("👨‍🍳➡️🎧")[1].strip()
    
    chef_decorator_interaction = ""
    if "👨‍🍳➡️🎨" in respuesta_decoracion:
        chef_decorator_interaction = respuesta_decoracion.split("👨‍🍳➡️🎨")[1].split("\n")[0].strip()
    
    dj_decorator_interaction = ""
    if "🎧➡️🎨" in respuesta_decoracion:
        dj_decorator_interaction = respuesta_decoracion.split("🎧➡️🎨")[1].split("\n")[0].strip()
    
    if chef_dj_interaction or chef_decorator_interaction or dj_decorator_interaction:
        interaction_html = '<div class="interaction">'
        if chef_dj_interaction:
            interaction_html += f'<p><strong>👨‍🍳➡️🎧 Chef → DJ:</strong> {chef_dj_interaction}</p>'
        if chef_decorator_interaction:
            interaction_html += f'<p><strong>👨‍🍳➡️🎨 Chef → Decorador:</strong> {chef_decorator_interaction}</p>'
        if dj_decorator_interaction:
            interaction_html += f'<p><strong>🎧➡️🎨 DJ → Decorador:</strong> {dj_decorator_interaction}</p>'
        interaction_html += '</div>'
        st.markdown(interaction_html, unsafe_allow_html=True)
    else:
        st.info("Los agentes trabajaron de forma independiente para esta temática.")
    
    # Botón para compartir/guardar
    st.button("🔄 Planear otra fiesta", on_click=lambda: st.experimental_rerun())
else:
    # Mostrar pantalla inicial cuando no hay resultados
    st.info("👆 Completa el formulario y haz clic en 'Planear mi fiesta' para comenzar.")
    
    # Mostrar información sobre los agentes
    st.subheader("Nuestro equipo de agentes expertos")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="text-align: center">
            <div class="emoji-big">👨‍🍳</div>
            <h3>Chef</h3>
            <p>Experto en crear menús temáticos deliciosos que se adaptan a tu presupuesto y número de invitados.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="text-align: center">
            <div class="emoji-big">🎧</div>
            <h3>DJ</h3>
            <p>Maestro musical que selecciona la banda sonora perfecta basada en la temática y las recomendaciones del Chef.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="text-align: center">
            <div class="emoji-big">🎨</div>
            <h3>Decorador</h3>
            <p>Artista creativo que diseña el ambiente perfecto coordinando con las sugerencias del Chef y DJ.</p>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("💡 **Planificador de Fiestas Multi-Agente** · Creado con ❤️ y Streamlit") 