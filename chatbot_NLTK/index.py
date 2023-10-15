# pip install nltk

import nltk
from nltk.chat.util import Chat,reflections



def chatbot():
    print("hola, soy un chatbot. ¿En que puedo ayudarte?")
    
    #* Definir los pares de patrones y respuestas
    pairs = [
        [r"mi nombre es (.*)",["Hola %1, ¿Cómo puedo ayudarte hoy"]],
        [r"cual es tu nombre",["Mi nombre es Chatbot. ¿Cómo puedo ayudarte hoy"]],
        [r"como estas?",["Estoy bien, ¿y tú"]],
        [r"chao",["!Hasta luego"]], 
    ]
    
    # *Creacion del chatbot
    
    chat = Chat(pairs,reflections)
    chat.converse()
    
if __name__ == "__main__":
    nltk.download("punkt")
    chatbot()