# 👾 CHEFÃO FINAL: este robô tem 5 erros. Achem todos em 5 minutos!
# Dica: rode, leia a mensagem de erro, conserte UM erro, rode de novo.
emojis = {
    "gato": "🐱",
    "pizza": "🍕",
    "feliz": "😀"
}

frase = "o gato feliz comeu pizza"
traducao = []
for palavra in frase.split():
    traducao.append(emojis.get(palavra, palavra))  

print(" ".join(traducao))