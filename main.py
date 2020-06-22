# import random
from http.server import HTTPServer, CGIHTTPRequestHandler
server_address = ("", 8000)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever()



# value_com = int(input('Введите количество команд: '))
# arr = []

# def start(value):
# 	for i in range(value):
# 		com = input(f'Введите имена игроков {i+1} команды (через И): ')
# 		arr.append(com)
# 		# print(com.lower().split(' и '))

# start(value_com)
# print(arr)