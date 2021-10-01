import re

padrao = "\w{5,50}@[a-z]{3,10}.com.br"
texto = "aaabbbcc lucas28@gmail.com.br"
resposta = re.search(padrao, texto)
print(resposta.group)
