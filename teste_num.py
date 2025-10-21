import pywhatkit as kit
import time

# Lista de números para testar
numeros = [
    "+5511999999999",
    "+5511999999999"
]

mensagem = "Olá! Eu que vou passar o nome da pessoa que você tirou no amigo secreto, então anota esse número e fique ligeiro(a)"

for numero in numeros:
    try:
        print(f"🔍 Estou testando uma paradinha aqui {numero}...")
        kit.sendwhatmsg_instantly(numero, mensagem, wait_time=10, tab_close=True)
        time.sleep(5)
    except Exception as e:
        print(f"❌ Número {numero} pode não estar ativo ({e})")
