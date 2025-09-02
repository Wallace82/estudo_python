import re

url = input("digite uma url: ")

if re.match(r'^https?://[^\s/$.?#].[^\s]*\.com$', url):
    print(f"Url válida terminando com {url}.")
else:
    print(f"Url inválida não termina com {url}.")