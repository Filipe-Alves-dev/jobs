from pygame import mixer
mixer.init()
mixer.music.load('Uai (Ao Vivo)(MP3_160K).mp3')
mixer.music.play()
mixer.music.set_volume(0.1)

while True:
    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program ")
    query = input(" ")
    if query == 'p':
        mixer.music.pause()
    elif query == 'r':
        mixer.music.unpause()
    elif query == 'e':
        mixer.music.stop()
        break
