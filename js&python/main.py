#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests as req

arr = []

# resp = req.get("https://omambe.ru/perepiska/voprosy-devushke-v-igre-pravda-ili-dejstvie")
resp = req.get("https://babyben.ru/otnosheniya/igra-s-parnem-v-voprosy-pravda-ili-dejstvie-spisok-prikolnyh-interesnyh-i-neozhidannyh-voprosov-i-zadanij-kakuyu-pravdu-mozhno-sprosit-u-parnya-v-igre-pravda-ili-dejstvie-10-100-1000-luchshih-vo.html")

soup = BeautifulSoup(resp.text, 'lxml')

# Запись в текстовый файл
# f = open('text2.txt', 'w')
for i in soup.find_all('ul'):
	print(i.text)
	# f.write(f"{i.text}\n\n")
# f.close()

# Чтение текстового файла
# f = open('text2.txt')
# print(f.read())