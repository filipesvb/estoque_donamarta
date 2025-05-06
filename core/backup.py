import os
import shutil
from datetime import datetime
from core.logging import registrar_log

CAMINHO_PASTA_BACKUPS = "backups"
CAMINHO_PRODUTOS = os.path.join("data", "estoque.json")

def garantir_estrutura():
    if not os.path.exists(CAMINHO_PASTA_BACKUPS):
        os.makedirs(CAMINHO_PASTA_BACKUPS)
        
def registrar_backup(dados):
    if not os.path.exists(CAMINHO_PRODUTOS):
        return

    if not dados:
        print("não tem dados")
        return

    garantir_estrutura()

    data_hora = datetime.now().strftime('%d%m%Y_%H%M%S')

    novo_arquivo = f"backup_{data_hora}.txt"
    caminho_novo_arquivo = os.path.join(CAMINHO_PASTA_BACKUPS, novo_arquivo)
    shutil.copy(CAMINHO_PRODUTOS, caminho_novo_arquivo)

    print(f"✅ Backup realizado com sucesso: {novo_arquivo}")
    registrar_log(f"Backup criado: {novo_arquivo}")
    

