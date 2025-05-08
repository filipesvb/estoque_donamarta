

class ErroNomeInvalido(Exception) :
    def __init__(self, msg="Nome inválido!"):
        super().__init__(msg)
        self.message = msg
    
class ErroQuantidadeInvalida(Exception) :
    def __init__(self, msg="Quantidade inválida!"):
        super().__init__(msg)
        self.message = msg

class ErroPrecoInvalido(Exception) :
    def __init__(self, msg="Preço inválido!"):
        super().__init__(msg)
        self.message = msg