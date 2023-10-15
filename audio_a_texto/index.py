
import speech_recognition as sr
from pydub import AudioSegment
import pyaudio
import wave

class Transcribir:
    def __init__(
        self,
        formato:pyaudio,
        canales:int,
        tasa_muestreo:int,
        tamanio_bufe:int,
        duracion_grabacion:int,
        ruta_archivo:str,
        ):
            self.formato = formato
            self.canales = canales
            self.tasa_muestreo = tasa_muestreo
            self.tamanio_bufe = tamanio_bufe
            self.duracion_grabacion = duracion_grabacion
            self.ruta_archivo = ruta_archivo
            
    def grabacion_de_audio(self):
        try:
            audio = pyaudio.PyAudio()
            stream = audio.open(
                format = self.formato,
                channels=self.canales,
                rate=self.tasa_muestreo,
                input=True,
                frames_per_buffer = self.tamanio_bufe,
            )
            print("Grabacion enpesada..........")
            
            frames = []
                
            #*Grabacion del audio
            for i in range(0, int(self.tasa_muestreo / self.tamanio_bufe * self.duracion_grabacion)):
                data= stream.read(self.tamanio_bufe)
                frames.append(data)
                   
            print("Grabacion finalizada")
            
            #*Detener el stream y cerrar Pyaudio
            stream.stop_stream()
            stream.close()
            audio.terminate()
            
            #*Guardar la grabacion
            
            wf = wave.open(self.ruta_archivo,"wb")
            wf.setnchannels(self.canales)
            wf.setsampwidth(audio.get_sample_size(self.formato))
            wf.setframerate(self.tasa_muestreo)
            wf.writeframes(b"".join(frames))
            wf.close()
            
            
            print(self.ruta_archivo)
            
            resultado = self.transcribir_audio(self.ruta_archivo)
            
            if resultado["estado"] == "success":
                return{
                    "estado":"success",
                    "mensaje":"Proceso culminado con exito",
                    "texto":resultado["texto"]
                }
            return{
                    "estado":"failed",
                    "mensaje":"no se pudo culminar con exito el proceso",
                    "texto":resultado["texto"]
                }    
        except Exception as exception:
            raise NameError(
                f"Ha ocurrido un error al grabar el audio revisa {exception}"
            )            
            
            
   
    def transcribir_audio(self,ruta_audio):
        try:
           print(ruta_audio)
           r = sr.Recognizer()
           audio_file = sr.AudioFile(ruta_audio)
           
           with audio_file as source:
               audio = r.record(source)
               
           texto = r.recognize_google(audio, language="es-ES")   
           
           if texto:
               return {
                   "estado":"success",
                   "mensaje":"Audio transcrito de manera exitosa!",
                   "texto":texto
               }
           return {
                   "estado":"failed",
                   "mensaje":"No se pudo trascribir el audio",
               }
        
        except Exception as exception:
            raise NameError(
                f"Ha ocurrido un error al trascribir el audio revisa {exception}"
            )            
                      
formato = pyaudio.paInt16
canales = 2
tasa_muesteo = 44100
tamanio_bufer = 1024
duracion_grabacion = 15
ruta_audio = "mi-audio.mp3"

transcribir = Transcribir(
    formato,canales,tasa_muesteo,tamanio_bufer,duracion_grabacion,ruta_audio
    )

# print(transcribir.grabacion_de_audio())



def transcribir_mi_audio(ruta_audio_mp3):
        try:
        #    audio_mp3 = AudioSegment.from_mp3(ruta_audio_mp3)
        #    ruta_audio_wav = "audio-temp.wav"
        #    audio_mp3.export(ruta_audio_wav, format="wav")
            
            
           r = sr.Recognizer()
           audio_file = sr.AudioFile("mi-audio.mp3")
           
           with audio_file as source:
               audio = r.record(source)
               
           texto = r.recognize_google(audio, language="es-ES")   
           
           if texto:
               return {
                   "estado":"success",
                   "mensaje":"Audio transcrito de manera exitosa!",
                   "texto":texto
               }
           return {
                   "estado":"failed",
                   "mensaje":"No se pudo trascribir el audio",
               }
        
        except Exception as exception:
            raise NameError(
                f"Ha ocurrido un error al trascribir el audio revisa {exception}"
            )   
            

ruta_audio_mp3 = "mi-audio.mp3"          
            
# print(transcribir_mi_audio(ruta_audio_mp3))