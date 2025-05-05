from datetime import datetime
import os

CAMINHO_PASTA_LOGS = "logs"
CAMINHO_ARQUIVO_LOGS = os.path.join(CAMINHO_PASTA_LOGS, "log.txt")

def garantir_estrutura():
    if not os.path.exists(CAMINHO_PASTA_LOGS):
        os.makedirs(CAMINHO_PASTA_LOGS)
    if not os.path.exists(CAMINHO_ARQUIVO_LOGS):
        with open(CAMINHO_ARQUIVO_LOGS, 'w', encoding='utf-8') as arq:
            arq.write('')

def registrar_log(mensagem = "Operação ? realizada"):

    garantir_estrutura()

    data_hora = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")

    novoLog = f"[{data_hora}] {mensagem}\n"

    with open(CAMINHO_ARQUIVO_LOGS, 'a', encoding='utf-8') as arq:
        arq.write(novoLog)
    
