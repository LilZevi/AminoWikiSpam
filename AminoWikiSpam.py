from colorama import init
from colorama import Fore, Back, Style
init()
print(Back.BLACK)
print(Fore.GREEN)
print("Script by Zevi/Скрипт сделан Zevi")
print("┌────────────────────────────────────┐")
print("│Author :  LilZevi                   │")
print("│Github : https://github.com/LilZevi │")
print("└────────────────────────────────────┘")
print("YouTube: https://www.youtube.com/channel/UCJ61JlXJckmO6yJr8BDRuGQ")
print("▄▀▄ █▄░▄█ ▀ █▄░█ ▄▀▄ █░░░█ ▀ █░▄▀ ▀ ▄▀▀ █▀▄ ▄▀▄ █▄░▄█")
print("█▀█ █░█░█ █ █░▀█ █░█ █░█░█ █ █▀▄░ █ ░▀▄ █░█ █▀█ █░█░█")
print("▀░▀ ▀░░░▀ ▀ ▀░░▀ ░▀░ ░▀░▀░ ▀ ▀░▀▀ ▀ ▀▀░ █▀░ ▀░▀ ▀░░░▀")
import amino
client = amino.Client()
email=input("Email/Почта:")
password=input("Password/Пароль:")
for name, id in zip(client.sub_clients().name, client.sub_clients().comId):
    print(f"{name}: {id}")
comid = input("Выберите сообщество(id): ")
client = amino.Client() 
client.login(email=email, password=password)
print('\nLogged in/Бот зашел!')
wikilk=input("Type WikiLink/Введите ссылку на статью:")
wiki=client.get_from_code(wikilk)
wikiId=wiki.objectId
comId=wiki.path[1:wiki.path.index('/')]
subclient=amino.SubClient(comId=comid ,profile=client.profile)
comment=input("Type a Comment/Введите коммент:")
while True:
	try:
		sub_client.comment(message=comment, wikiId=wikiId)
		print("Comment Sended/Коммент отправлен")
	except:
		pass
