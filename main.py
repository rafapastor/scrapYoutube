from pytube import Channel, YouTube

# URL del canal de YouTube (asegúrate de que es la URL de la pestaña "Videos")
channel_url = "https://www.youtube.com/c/NOMBRE_DEL_CANAL/videos"

# Crear objeto Channel
channel = Channel(channel_url)

print(f"Descargando videos de: {channel.channel_name}")

# Descargar todos los videos del canal
for url in channel.video_urls:
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    print(f"Descargando: {yt.title}")
    stream.download(output_path="videos_del_canal")  # Carpeta donde se guardarán los videos

print("Descarga completada!")
