
from pytube import YouTube

link = input("Введите ссылку на видео: ")
yt = YouTube(link)
print("Длина: ", yt.length, "секунд")
yt = yt.streams.get_by_itag("18")
yt.download('Downloads')
print("Видео скачано")

