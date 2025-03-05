from langchain_core.prompts import PromptTemplate
from gestor_base_datos import GestorBaseDatos
import os
from dotenv import load_dotenv
import time
import random
from typing import Dict, Any, Optional, List, Union

# Cargar variables de entorno
load_dotenv()

# Clase para un LLM simulado simple sin dependencias externas
class SimuladorLLM:
    def __init__(self):
        pass
    
    def invoke(self, prompt_str):
        """Procesa el prompt y devuelve una respuesta apropiada"""
        prompt_lower = prompt_str.lower()
        
        # Detectar el tipo de agente y contexto de interacción
        # Uso una detección más estricta para cada agente
        is_chef = "respuesta divertida del chef" in prompt_lower
        is_dj = "respuesta cool del dj" in prompt_lower
        is_decorator = "respuesta creativa del decorador" in prompt_lower
        
        # Detectar si hay recomendaciones previas de otros agentes
        chef_recommendations = ""
        if "recomendaciones del chef:" in prompt_lower:
            # Extraer recomendaciones del chef del prompt
            chef_start = prompt_lower.find("recomendaciones del chef:")
            if chef_start > -1:
                chef_end = prompt_lower.find("contexto actual:", chef_start)
                if chef_end > -1:
                    chef_recommendations = prompt_lower[chef_start:chef_end]
        
        dj_recommendations = ""
        if "recomendaciones del dj:" in prompt_lower:
            # Extraer recomendaciones del DJ del prompt
            dj_start = prompt_lower.find("recomendaciones del dj:")
            if dj_start > -1:
                dj_end = prompt_lower.find("contexto actual:", dj_start)
                if dj_end > -1:
                    dj_recommendations = prompt_lower[dj_start:dj_end]
        
        # Detectar el tema de la fiesta
        theme = self._extract_theme(prompt_lower)
        
        # Generar respuesta según el tipo de agente y tema, considerando recomendaciones previas
        if is_chef:
            return self._get_food_response(theme)
        elif is_dj:
            return self._get_music_response(theme, chef_recommendations)
        elif is_decorator:
            return self._get_decor_response(theme, chef_recommendations, dj_recommendations)
        else:
            # Si no se puede determinar el tipo, intentar inferirlo del contenido
            if "comida" in prompt_lower or "menú" in prompt_lower or "bebida" in prompt_lower:
                return self._get_food_response(theme)
            elif "música" in prompt_lower or "canciones" in prompt_lower:
                return self._get_music_response(theme, chef_recommendations)
            elif "decoración" in prompt_lower or "ambiente" in prompt_lower:
                return self._get_decor_response(theme, chef_recommendations, dj_recommendations)
            else:
                return "¡No estoy seguro de qué recomendar para esta fiesta!"
    
    def _extract_theme(self, text):
        """Extrae el tema de la fiesta del prompt"""
        if "80s" in text or "años 80" in text or "ochentas" in text:
            return "80s"
        elif "halloween" in text or "terror" in text:
            return "halloween"
        elif "navidad" in text or "christmas" in text:
            return "navidad"
        elif "medieval" in text:
            return "medieval"
        elif "superhéroes" in text or "superheroes" in text:
            return "superhéroes"
        else:
            return "general"
    
    def _get_food_response(self, theme):
        """Devuelve ideas de comida según el tema"""
        responses = {
            "80s": "¡Viajemos en el tiempo con estos sabores ochentas!\n\n" + 
                  "- Mini hamburguesas 'Pac-Man'\n" + 
                  "- Hot dogs 'Miami Vice'\n" +
                  "- Pizza cortada en cuadrados coloridos estilo Rubik\n" +
                  "- Ponche de frutas neón\n" +
                  "- Palomitas con colorante en tonos fluorescentes",
            
            "halloween": "¡Un festín terroríficamente delicioso!\n\n" +
                        "- 'Dedos de zombie' (hot dogs envueltos en masa teñida de verde)\n" +
                        "- 'Cerebros de gelatina' en moldes anatómicos\n" +
                        "- 'Ponche de sangre' con frutas flotantes\n" +
                        "- Mini pizzas con 'arañas' de aceitunas\n" +
                        "- Cupcakes decorados con tumbas de chocolate",
                        
            "navidad": "¡Una cena festiva perfecta para la ocasión!\n\n" +
                     "- Ponche de frutas caliente con canela y clavo\n" +
                     "- Galletas decoradas de bastones de caramelo\n" +
                     "- Mini pasteles de frutas navideños\n" +
                     "- Chocolate caliente con malvaviscos\n" +
                     "- Canapés con forma de árbol de Navidad",
                     
            "medieval": "¡Un banquete digno del rey Arturo!\n\n" +
                       "- Piernas de pollo asadas 'estilo medieval'\n" +
                       "- Pan rústico con dips variados\n" +
                       "- Pastel de carne en molde de castillo\n" +
                       "- Hidromiel (o sidra para niños)\n" +
                       "- Frutas servidas en bandejas de madera",
                       
            "superhéroes": "¡Comida con superpoderes!\n\n" +
                          "- Mini hamburguesas 'Hulk' (con pan verde)\n" +
                          "- 'Escudos del Capitán América' (galletas decoradas)\n" +
                          "- 'Telarañas de Spider-Man' (pretzels bañados en chocolate)\n" +
                          "- Batidos de varios colores para cada superhéroe\n" +
                          "- Fruta cortada con formas de símbolos heroicos"
        }
        
        return responses.get(theme, "¡Para tu fiesta recomiendo estas delicias!\n\n" + 
                            "- Tabla de quesos y embutidos variados\n" +
                            "- Mini sándwiches surtidos\n" +
                            "- Brochetas de frutas coloridas\n" +
                            "- Punch de frutas refrescante\n" +
                            "- Pequeños brownies y galletas para el postre")
    
    def _get_music_response(self, theme, chef_recommendations=""):
        """Devuelve ideas de música según el tema y considerando la comida"""
        # Base responses
        responses = {
            "80s": "¡Prepárate para viajar en el tiempo con estos ritmos!\n\n" +
                  "- Michael Jackson - Thriller y Billie Jean\n" +
                  "- Madonna - Like a Prayer y Material Girl\n" +
                  "- Queen - Another One Bites the Dust\n" +
                  "- Cyndi Lauper - Girls Just Want to Have Fun\n" +
                  "- A-ha - Take On Me",
            
            "halloween": "¡La playlist perfecta para una noche espeluznante!\n\n" +
                        "- Thriller - Michael Jackson\n" +
                        "- Highway to Hell - AC/DC\n" +
                        "- Superstition - Stevie Wonder\n" +
                        "- Ghostbusters - Ray Parker Jr.\n" +
                        "- Monster Mash - Bobby Pickett",
                        
            "navidad": "¡Una selección musical que traerá el espíritu navideño!\n\n" +
                      "- All I Want for Christmas Is You - Mariah Carey\n" +
                      "- Last Christmas - Wham!\n" +
                      "- Jingle Bell Rock - Bobby Helms\n" +
                      "- Feliz Navidad - José Feliciano\n" +
                      "- Versiones modernas de villancicos clásicos",
                      
            "medieval": "¡Música que te transportará a otra época!\n\n" +
                       "- Música celta instrumental\n" +
                       "- Bandas sonoras de Juego de Tronos o El Señor de los Anillos\n" +
                       "- Versiones modernas de música medieval\n" +
                       "- Música de laúd y arpa para momentos tranquilos\n" +
                       "- Tambores tribales para momentos más animados",
                       
            "superhéroes": "¡Música épica para héroes épicos!\n\n" +
                          "- Bandas sonoras de películas de Marvel y DC\n" +
                          "- We Will Rock You - Queen\n" +
                          "- Holding Out for a Hero - Bonnie Tyler\n" +
                          "- Thunderstruck - AC/DC\n" +
                          "- Immigrant Song - Led Zeppelin (Thor: Ragnarok)"
        }
        
        base_response = responses.get(theme, "¡Mi selección musical perfecta para tu fiesta!\n\n" +
                            "- Hits actuales que todos conocen\n" +
                            "- Clásicos bailables de distintas épocas\n" +
                            "- Música latina para animar el ambiente\n" +
                            "- Éxitos de los 2000 para la nostalgia\n" +
                            "- Canciones lentas para el final de la fiesta")
        
        # Añadir comentarios basados en recomendaciones del chef
        food_comment = ""
        if chef_recommendations:
            if "pizza" in chef_recommendations.lower():
                food_comment = "\n\n👨‍🍳➡️🎧 He notado que el Chef recomendó pizza, así que añadiré algo de rock italiano como Måneskin o música disco que va perfecta con la pizza."
            elif "ponche" in chef_recommendations.lower() or "bebidas" in chef_recommendations.lower():
                food_comment = "\n\n👨‍🍳➡️🎧 El Chef recomendó bebidas vibrantes, así que incluiré canciones que inviten a bailar y brindar como 'Raise Your Glass' de Pink y 'Cheers (Drink to That)' de Rihanna."
            else:
                food_comment = "\n\n👨‍🍳➡️🎧 Viendo las recomendaciones del Chef, he adaptado mi playlist para crear el ambiente perfecto mientras disfrutan de esa deliciosa comida."
        
        return base_response + food_comment
    
    def _get_decor_response(self, theme, chef_recommendations="", dj_recommendations=""):
        """Devuelve ideas de decoración según el tema, comida y música"""
        # Base responses
        responses = {
            "80s": "¡Transformaremos el espacio en una explosión ochentera!\n\n" +
                  "- Neones por todas partes - tubos flexibles LED en colores brillantes\n" +
                  "- Posters de películas clásicas de los 80s: Volver al Futuro, E.T., Los Cazafantasmas\n" +
                  "- Una máquina de arcade vintage (o una recreación con cartón)\n" +
                  "- Cubos de Rubik gigantes como centros de mesa\n" +
                  "- Casetes y vinilos colgando del techo",
            
            "halloween": "¡Una decoración que pondrá los pelos de punta!\n\n" +
                        "- Telarañas artificiales en cada esquina\n" +
                        "- Calabazas talladas con luces LED internas\n" +
                        "- Siluetas de murciélagos y gatos negros en las paredes\n" +
                        "- Un 'cementerio' miniatura en una mesa\n" +
                        "- Luces negras para crear un ambiente sobrenatural",
                        
            "navidad": "¡Un ambiente mágico lleno del espíritu navideño!\n\n" +
                      "- Árbol de Navidad como pieza central\n" +
                      "- Luces blancas cálidas por todas partes\n" +
                      "- Guirnaldas y coronas en puertas y paredes\n" +
                      "- Mesa decorada con motivos navideños y velas\n" +
                      "- Pequeños adornos temáticos como detalles para los invitados",
                      
            "medieval": "¡Un castillo digno de la realeza!\n\n" +
                       "- Estandartes y banderas colgando del techo\n" +
                       "- Candelabros (reales o LED) para la iluminación\n" +
                       "- Mesa principal con aspecto de banquete medieval\n" +
                       "- Elementos decorativos como escudos, espadas y armaduras\n" +
                       "- Tapices o telas que simulen tapices antiguos",
                       
            "superhéroes": "¡Un cuartel general para tus superhéroes favoritos!\n\n" +
                          "- Paneles de cómic ampliados como decoración de pared\n" +
                          "- Globos en los colores de los superhéroes principales\n" +
                          "- Centros de mesa con figuras de acción\n" +
                          "- Símbolos icónicos (Escudo del Capitán América, S de Superman) como decoración\n" +
                          "- Cabina de fotos con accesorios de superhéroes"
        }
        
        base_response = responses.get(theme, "¡Crearemos un ambiente festivo y elegante!\n\n" +
                            "- Iluminación suave y acogedora\n" +
                            "- Centros de mesa con flores o velas\n" +
                            "- Globos en colores que combinen con la temática\n" +
                            "- Mantelería y servilletas elegantes\n" +
                            "- Un área para fotos con un fondo atractivo")
        
        # Comentarios basados en las recomendaciones previas
        additional_comments = []
        
        if chef_recommendations:
            if "hamburguesas" in chef_recommendations.lower():
                additional_comments.append("👨‍🍳➡️🎨 Dado que el Chef sugirió hamburguesas, voy a añadir una zona temática tipo 'diner' americano con servilleteros y menús vintage.")
            elif "ponche" in chef_recommendations.lower():
                additional_comments.append("👨‍🍳➡️🎨 Para complementar el ponche del Chef, añadiré una estación de bebidas decorada espectacularmente con luces que combinen con los colores del ponche.")
        
        if dj_recommendations:
            if "michael jackson" in dj_recommendations.lower():
                additional_comments.append("🎧➡️🎨 Veo que el DJ incluirá música de Michael Jackson, así que añadiré un guante blanco brillante como pieza decorativa y algunas siluetas de baile icónicas.")
            elif "queen" in dj_recommendations.lower():
                additional_comments.append("🎧➡️🎨 Para acompañar la música de Queen, incorporaré elementos visuales inspirados en sus portadas de discos más icónicas.")
            elif "bandas sonoras" in dj_recommendations.lower():
                additional_comments.append("🎧➡️🎨 Con la música épica que ha seleccionado el DJ, crearé zonas temáticas que evoquen esas películas, con iluminación dinámica que cambiará con el ritmo.")
        
        # Añadir comentarios si hay alguno
        if additional_comments:
            integration_text = "\n\n✨ Coordinación con el equipo ✨\n" + "\n".join(additional_comments)
            return base_response + integration_text
        else:
            return base_response

# Crear instancia del modelo simulado
llm = SimuladorLLM()

# Agente Chef - Experto en comida y bebidas
def agente_chef(inputs):
    prompt = f"""Eres un chef experto y divertido. Tu trabajo es sugerir comida y bebidas para fiestas.
    
    Contexto actual: {inputs['context']}
    Pregunta: {inputs['question']}
    
    Respuesta divertida del Chef:"""
    return llm.invoke(prompt)

# Agente DJ - Experto en música
def agente_dj(inputs):
    # Aseguramos que las recomendaciones del chef se transmitan correctamente
    chef_recommendations = inputs.get('food_response', '')
    
    prompt = f"""Eres un DJ experto y muy cool. Tu trabajo es sugerir música perfecta para fiestas.
    
    Recomendaciones del Chef: {chef_recommendations}
    
    Contexto actual: {inputs['context']}
    Pregunta: {inputs['question']}
    
    Respuesta cool del DJ:"""
    return llm.invoke(prompt)

# Agente Decorador - Experto en decoración
def agente_decorador(inputs):
    # Aseguramos que las recomendaciones del chef y DJ se transmitan correctamente
    chef_recommendations = inputs.get('food_response', '')
    dj_recommendations = inputs.get('music_response', '')
    
    prompt = f"""Eres un decorador creativo y extravagante. Tu trabajo es sugerir decoraciones temáticas.
    
    Recomendaciones del Chef: {chef_recommendations}
    Recomendaciones del DJ: {dj_recommendations}
    
    Contexto actual: {inputs['context']}
    Pregunta: {inputs['question']}
    
    Respuesta creativa del Decorador:"""
    return llm.invoke(prompt)

def formatear_fiestas_previas(fiestas):
    if not fiestas:
        return "No hay fiestas similares anteriores."
    
    formatted = "Fiestas anteriores relevantes:\n"
    for fiesta in fiestas:
        formatted += f"\nFiesta #{fiesta['id']} - Tema: {fiesta['theme']}\n"
        formatted += f"Invitados: {fiesta['guests']} | Presupuesto: ${fiesta['budget']}\n"
        formatted += f"Comida: {fiesta['food_plan']}\n"
        formatted += f"Música: {fiesta['music_plan']}\n"
        formatted += f"Decoración: {fiesta['decoration_plan']}\n"
        formatted += "-" * 50 + "\n"
    return formatted

# Coordinador de la Fiesta - El agente principal que coordina todo
class CoordinadorFiesta:
    def __init__(self):
        self.chef = agente_chef
        self.dj = agente_dj
        self.decorador = agente_decorador
        self.plan_fiesta = {}
        self.gestor_db = GestorBaseDatos()
    
    def obtener_info_fiestas_similares(self, tema, presupuesto):
        fiestas_similares = self.gestor_db.obtener_fiestas_similares(tema, presupuesto)
        return formatear_fiestas_previas(fiestas_similares)
    
    def planificar_fiesta(self, tema, invitados, presupuesto):
        print("🎉 ¡Iniciando planificación de fiesta!\n")
        
        # Obtener información de fiestas similares
        info_fiestas_previas = self.obtener_info_fiestas_similares(tema, presupuesto)
        print("🔍 Consultando experiencias previas...\n")
        
        # Paso 1: Consultar al Chef
        pregunta_comida = f"Necesito un menú divertido para una fiesta {tema} con {invitados} invitados y presupuesto de ${presupuesto}."
        respuesta_comida = self.chef({
            "previous_parties": info_fiestas_previas,
            "context": f"Fiesta {tema}",
            "question": pregunta_comida
        })
        print("👨‍🍳 Chef dice:", respuesta_comida, "\n")
        time.sleep(1)
        
        # Paso 2: Consultar al DJ (ahora con conocimiento de la comida)
        pregunta_musica = f"¿Qué música recomiendas para una fiesta {tema}? Necesito crear un ambiente increíble."
        respuesta_musica = self.dj({
            "previous_parties": info_fiestas_previas,
            "context": f"Fiesta {tema}",
            "question": pregunta_musica,
            "food_response": respuesta_comida  # Pasar las recomendaciones del chef
        })
        print("🎧 DJ dice:", respuesta_musica, "\n")
        time.sleep(1)
        
        # Paso 3: Consultar al Decorador (con conocimiento de comida y música)
        pregunta_decoracion = f"¿Cómo decorarías un espacio para una fiesta {tema} con {invitados} invitados?"
        respuesta_decoracion = self.decorador({
            "previous_parties": info_fiestas_previas,
            "context": f"Fiesta {tema}",
            "question": pregunta_decoracion,
            "food_response": respuesta_comida,  # Pasar recomendaciones del chef
            "music_response": respuesta_musica  # Pasar recomendaciones del DJ
        })
        print("🎨 Decorador dice:", respuesta_decoracion, "\n")
        
        # Guardar el plan en la base de datos
        id_plan = self.gestor_db.guardar_plan_fiesta(
            tema=tema,
            invitados=invitados,
            presupuesto=presupuesto,
            plan_comida=respuesta_comida,
            plan_musica=respuesta_musica,
            plan_decoracion=respuesta_decoracion
        )
        
        self.plan_fiesta = {
            "id": id_plan,
            "tema": tema,
            "invitados": invitados,
            "presupuesto": presupuesto,
            "comida": respuesta_comida,
            "música": respuesta_musica,
            "decoración": respuesta_decoracion
        }
        
        print("🤝 Los agentes han colaborado exitosamente para crear un plan coherente y armonioso.\n")
        return f"¡Plan de fiesta completado y guardado! 🎉 (ID: {id_plan})"
    
    def __del__(self):
        self.gestor_db.cerrar()

# Ejemplo de uso
if __name__ == "__main__":
    coordinador = CoordinadorFiesta()
    print(coordinador.planificar_fiesta(
        tema="Piratas del Caribe",
        invitados=30,
        presupuesto=1000
    )) 