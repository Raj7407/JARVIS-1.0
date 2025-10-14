import asyncio
import threading
import os
import edge_tts
import pygame
Voice= "en-HK-SamNeural"
BUFFER_SIZE=1024
def remove_file(file_path):
    max_attempts =3
    attempt =0
    while attempt<max_attempts:
      with open (file_path,"wb"):
        os.remove(file_path)
        break
async def amain(TEXT,output_file)   -> None:
    try:
        cm_txt=  edge_tts.Communicate(TEXT,Voice)
        await cm_txt.save(output_file)
        thread= threading.Thread(target=play_audio,args=(output_file,))
        thread.start()
        thread.join()
    except Exception as e:
        print (e)
    


def play_audio(file_path):
    try:
        pygame.init()
        pygame .mixer.init()
        sound = pygame.mixer.Sound(file_path)
        sound.play() 
        while pygame.mixer.get_busy():
            pygame.time.Clock().tick(10) 
        pygame.quit()

    except Exception as e:
        print(e)
def speak(Text, output_file=None):
    try:
        if output_file is None:
            output_file = f"{os.getcwd()}/speech.mp3"
        asyncio.run(amain(Text, output_file))
    except Exception as e:   # fixed
        print(e)

speak("hello i am jarvis")  
speak("hello palash sir, how may i help you today")   
                              

