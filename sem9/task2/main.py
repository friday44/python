
from pytube import YouTube
import telebot

bot = telebot.TeleBot('5636976148:AAHl3nSmTgOpQTXJ2gzBr1vSxmcXbvDVZo4')

@bot.message_handler(commands = ['start'])
def start(message):
    link = f'{message.from_user.first_name}, введите ссылку на видео: '
    bot.send_message(message.chat.id, link)
    yt = YouTube(link)
    bot.send_message(message.chat.id, f'Длина видео: {yt.length} секунд')
    yt = yt.streams.get_by_itag("18")    #скачивание
    yt.download('Downloads')
    bot.send_message(message.chat.id, f'Видео скачано')
    bot.send_video(message.chat.id, str(yt) + '.mp4') #загрузка видео в чат

bot.polling(none_stop=True)


# link = input("Введите ссылку на видео: ")
# yt = YouTube(link)
# print("Длина: ", yt.length, "секунд")
# yt = yt.streams.get_by_itag("18")
# yt.download('Downloads')
# print("Видео скачано")



