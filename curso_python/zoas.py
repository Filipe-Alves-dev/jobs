import os
from pydub import AudioSegment
from pydub.playback import play
import yt_dlp

def tocar_musica(link):
    # Configurações do yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',  # Nome do arquivo de saída
    }

    # Baixando o áudio
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(link, download=True)
        titulo = info['title'] + '.mp3'  # Nome do arquivo baixado

    # Tocando a música
    audio = AudioSegment.from_mp3(titulo)
    play(audio)

    # Remover o arquivo após tocar
    os.remove(titulo)

# Exemplo de uso
link_musica = input("Digite o link da música do YouTube: ")
tocar_musica(link_musica)