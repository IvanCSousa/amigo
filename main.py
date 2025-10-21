import random
import time
import urllib.parse
import os
import webbrowser

# # Lista de participantes
# pessoas = [
#     {"nome": "Ana", "tel": "+5599999999999"},
#     {"nome": "João", "tel": "+5598888888888"},
#     {"nome": "Bia", "tel": "+5597777777777"},
#     {"nome": "Carlos", "tel": "+5596666666666"}
# ]

# Lê participantes de um arquivo .txt
def ler_participantes(caminho_arquivo):
    participantes = []
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if not linha:
                continue  # pula linhas vazias
            try:
                nome, tel = [x.strip() for x in linha.split(",", 1)]
                participantes.append({"nome": nome, "tel": tel})
            except ValueError:
                print(f"⚠️ Linha ignorada (formato incorreto): {linha}")
    return participantes


# Caminho do arquivo
ARQUIVO_PARTICIPANTES = "participantes.txt"

# Lê os dados do arquivo
pessoas = ler_participantes(ARQUIVO_PARTICIPANTES)

# Embaralha a lista (só uma vez)
random.shuffle(pessoas)

# Cria pares no formato circular
pares = []
for i in range(len(pessoas)):
    atual = pessoas[i]
    sorteado = pessoas[(i + 1) % len(pessoas)]  # o último tira o primeiro
    pares.append({
        "de": atual["nome"],
        "tel": atual["tel"],
        "para": sorteado["nome"]
    })

# Mostra resultado no console
print("🎉 Resultado do sorteio:\n")
for p in pares:
    print(f"{p['de']} → {p['para']}")
print("\n✅ Iniciando envio das mensagens...\n")

# Função para gerar link do WhatsApp
def gerar_link_whatsapp(numero: str, mensagem: str) -> str:
    numero = numero.replace("+", "").replace(" ", "")
    texto = urllib.parse.quote(mensagem)
    return f"https://wa.me/{numero}?text={texto}"

# Gera os links do Amigo Secreto
print("\n🎉 Gerando links personalizados do Amigo Secreto...\n")

with open("links_gerados.txt", "w") as f:
    for p in pares:
        msg = f"🎁 Olá {p['de']}! Você tirou {p['para']} no Amigo Secreto! 🤫"
        link = gerar_link_whatsapp(p["tel"], msg)

        # print(f"🔗 {p['de']} ({p['tel']}): {link}")
        print(f"{link}")
        f.write(f"{link}\n")

        time.sleep(1)  # pequena pausa só para legibilidade no terminal

print("\n✅ Todos os links foram gerados e salvos em 'links_gerados.txt'!")
