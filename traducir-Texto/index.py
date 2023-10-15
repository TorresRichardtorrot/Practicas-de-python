from googletrans import Translator

translator = Translator()
translated = translator.translate(
    """My focus on technology and development has led me to becoming an
       autodidact, always looking to learn new skills and keep up to date 
       with the latest trends in Web development""",
       src='en',dest="es"
)

print(translated.text)