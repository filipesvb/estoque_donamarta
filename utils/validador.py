from errors.exceptions import ErroNomeInvalido, ErroPrecoInvalido, ErroQuantidadeInvalida

    
def validar_nome(nome : str): 
    if not nome or not nome.strip():
        raise ErroNomeInvalido("⚠️  O nome não pode ser vazio")
    if not all(palavra.isalpha() for palavra in nome.strip().split()):
        raise ErroNomeInvalido("⚠️ O nome deve conter apenas letras.")
    if len(nome.strip()) < 6:
        raise ErroNomeInvalido("⚠️  O nome deve ter mais do que 6 caracteres.")

    return nome

def validar_quantidade(qtd : int):
    if not qtd.strip():
        raise ErroQuantidadeInvalida("⚠️  A quantidade não pode ser vazia.")
    try:
        qtd = int(qtd)
    except ValueError:
        raise ErroQuantidadeInvalida("⚠️  A quantidade deve ser um número inteiro válido.")
    
    if qtd < 0:
        raise ErroQuantidadeInvalida("⚠️  A quantidade não pode ser menor que zero.")
    
    return qtd

def validar_preco(preco : float):
    if not preco.strip():
        raise ErroPrecoInvalido("⚠️  O preço não pode ser vazio.")
    try:
        preco = float(preco.strip())

        if preco < 0:
            raise ErroPrecoInvalido("⚠️  O preço não pode ser menor que zero.")
    except ValueError:
        raise ErroPrecoInvalido("⚠️  O preço deve ser um número real válido.")
    
    return preco
    
def validar_edicao_nome(nome : str): 
    if not nome or not nome.strip():
        return nome
    if not all(palavra.isalpha() for palavra in nome.strip().split()):
        raise ErroNomeInvalido("⚠️ O nome deve conter apenas letras.")
    if len(nome.strip()) < 6:
        raise ErroNomeInvalido("⚠️  O nome deve ter mais do que 6 caracteres.")

    return nome

def validar_edicao_quantidade(qtd : int):
    if not qtd.strip():
        return qtd
    try:
        qtd = int(qtd)
    except ValueError:
        raise ErroQuantidadeInvalida("⚠️  A quantidade deve ser um número inteiro válido.")
    
    if qtd < 0:
        raise ErroQuantidadeInvalida("⚠️  A quantidade não pode ser menor que zero.")
    
    return qtd

def validar_edicao_preco(preco : float):
    if not preco.strip():
        return preco
    try:
        preco = float(preco.strip())

        if preco < 0:
            raise ErroPrecoInvalido("⚠️  O preço não pode ser menor que zero.")
    except ValueError:
        raise ErroPrecoInvalido("⚠️  O preço deve ser um número real válido.")
    

    return preco