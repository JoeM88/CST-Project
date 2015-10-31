import wave
import pygame

pygame.init()

def GameMusic():
    CHANNELS = 1
    Change_Rate = 1

    Change_Rate = 3
    song = wave.open('keygen.wav', 'rb') #opens the original wav file
    RATE = song.getframerate() #stores the rate
    signal = song.readframes(-1) #reads the frames
    sample_width = song.getsampwidth() #gets the sample width

    faster_song = wave.open("keygen2.wav", 'wb') #Creates a new new wav file called faster song
    faster_song.setnchannels(CHANNELS) #sets the channels, sample rate, and the framerate
    faster_song.setsampwidth(sample_width)
    faster_song.setframerate(RATE * 4) #multiplies the original rate by four 
    faster_song.writeframes(signal)
    faster_song.close() #Closes the wav file
    sound = pygame.mixer.Sound('C:\\Users\\Joseph Molina\\Desktop\\CST\\keygen2.wav') # opens the new wav file that we just created
    sound.play(loops = -1) #plays it indefinately
