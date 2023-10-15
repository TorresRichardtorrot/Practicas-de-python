from gtts import gTTS
#* El gTTS (Google Text-to-Speech) es una biblioteca de Python que permite convertir texto en voz utilizando
#* las voces de síntesis de Google. Es útil cuando deseas agregar funcionalidad de síntesis de voz a un
#* programa Python o a una aplicación web. El gTTS es fácil de usar y admite varios idiomas y voces.


archivo = open("libro.txt","r", encoding="utf-8")
texto = archivo.read()
archivo.close()

tts = gTTS(text=texto,lang="en")
tts.save("audio-book.mp3")