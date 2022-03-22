
from pytube import YouTube
import urllib
import requests
print ("Введите URL видео")
url = input(' ')
video = YouTube(url)
print ("Название видео:")
print(video.title)
print("Ссылка на изображение:")
print(video.thumbnail_url)
tnail = str(video.thumbnail_url)
print("Введите имя изображения:")
img_name = str(input())
img = requests.get(tnail)
img_option = open(img_name + '.jpg','wb')
img_option.write(img.content)
img_option.close
print("Описание видео:")
print(video.description)
print("Загрузка видео в максимальном разрешении:")
video = video.streams.get_highest_resolution()
video = video.download()



